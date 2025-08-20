import os
import re
import json
import hashlib
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
import chromadb
from chromadb.config import Settings
import boto3
from botocore.exceptions import ClientError
import numpy as np


@dataclass
class CodeChunk:
    """Represents a chunk of COBOL code with metadata"""
    content: str
    start_line: int
    end_line: int
    section_type: str
    summary: str
    pseudo_code: str
    file_name: str


class TitanEmbeddings:
    """Handles AWS Titan embeddings"""
    
    def __init__(self, region_name='us-east-1'):
        self.bedrock = boto3.client('bedrock-runtime', region_name=region_name)
        self.model_id = 'amazon.titan-embed-text-v1'
    
    def get_embedding(self, text: str) -> List[float]:
        """Get embedding for text using Titan"""
        try:
            body = json.dumps({
                "inputText": text,
            })
            
            response = self.bedrock.invoke_model(
                body=body,
                modelId=self.model_id,
                accept='application/json',
                contentType='application/json'
            )
            
            response_body = json.loads(response.get('body').read())
            return response_body.get('embedding')
            
        except ClientError as e:
            print(f"Error getting embedding: {e}")
            return None


class ClaudeClient:
    """Handles Claude 3.5 Sonnet API calls via AWS Bedrock"""
    
    def __init__(self, region_name='us-east-1'):
        self.bedrock = boto3.client('bedrock-runtime', region_name=region_name)
        self.model_id = 'anthropic.claude-3-5-sonnet-20241022-v2:0'
    
    def generate_response(self, prompt: str, max_tokens: int = 4000) -> str:
        """Generate response using Claude 3.5 Sonnet"""
        try:
            body = json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": max_tokens,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
            
            response = self.bedrock.invoke_model(
                body=body,
                modelId=self.model_id,
                accept='application/json',
                contentType='application/json'
            )
            
            response_body = json.loads(response.get('body').read())
            return response_body['content'][0]['text']
            
        except ClientError as e:
            print(f"Error calling Claude: {e}")
            return ""


class COBOLChunker:
    """Intelligent COBOL code chunker that respects program structure"""
    
    def __init__(self):
        self.cobol_sections = [
            'IDENTIFICATION DIVISION',
            'ENVIRONMENT DIVISION',
            'DATA DIVISION',
            'PROCEDURE DIVISION',
            'WORKING-STORAGE SECTION',
            'FILE SECTION',
            'LINKAGE SECTION',
            'LOCAL-STORAGE SECTION'
        ]
        
        self.cobol_paragraphs = r'^[\s]*([A-Z0-9][A-Z0-9\-]*)\.\s*$'
        self.max_chunk_size = 2000  # Maximum lines per chunk
    
    def identify_section_type(self, lines: List[str]) -> str:
        """Identify the type of COBOL section"""
        content = '\n'.join(lines[:10]).upper()  # Check first 10 lines
        
        for section in self.cobol_sections:
            if section in content:
                return section
        
        # Check for paragraph names
        for line in lines[:5]:
            if re.match(self.cobol_paragraphs, line.strip(), re.IGNORECASE):
                return 'PROCEDURE PARAGRAPH'
        
        return 'CODE BLOCK'
    
    def chunk_cobol_file(self, file_path: str) -> List[CodeChunk]:
        """Chunk COBOL file intelligently based on structure"""
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        chunks = []
        current_chunk = []
        current_start = 0
        file_name = os.path.basename(file_path)
        
        i = 0
        while i < len(lines):
            line = lines[i].strip().upper()
            
            # Check for COBOL division/section boundaries
            is_boundary = any(section in line for section in self.cobol_sections)
            
            # Check for paragraph boundaries (ending with .)
            is_paragraph = re.match(self.cobol_paragraphs, lines[i].strip(), re.IGNORECASE)
            
            if (is_boundary or is_paragraph or len(current_chunk) >= self.max_chunk_size) and current_chunk:
                # Create chunk from accumulated lines
                section_type = self.identify_section_type(current_chunk)
                chunk_content = ''.join(current_chunk)
                
                chunk = CodeChunk(
                    content=chunk_content,
                    start_line=current_start + 1,
                    end_line=i,
                    section_type=section_type,
                    summary="",  # Will be filled by LLM
                    pseudo_code="",  # Will be filled by LLM
                    file_name=file_name
                )
                chunks.append(chunk)
                
                # Start new chunk
                current_chunk = []
                current_start = i
            
            current_chunk.append(lines[i])
            i += 1
        
        # Add final chunk if exists
        if current_chunk:
            section_type = self.identify_section_type(current_chunk)
            chunk_content = ''.join(current_chunk)
            
            chunk = CodeChunk(
                content=chunk_content,
                start_line=current_start + 1,
                end_line=len(lines),
                section_type=section_type,
                summary="",
                pseudo_code="",
                file_name=file_name
            )
            chunks.append(chunk)
        
        return chunks


class RAGPseudoCodeGenerator:
    """Main class for RAG-based pseudo code generation"""
    
    def __init__(self, chroma_db_path: str = "./chroma_db", region_name: str = 'us-east-1'):
        self.chroma_client = chromadb.PersistentClient(path=chroma_db_path)
        self.collection_name = "cobol_chunks"
        
        # Initialize collection
        try:
            self.collection = self.chroma_client.get_collection(name=self.collection_name)
        except:
            self.collection = self.chroma_client.create_collection(
                name=self.collection_name,
                metadata={"hnsw:space": "cosine"}
            )
        
        self.embeddings = TitanEmbeddings(region_name)
        self.claude = ClaudeClient(region_name)
        self.chunker = COBOLChunker()
    
    def generate_chunk_summary(self, chunk: CodeChunk) -> str:
        """Generate summary for a code chunk using Claude"""
        prompt = f"""
        Analyze this COBOL code chunk and provide a concise summary (2-3 sentences) of what it does:
        
        Section Type: {chunk.section_type}
        File: {chunk.file_name}
        Lines: {chunk.start_line}-{chunk.end_line}
        
        COBOL Code:
        {chunk.content}
        
        Focus on:
        1. Main functionality
        2. Key variables/data structures
        3. Business logic purpose
        
        Summary:
        """
        
        return self.claude.generate_response(prompt, max_tokens=500)
    
    def generate_chunk_pseudocode(self, chunk: CodeChunk) -> str:
        """Generate pseudo code for a chunk using Claude"""
        prompt = f"""
        Convert this COBOL code chunk to detailed pseudo code. Use clear, structured pseudo code with proper indentation and logic flow:
        
        Section Type: {chunk.section_type}
        File: {chunk.file_name}
        
        COBOL Code:
        {chunk.content}
        
        Generate pseudo code that:
        1. Shows the logical flow clearly
        2. Explains data operations
        3. Describes business rules
        4. Uses readable variable names
        5. Includes comments for complex logic
        
        Pseudo Code:
        ```
        """
        
        return self.claude.generate_response(prompt, max_tokens=2000)
    
    def process_and_store_chunks(self, cobol_file_path: str):
        """Process COBOL file, generate summaries/pseudocode, and store in vector DB"""
        print(f"Processing COBOL file: {cobol_file_path}")
        
        # Chunk the file
        chunks = self.chunker.chunk_cobol_file(cobol_file_path)
        print(f"Created {len(chunks)} chunks")
        
        # Process each chunk
        for i, chunk in enumerate(chunks):
            print(f"Processing chunk {i+1}/{len(chunks)}")
            
            # Generate summary and pseudo code
            chunk.summary = self.generate_chunk_summary(chunk)
            chunk.pseudo_code = self.generate_chunk_pseudocode(chunk)
            
            # Create embedding text (combination of content and summary)
            embedding_text = f"{chunk.summary}\n\n{chunk.content[:1000]}"  # Truncate content for embedding
            
            # Get embedding
            embedding = self.embeddings.get_embedding(embedding_text)
            
            if embedding:
                # Create unique ID
                chunk_id = hashlib.md5(f"{chunk.file_name}_{chunk.start_line}_{chunk.end_line}".encode()).hexdigest()
                
                # Store in ChromaDB
                self.collection.add(
                    embeddings=[embedding],
                    documents=[chunk.content],
                    metadatas=[{
                        "file_name": chunk.file_name,
                        "start_line": chunk.start_line,
                        "end_line": chunk.end_line,
                        "section_type": chunk.section_type,
                        "summary": chunk.summary,
                        "pseudo_code": chunk.pseudo_code
                    }],
                    ids=[chunk_id]
                )
                
                print(f"Stored chunk {chunk_id}")
    
    def retrieve_relevant_chunks(self, query: str, n_results: int = 5) -> List[Dict]:
        """Retrieve relevant chunks based on query"""
        query_embedding = self.embeddings.get_embedding(query)
        
        if not query_embedding:
            return []
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        relevant_chunks = []
        for i in range(len(results['ids'][0])):
            relevant_chunks.append({
                'id': results['ids'][0][i],
                'content': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else 0
            })
        
        return relevant_chunks
    
    def generate_comprehensive_pseudocode(self, query: str, output_file: str = "pseudocode_output.md"):
        """Generate comprehensive pseudo code based on query"""
        print(f"Generating pseudo code for query: {query}")
        
        # Retrieve relevant chunks
        relevant_chunks = self.retrieve_relevant_chunks(query, n_results=10)
        
        if not relevant_chunks:
            print("No relevant chunks found")
            return
        
        # Prepare context from relevant chunks
        context_parts = []
        for chunk in relevant_chunks:
            context_parts.append(f"""
### Chunk from {chunk['metadata']['file_name']} (Lines {chunk['metadata']['start_line']}-{chunk['metadata']['end_line']})
**Section Type:** {chunk['metadata']['section_type']}
**Summary:** {chunk['metadata']['summary']}
**Pseudo Code:**
```
{chunk['metadata']['pseudo_code']}
```
**Original Code Snippet:**
```cobol
{chunk['content'][:500]}...
```
""")
        
        context = "\n".join(context_parts)
        
        # Generate comprehensive pseudo code
        prompt = f"""
        Based on the following COBOL code chunks and their individual pseudo codes, generate a comprehensive, 
        well-structured pseudo code document that addresses this query: "{query}"
        
        Relevant Code Chunks:
        {context}
        
        Generate a comprehensive pseudo code document that:
        1. Provides an overview of the functionality
        2. Shows the complete logical flow
        3. Explains data structures and variables
        4. Describes business logic and rules
        5. Includes error handling where applicable
        6. Uses proper pseudo code formatting
        7. Adds explanatory comments
        
        Structure the output as a proper markdown document with:
        - Title and description
        - Table of contents
        - Main pseudo code sections
        - Data structures section
        - Business rules section
        - Notes and assumptions
        
        Comprehensive Pseudo Code Document:
        """
        
        comprehensive_pseudocode = self.claude.generate_response(prompt, max_tokens=4000)
        
        # Save to markdown file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Pseudo Code Generation Results\n\n")
            f.write(f"**Query:** {query}\n\n")
            f.write(f"**Generated on:** {os.popen('date').read().strip()}\n\n")
            f.write("---\n\n")
            f.write(comprehensive_pseudocode)
            f.write("\n\n---\n\n")
            f.write("## Source Chunks Used\n\n")
            
            for i, chunk in enumerate(relevant_chunks, 1):
                f.write(f"### {i}. {chunk['metadata']['file_name']} (Lines {chunk['metadata']['start_line']}-{chunk['metadata']['end_line']})\n")
                f.write(f"**Section:** {chunk['metadata']['section_type']}\n")
                f.write(f"**Relevance Score:** {1 - chunk['distance']:.3f}\n")
                f.write(f"**Summary:** {chunk['metadata']['summary']}\n\n")
        
        print(f"Comprehensive pseudo code saved to: {output_file}")


# Example usage
def main():
    """Main function demonstrating the usage"""
    
    # Initialize the RAG system
    rag_generator = RAGPseudoCodeGenerator(
        chroma_db_path="./cobol_vector_db",
        region_name='us-east-1'  # Change to your AWS region
    )
    
    # Process a COBOL file (replace with your file path)
    cobol_file_path = "path/to/your/cobol/file.cbl"
    
    # Check if file exists
    if os.path.exists(cobol_file_path):
        # Process and store chunks
        rag_generator.process_and_store_chunks(cobol_file_path)
        
        # Generate pseudo code for specific queries
        queries = [
            "data validation and input processing logic",
            "file handling and record processing",
            "calculation and business logic",
            "error handling and exception processing"
        ]
        
        for query in queries:
            output_file = f"pseudocode_{query.replace(' ', '_').replace('/', '_')}.md"
            rag_generator.generate_comprehensive_pseudocode(query, output_file)
    
    else:
        print(f"COBOL file not found: {cobol_file_path}")
        print("Please update the cobol_file_path variable with your actual file path")


if __name__ == "__main__":
    main()
