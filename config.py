# requirements.txt
chromadb==0.4.18
boto3==1.34.0
numpy==1.24.3
python-dotenv==1.0.0

# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration settings for the COBOL RAG system"""
    
    # AWS Configuration
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    
    # Model Configuration
    TITAN_MODEL_ID = 'amazon.titan-embed-text-v1'
    CLAUDE_MODEL_ID = 'anthropic.claude-3-5-sonnet-20241022-v2:0'
    
    # ChromaDB Configuration
    CHROMA_DB_PATH = os.getenv('CHROMA_DB_PATH', './cobol_vector_db')
    COLLECTION_NAME = 'cobol_chunks'
    
    # Chunking Configuration
    MAX_CHUNK_SIZE = int(os.getenv('MAX_CHUNK_SIZE', '2000'))
    MAX_EMBEDDING_TEXT_LENGTH = int(os.getenv('MAX_EMBEDDING_TEXT_LENGTH', '1000'))
    
    # Output Configuration
    OUTPUT_DIR = os.getenv('OUTPUT_DIR', './pseudocode_output')
    
    @classmethod
    def ensure_output_dir(cls):
        """Ensure output directory exists"""
        os.makedirs(cls.OUTPUT_DIR, exist_ok=True)

# .env (example file)
"""
# AWS Configuration
AWS_REGION=us-east-1
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here

# Database Configuration
CHROMA_DB_PATH=./cobol_vector_db

# Processing Configuration
MAX_CHUNK_SIZE=2000
MAX_EMBEDDING_TEXT_LENGTH=1000

# Output Configuration
OUTPUT_DIR=./pseudocode_output
"""

# batch_processor.py
import os
import glob
from typing import List
from cobol_rag_pseudocode import RAGPseudoCodeGenerator, Config

class BatchProcessor:
    """Process multiple COBOL files in batch"""
    
    def __init__(self):
        self.rag_generator = RAGPseudoCodeGenerator(
            chroma_db_path=Config.CHROMA_DB_PATH,
            region_name=Config.AWS_REGION
        )
        Config.ensure_output_dir()
    
    def find_cobol_files(self, directory: str) -> List[str]:
        """Find all COBOL files in directory"""
        patterns = ['*.cbl', '*.cob', '*.cobol', '*.CBL', '*.COB', '*.COBOL']
        cobol_files = []
        
        for pattern in patterns:
            cobol_files.extend(glob.glob(os.path.join(directory, '**', pattern), recursive=True))
        
        return cobol_files
    
    def process_directory(self, directory: str):
        """Process all COBOL files in a directory"""
        cobol_files = self.find_cobol_files(directory)
        
        print(f"Found {len(cobol_files)} COBOL files in {directory}")
        
        for i, file_path in enumerate(cobol_files, 1):
            print(f"\nProcessing file {i}/{len(cobol_files)}: {file_path}")
            try:
                self.rag_generator.process_and_store_chunks(file_path)
                print(f"Successfully processed: {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")
    
    def generate_pseudocode_for_queries(self, queries: List[str]):
        """Generate pseudo code for multiple queries"""
        for query in queries:
            output_file = os.path.join(
                Config.OUTPUT_DIR,
                f"pseudocode_{query.replace(' ', '_').replace('/', '_')}.md"
            )
            print(f"\nGenerating pseudo code for: {query}")
            self.rag_generator.generate_comprehensive_pseudocode(query, output_file)

# query_interface.py
class QueryInterface:
    """Interactive query interface for pseudo code generation"""
    
    def __init__(self):
        self.rag_generator = RAGPseudoCodeGenerator(
            chroma_db_path=Config.CHROMA_DB_PATH,
            region_name=Config.AWS_REGION
        )
        Config.ensure_output_dir()
    
    def interactive_query(self):
        """Interactive query interface"""
        print("COBOL Pseudo Code Generator")
        print("=" * 40)
        
        while True:
            print("\nOptions:")
            print("1. Generate pseudo code for a specific query")
            print("2. List common query templates")
            print("3. Exit")
            
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                query = input("Enter your query: ").strip()
                if query:
                    output_file = os.path.join(
                        Config.OUTPUT_DIR,
                        f"pseudocode_{query.replace(' ', '_')[:50]}.md"
                    )
                    self.rag_generator.generate_comprehensive_pseudocode(query, output_file)
                    print(f"Pseudo code generated: {output_file}")
            
            elif choice == '2':
                self.show_query_templates()
            
            elif choice == '3':
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def show_query_templates(self):
        """Show common query templates"""
        templates = [
            "data validation and input processing",
            "file handling and record processing", 
            "calculation and business logic",
            "error handling and exception management",
            "database operations and SQL calls",
            "report generation logic",
            "batch processing workflow",
            "data transformation and formatting",
            "conditional logic and decision making",
            "loop processing and iteration logic"
        ]
        
        print("\nCommon Query Templates:")
        print("-" * 30)
        for i, template in enumerate(templates, 1):
            print(f"{i:2d}. {template}")
        
        choice = input("\nSelect a template (1-10) or press Enter to return: ").strip()
        
        if choice.isdigit() and 1 <= int(choice) <= len(templates):
            selected_query = templates[int(choice) - 1]
            output_file = os.path.join(
                Config.OUTPUT_DIR,
                f"pseudocode_{selected_query.replace(' ', '_')}.md"
            )
            print(f"Generating pseudo code for: {selected_query}")
            self.rag_generator.generate_comprehensive_pseudocode(selected_query, output_file)
            print(f"Pseudo code generated: {output_file}")

# Example usage script
def example_usage():
    """Example of how to use the system"""
    
    # Single file processing
    rag_gen = RAGPseudoCodeGenerator()
    rag_gen.process_and_store_chunks("path/to/your/cobol/file.cbl")
    
    # Batch processing
    batch_processor = BatchProcessor()
    batch_processor.process_directory("path/to/cobol/directory")
    
    # Generate pseudo code for common queries
    common_queries = [
        "data validation and input processing logic",
        "file handling and record processing",
        "calculation and business logic",
        "error handling and exception processing"
    ]
    batch_processor.generate_pseudocode_for_queries(common_queries)
    
    # Interactive mode
    query_interface = QueryInterface()
    query_interface.interactive_query()

if __name__ == "__main__":
    example_usage()
