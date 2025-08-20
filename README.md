# COBOL Pseudo Code Generator with RAG

A comprehensive solution for generating pseudo code from large mainframe COBOL files using Retrieval-Augmented Generation (RAG) with ChromaDB, AWS Titan embeddings, and Claude 3.5 Sonnet.

## Features

- **Intelligent Chunking**: Respects COBOL program structure (divisions, sections, paragraphs)
- **LLM-Generated Summaries**: Creates summaries for each chunk using Claude 3.5 Sonnet
- **Vector Storage**: Uses ChromaDB with Titan embeddings for efficient retrieval
- **RAG-Based Generation**: Generates comprehensive pseudo code using relevant chunks
- **Batch Processing**: Process multiple COBOL files at once
- **Interactive Interface**: Query-based pseudo code generation

## Prerequisites

### AWS Setup
1. AWS account with access to Amazon Bedrock
2. Enable Claude 3.5 Sonnet and Titan embeddings in Bedrock
3. Proper IAM permissions for Bedrock access

### Python Requirements
- Python 3.8 or higher
- Required packages (see requirements.txt)

## Installation

1. **Clone/Download the code files**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up AWS credentials**
   - Option 1: AWS CLI configuration
   ```bash
   aws configure
   ```
   
   - Option 2: Environment variables
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_REGION=us-east-1
   ```
   
   - Option 3: Create `.env` file
   ```
   AWS_REGION=us-east-1
   AWS_ACCESS_KEY_ID=your_access_key_here
   AWS_SECRET_ACCESS_KEY=your_secret_key_here
   CHROMA_DB_PATH=./cobol_vector_db
   OUTPUT_DIR=./pseudocode_output
   ```

4. **Verify Bedrock access**
```bash
aws bedrock list-foundation-models --region us-east-1
```

## Usage

### 1. Single File Processing

```python
from cobol_rag_pseudocode import RAGPseudoCodeGenerator

# Initialize the generator
rag_gen = RAGPseudoCodeGenerator(
    chroma_db_path="./cobol_vector_db",
    region_name="us-east-1"
)

# Process a single COBOL file
rag_gen.process_and_store_chunks("path/to/your/cobol_file.cbl")

# Generate pseudo code for specific functionality
rag_gen.generate_comprehensive_pseudocode(
    "data validation and input processing logic",
    "data_validation_pseudocode.md"
)
```

### 2. Batch Processing

```python
from batch_processor import BatchProcessor

# Initialize batch processor
processor = BatchProcessor()

# Process all COBOL files in a directory
processor.process_directory("path/to/cobol/directory")

# Generate pseudo code for common queries
queries = [
    "file handling and record processing",
    "calculation and business logic",
    "error handling procedures"
]
processor.generate_pseudocode_for_queries(queries)
```

### 3. Interactive Mode

```python
from query_interface import QueryInterface

# Start interactive interface
interface = QueryInterface()
interface.interactive_query()
```

### 4. Command Line Usage

```bash
# Process files and generate pseudo code
python cobol_rag_pseudocode.py

# Batch processing
python batch_processor.py

# Interactive mode
python query_interface.py
```

## Configuration Options

### Environment Variables
- `AWS_REGION`: AWS region (default: us-east-1)
- `CHROMA_DB_PATH`: Path to ChromaDB storage (default: ./cobol_vector_db)
- `MAX_CHUNK_SIZE`: Maximum lines per chunk (default: 2000)
- `OUTPUT_DIR`: Output directory for generated files (default: ./pseudocode_output)

### Chunking Strategy
The system intelligently chunks COBOL code based on:
- **Division boundaries** (IDENTIFICATION, ENVIRONMENT, DATA, PROCEDURE)
- **Section boundaries** (WORKING-STORAGE, FILE, LINKAGE sections)
- **Paragraph boundaries** (paragraph names ending with .)
- **Size limits** (max 2000 lines per chunk)

### Common Query Types

1. **Data Operations**
   - "data validation and input processing logic"
   - "data transformation and formatting"
   - "record handling and field processing"

2. **File Operations**
   - "file handling and record processing"
   - "file input/output operations"
   - "sequential file processing"

3. **Business Logic**
   - "calculation and business logic"
   - "conditional logic and decision making"
   - "business rule implementation"

4. **Error Handling**
   - "error handling and exception processing"
   - "validation and error checking"
   - "exception management procedures"

5. **Control Flow**
   - "loop processing and iteration logic"
   - "program flow control"
   - "conditional branching logic"

## Output Format

The system generates comprehensive markdown files containing:

### Main Sections
- **Overview**: High-level description of functionality
- **Pseudo Code**: Structured pseudo code with proper indentation
- **Data Structures**: Description of key variables and data elements
- **Business Rules**: Explanation of business logic and rules
- **Error Handling**: Exception handling procedures
- **Notes**: Additional assumptions and considerations

### Source Information
- **Source Chunks**: Details of COBOL chunks used
- **Relevance Scores**: How relevant each chunk is to the query
- **File References**: Original file names and line numbers

## Example Output Structure

```markdown
# Pseudo Code Generation Results

**Query:** data validation and input processing logic

## Overview
This pseudo code describes the data validation and input processing...

## Main Processing Logic
```
BEGIN data_validation_process
    INITIALIZE validation_flags
    FOR each input_record
        VALIDATE record_format
        IF format_valid THEN
            PROCESS field_validations
            UPDATE validation_counters
        ELSE
            LOG validation_error
            SET error_flag
        END IF
    END FOR
END data_validation_process
```

## Data Structures
- input_record: Main input data structure
- validation_
