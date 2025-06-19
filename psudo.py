def create_pseudocode_documentation_prompt(code_content, filename):
    """Create a prompt for generating pseudocode documentation in plain English"""
    return f"""Generate comprehensive pseudocode documentation that explains the application logic in plain English. Break down the code into logical segments and provide step-by-step explanations of what the application does, how it works, and what each part accomplishes. Use clear, conversational language that anyone can understand.

# Pseudocode Documentation: {filename}

## 1. Application Overview
Explain in simple terms what this application does overall. Describe its main purpose, who would use it, and what problem it solves. Use plain English to describe the big picture without technical jargon.

## 2. Core Logic Breakdown

### 2.1 Data Handling Logic
Describe in plain English how the application handles data with SPECIFIC DETAILS from the code:
- What EXACT types of information does it work with? (Be specific: customer records, transaction files, configuration data, etc.)
- What are the EXACT file names, database tables, or data sources it reads from?
- What are the SPECIFIC data fields, columns, or parameters it processes?
- What EXACT formats does the data come in? (CSV, JSON, fixed-width, database records, etc.)
- What are the SPECIFIC file paths, directories, or locations mentioned in the code?
- What EXACT information does it produce or output?
- What are the SPECIFIC output file names, destinations, or targets?

Example: "The application reads customer transaction data from the file '/data/daily_transactions.csv' which contains fields like customer_id, transaction_amount, transaction_date, and product_code. It also reads configuration settings from 'config/app_settings.xml' including database connection strings, retry limits (set to 3), and timeout values (30 seconds)."

### 2.2 Main Operations Logic
Break down the main things the application does with SPECIFIC CONTEXTUAL DETAILS:
- Step 1: [What EXACTLY happens first? Include specific file names, function names, or operations]
- Step 2: [What EXACTLY happens next? Include specific data being processed, calculations being performed]
- Step 3: [Continue with SPECIFIC details about each operation, including actual values, thresholds, or conditions mentioned in the code]

Include SPECIFIC details like:
- Exact function names or method calls
- Specific configuration parameters and their values
- Actual file names, paths, and extensions
- Precise data transformations or calculations
- Specific business rules with actual threshold values
- Exact error codes or status messages

Example: "First, the application calls the 'loadConfiguration()' function to read settings from 'app.properties' including the batch_size (500 records), max_retry_attempts (3), and database_url. Then it opens the input file 'daily_sales_YYYYMMDD.dat' and reads records in batches of 500."

### 2.3 Decision Making Logic
Describe how the application makes decisions with SPECIFIC CONDITIONS and VALUES:
- What EXACT choices does it need to make? (Include specific conditional statements)
- What SPECIFIC information or values does it use to decide? (Include actual field names, thresholds, flags)
- What EXACTLY happens in different scenarios? (Include specific outcomes, file names, actions)
- What are the EXACT conditions checked? (Include specific comparison values, status codes, flags)

Use specific "if-then" language: "If the transaction_amount is greater than $10,000, then the application writes the record to 'high_value_transactions.log' and sends an alert email to 'compliance@company.com'. If the customer_status equals 'SUSPENDED', then it skips processing and writes an entry to 'skipped_records.txt' with the reason code 'CUST_SUSPENDED'."

## 3. User Interaction Flow
Explain how users interact with the application:
- What can users do?
- What steps do they follow?
- What feedback do they get?
- How does the application respond to their actions?

Describe this like you're explaining how to use the application to a friend.

## 4. Internal Process Flow

### 4.1 Startup Process
Describe what happens when the application starts with SPECIFIC DETAILS:
- What EXACT configuration files does it load? (Include file names and paths)
- What SPECIFIC environment variables or settings does it check?
- What EXACT database connections or external services does it establish?
- What SPECIFIC initialization parameters or default values does it set?
- What EXACT validation checks does it perform during startup?

Example: "When the application starts, it first reads the 'database.properties' file to get the connection string for the PROD_DB database. It then validates that the required directories '/app/logs' and '/app/temp' exist and creates them if missing. It also checks that the environment variable 'APP_MODE' is set to either 'BATCH' or 'ONLINE'."

### 4.2 Main Processing Loop
Explain the main cycle of operations with SPECIFIC DETAILS:
- What EXACTLY does the application do repeatedly? (Include specific operations, file processing, etc.)
- How EXACTLY does it handle multiple tasks? (Include specific queuing, threading, or batching details)
- What are the SPECIFIC conditions that make it stop or pause? (Include exact error conditions, completion criteria)
- What are the EXACT performance metrics or limits it monitors? (Include specific thresholds, counters, timers)

Example: "The application continuously monitors the '/input/pending' directory for new files with the pattern 'TXN_*.csv'. When found, it processes them in batches of 1000 records each. It stops processing when it encounters a file named 'STOP_PROCESSING.flag' or when the error count exceeds 50 failed records."

### 4.3 Data Processing Steps
Break down how the application processes information with SPECIFIC CONTEXTUAL DETAILS:
- How EXACTLY does it receive information? (Include specific input sources, file formats, API endpoints)
- What are the SPECIFIC steps it follows to work with the data? (Include exact transformations, validations, calculations)
- How EXACTLY does it transform or change the information? (Include specific conversion rules, formulas, mappings)
- What EXACTLY does it produce as output? (Include specific output formats, file names, destinations)

Example: "The application reads each record from 'customer_updates.xml', extracts the customer_id, account_balance, and last_transaction_date fields. It then validates that account_balance is numeric and greater than -$1000. For valid records, it calculates the interest earned using the formula: balance * 0.035 / 365 * days_since_last_transaction. Finally, it writes the results to 'interest_calculations_YYYYMMDD.csv' with columns: customer_id, old_balance, interest_earned, new_balance."

## 5. Error Handling Logic
Describe how the application deals with problems with SPECIFIC DETAILS:
- What are the EXACT kinds of problems that might occur? (Include specific error types, conditions, exception names)
- How EXACTLY does it detect these problems? (Include specific validation checks, monitoring mechanisms)
- What EXACTLY does it do when something goes wrong? (Include specific error handling actions, retry logic, fallback procedures)
- How EXACTLY does it recover or continue working? (Include specific recovery procedures, restart mechanisms)
- What are the SPECIFIC error messages, log entries, or notifications it generates?
- What are the EXACT error codes or status values it uses?

Example: "If the application cannot connect to the database after 3 attempts, it writes the error 'DB_CONNECTION_FAILED' to 'application.log' and switches to reading from the backup file 'customer_data_backup.csv'. If a record has an invalid customer_id format (not 8 digits), it logs the error 'INVALID_CUSTOMER_ID' and moves the record to 'rejected_records.txt' with the original data plus an error description."

## 6. Component Interactions
Explain how different parts of the application work together with SPECIFIC DETAILS:
- What are the EXACT main parts or modules? (Include specific class names, module names, service names)
- How EXACTLY do they communicate with each other? (Include specific method calls, message formats, API calls)
- What SPECIFIC information do they share? (Include exact data structures, parameter names, message contents)
- How EXACTLY do they coordinate their work? (Include specific synchronization mechanisms, workflow orchestration)
- What are the SPECIFIC interfaces, APIs, or protocols used for communication?

Example: "The 'DataReader' module calls the 'ValidationService.validateRecord()' method, passing a CustomerRecord object containing customer_id, name, and account_balance. The ValidationService returns a ValidationResult object with fields: isValid (true/false), errorCode (string), and errorMessage (string). If validation passes, DataReader then calls 'DatabaseService.updateCustomer()' with the validated record."

## 7. Security and Validation Logic
Describe how the application keeps things safe and correct with SPECIFIC DETAILS:
- What are the EXACT checks it performs? (Include specific validation rules, field checks, business rule validations)
- How EXACTLY does it verify information is correct? (Include specific validation methods, criteria, thresholds)
- What are the SPECIFIC security measures it uses? (Include authentication methods, authorization checks, encryption details)
- How EXACTLY does it protect sensitive information? (Include specific data protection methods, masking techniques, access controls)
- What are the EXACT security configurations, permissions, or access rules?

Example: "The application validates that social security numbers match the pattern XXX-XX-XXXX using regex validation. It encrypts sensitive data using AES-256 before storing it in 'encrypted_customer_data.db'. All database access requires the user to be in the 'DATA_PROCESSORS' security group, and failed login attempts are logged to 'security_audit.log' after 3 consecutive failures."

## 8. Configuration and Settings
Explain how the application can be customized with SPECIFIC DETAILS:
- What are the EXACT configuration files, parameters, or settings? (Include specific file names, parameter names, default values)
- How EXACTLY does it remember preferences? (Include specific storage mechanisms, configuration persistence)
- What EXACTLY happens with different configurations? (Include specific behavioral changes, feature toggles)
- How EXACTLY does it adapt to different environments? (Include specific environment variables, deployment configurations)
- What are the SPECIFIC configuration validation rules or constraints?

Example: "The application reads settings from 'config/application.yml' including batch_size (default: 1000), max_threads (default: 4), and log_level (default: INFO). In production, it overrides these with environment variables: APP_BATCH_SIZE, APP_MAX_THREADS. If running in 'development' mode (set via APP_ENVIRONMENT variable), it enables debug logging and uses the test database connection string."

## 9. Performance and Efficiency Logic
Describe how the application works efficiently with SPECIFIC DETAILS:
- What EXACTLY does it do to work faster? (Include specific optimization techniques, caching mechanisms, performance improvements)
- How EXACTLY does it handle large amounts of data? (Include specific batching strategies, streaming approaches, memory management)
- What are the SPECIFIC shortcuts or optimizations it uses? (Include actual performance tuning parameters, algorithmic improvements)
- How EXACTLY does it manage resources? (Include specific resource pools, connection management, memory allocation strategies)
- What are the EXACT performance metrics, thresholds, or monitoring points?

Example: "To improve performance, the application processes records in batches of 5000 instead of one-by-one. It maintains a connection pool of 10 database connections (configured in 'db_pool.properties'). When memory usage exceeds 80% (monitored every 30 seconds), it triggers garbage collection and temporarily reduces batch size to 2500 records. It also caches frequently accessed lookup data in a HashMap with a maximum size of 50,000 entries."

## 10. Integration Points
Explain how the application connects with other systems with SPECIFIC DETAILS:
- What are the EXACT external services, APIs, or systems it uses? (Include specific service names, API endpoints, system identifiers)
- How EXACTLY does it communicate with other applications? (Include specific protocols, message formats, authentication methods)
- What SPECIFIC information does it exchange? (Include exact data formats, field mappings, message structures)
- How EXACTLY does it handle communication failures? (Include specific retry logic, fallback mechanisms, error handling procedures)
- What are the SPECIFIC integration configurations, timeouts, or connection parameters?

Example: "The application connects to the PaymentService API at 'https://api.payments.company.com/v2/process' using OAuth2 authentication with the client_id 'APP_12345'. It sends transaction data in JSON format including fields: customer_id, amount, currency_code, and transaction_type. If the API call fails, it retries up to 3 times with exponential backoff (2, 4, 8 seconds), then writes failed transactions to 'failed_payments.queue' for manual processing."

## Summary

### What This File Contains
Provide a comprehensive summary with SPECIFIC DETAILS from the code:

**Main Purpose**: [Describe the primary function using EXACT business processes, file names, or operations mentioned in the code]

**Core Components Explained**:
- [List each major component with SPECIFIC names, classes, or modules from the code]
- [Explain what each component does using ACTUAL functionality and specific operations]
- [Describe how components work together using EXACT method calls, data exchanges, or communication patterns]

**Key Processes Documented**:
- [List the main processes using SPECIFIC workflow names, function names, or operation sequences from the code]
- [Describe the most important operations using ACTUAL processing steps, calculations, or transformations]
- [Highlight critical decision points using EXACT conditions, thresholds, or business rules from the code]

**Data Handling Summary**:
- [Describe SPECIFIC data types, file formats, database tables, or data structures processed]
- [Explain the main data transformations using ACTUAL conversion rules, calculations, or mappings]
- [Summarize storage and retrieval operations using EXACT file names, database operations, or persistence mechanisms]

**User Interaction Summary**:
- [Describe how users interact using SPECIFIC interfaces, input methods, or interaction patterns from the code]
- [List the main user scenarios using ACTUAL use cases, workflows, or business processes]
- [Explain the user experience flow using EXACT steps, validations, or feedback mechanisms]

**Technical Concepts Simplified**:
- [List complex technical concepts using SPECIFIC algorithms, patterns, or technical approaches from the code]
- [Describe how they were broken down using ACTUAL implementations, configurations, or technical details]
- [Highlight the most important technical decisions using EXACT architectural choices, design patterns, or technical solutions]

**Integration and Dependencies**:
- [Describe connections using SPECIFIC system names, API endpoints, or external services from the code]
- [Explain external dependencies using ACTUAL library names, service dependencies, or system requirements]
- [Summarize how this code fits using EXACT relationships, data flows, or system interactions]

**Configuration and Environment Details**:
- [List SPECIFIC configuration files, environment variables, or settings used]
- [Describe EXACT deployment requirements, runtime parameters, or environmental dependencies]
- [Explain ACTUAL customization options, feature flags, or operational parameters]

**This documentation has provided a complete plain-English explanation of the application logic with specific contextual details extracted directly from the code. Each section includes actual file names, specific parameter values, exact business rules, and precise technical implementations found in the codebase, making it possible for readers to understand not just what the application does, but exactly how it does it with all the specific details needed for practical understanding and maintenance.**

Remember: Use conversational language throughout. Avoid technical jargon. Explain complex concepts using analogies and real-world examples. Write as if explaining to someone who is intelligent but not familiar with programming.

{code_content}
"""
--------------------------------------------------------------------------------------------------------------------------------------------
## JCL (Job Control Language)
if prog_type == JCL_TYPE:
    base_prompt += """
    # JCL Documentation: {filename}
    
    ## 1. Job Execution Overview
    Provide a comprehensive overview of this JCL. Explain its primary purpose in the system, when it's typically executed (scheduled, event-driven, etc.), and its business significance. Describe the overall workflow from initialization to completion and any prerequisites for execution.
    
    ## 2. Job Step Analysis
    Analyze each job step in sequence with the following details:
        - Step name and executed program/utility
        - Purpose and function of each step
        - Input and output datasets with their business purpose
        - Parameter specifications and their meaning
        - Expected condition codes and their implications
        - Dependencies between steps and workflow control mechanisms
    
    ## 3. Dataset Usage & Data Flow
    Document all datasets referenced in this JCL:
        - Input datasets: origin, content purpose, and validation requirements
        - Output datasets: destination, content produced, and business significance
        - Temporary datasets: purpose and lifespan within the job
        - Generation Data Groups (GDGs): versioning strategy and retention policies
        - VSAM files: access methods and business function
    
    ## 4. Execution Parameters & JCL Logic
    Explain all conditional processing:
        - JOB statement parameters and their operational significance
        - COND parameters and their decision logic
        - IF/THEN/ELSE constructs and their business rules
        - INCLUDE statements and their purpose
        - JCL symbols and their usage
    
    ## 5. Error Handling & Recovery
    Detail the error handling mechanisms:
        - Expected condition codes for normal and abnormal termination
        - Restart procedures and checkpoint mechanisms
        - Error notification processes (messages, alerts)
        - Recovery procedures and alternative execution paths
        - Escalation workflows for critical failures
    
    ## 6. Integration Points
    Document how this JCL interacts with other components:
        - Upstream dependencies (jobs that must complete before this one)
        - Downstream jobs triggered by this JCL
        - Interfaces with other systems or applications
        - Data exchange protocols and formats
    
    ## 7. Operational Considerations
    Provide guidance for operations personnel:
        - Execution frequency and typical runtime
        - Resource requirements (CPU, memory, disk space)
        - Scheduling dependencies and optimal execution windows
        - Job monitoring checkpoints and verification procedures
        - Common operational issues and their resolution
    
    Format your response with appropriate headings and subheadings, providing thorough analysis while maintaining clarity.
    """
```

## PROC/CLIST

```python
elif prog_type == PROC_TYPE or prog_type == CLIST_TYPE:
    base_prompt += """
    # Procedure/CLIST Documentation: {filename}
    
    ## 1. Purpose & Function Overview
    Provide a comprehensive explanation of this procedure's business purpose and technical function. Describe when and why it's invoked, what business process it supports, and its role in the larger system architecture.
    
    ## 2. Parameter Analysis
    Document all input parameters in detail:
        - Parameter name and syntax
        - Purpose and business significance
        - Default values and override mechanisms
        - Valid value ranges and constraints
        - Impact of different parameter values on execution path
    
    ## 3. Environment Configuration
    Explain the environmental setup performed:
        - System variables defined or modified
        - Dataset allocations and their purpose
        - Security and authorization settings
        - Regional or environment-specific configurations
        - Required prerequisites and preconditions
    
    ## 4. Execution Workflow
    Detail the step-by-step execution sequence:
        - Programs or utilities called and their purpose
        - Order of operations and processing dependencies
        - Decision points and conditional execution paths
        - Looping or iterative processing structures
        - Task delegation and subprocedure calls
    
    ## 5. Logical Implementation
    Analyze the business logic and technical implementation:
        - Key algorithms and processing methods
        - Business rules and validation checks
        - Data transformation and processing techniques
        - Calculated values and their business meaning
        - Exception handling and error recovery logic
    
    ## 6. Integration Context
    Document how this procedure interacts with other components:
        - Calling patterns and invocation methods
        - Return codes and their interpretation
        - Data passing mechanisms (parameters, variables, files)
        - Dependencies on other procedures or programs
        - Services provided to other system components
    
    ## 7. Operational Considerations
    Provide guidance for implementation and maintenance:
        - Performance characteristics and resource utilization
        - Reusability aspects and potential for customization
        - Known limitations or constraints
        - Common troubleshooting scenarios and solutions
        - Maintenance history and evolution
    
    Format your response with appropriate headings and subheadings, providing thorough analysis while maintaining clarity.
    """
```

## COBOL Programs

```python
elif prog_type == COBOL_TYPE:
    base_prompt += """
    # COBOL Program Documentation: {filename}
    
    ## 1. Business Purpose Overview
    Provide a comprehensive explanation of this program's business function. Describe the business process it supports, its role in the larger system, and the business value it delivers. Include any business rules or policies it implements.
    
    ## 2. Program Architecture
    Document the high-level structure of the program:
        - Program organization (sections, paragraphs, modules)
        - Control flow and processing sequence
        - Key subroutines and their business functions
        - Linkage with other programs or components
        - Reusable components and shared functionality
    
    ## 3. Data Structures & File Handling
    Analyze all data structures and file operations:
        - Input files: format, record layout, and business purpose
        - Output files: format, record layout, and business meaning
        - Working storage structures and their business significance
        - Database or VSAM operations and table relationships
        - Data validation rules and constraints
    
    ## 4. Business Logic Implementation
    Detail the core business logic:
        - Business rules and their implementation
        - Calculation methods and formulas with business context
        - Decision processes and conditional logic
        - Validation and verification procedures
        - Workflow control and processing sequence
    
    ## 5. Error Handling & Exception Management
    Explain the error handling mechanisms:
        - Error conditions detected and their business impact
        - Error reporting and notification procedures
        - Recovery mechanisms and alternate processing paths
        - Return codes and their business interpretation
        - Exception logs and audit trails
    
    ## 6. Processing Workflow
    Document the step-by-step processing workflow:
        - Initialization and setup procedures
        - Main processing loops and iterations
        - Transaction processing or batch processing logic
        - End-of-job procedures and cleanup operations
        - Integration points with other system components
    
    ## 7. Performance & Technical Considerations
    Provide insights on technical implementation details:
        - Optimization techniques and performance enhancements
        - Resource utilization patterns (memory, file I/O)
        - Processing volume considerations and scaling factors
        - Technical constraints and limitations
        - Common technical issues and their resolution
    
    Format your response with appropriate headings and subheadings, providing thorough analysis while maintaining clarity.
    """
```

## Assembler Programs

```python
elif prog_type == ASSEMBLER_TYPE:
    base_prompt += """
    # Assembler Program Documentation: {filename}
    
    ## 1. Program Purpose & Context
    Provide a comprehensive explanation of this assembler program's purpose. Describe its role in the system architecture, the technical services it provides, and why assembler was chosen for this functionality.
    
    ## 2. Program Structure
    Document the overall structure of the program:
        - Program entry points and initialization sequence
        - Main processing sections and their functions
        - Subroutines and their technical purposes
        - Program termination and cleanup procedures
        - Code organization and modular design
    
    ## 3. Register Usage & Parameter Handling
    Analyze the register utilization strategy:
        - Register assignment and usage patterns
        - Parameter passing mechanisms and conventions
        - Register saving and restoration procedures
        - Base register management and addressing techniques
        - Register interdependencies and preservation requirements
    
    ## 4. Memory & Storage Management
    Detail memory and storage operations:
        - Dynamic storage allocation and deallocation
        - Storage addressing modes and techniques
        - Data areas and their organization
        - Buffer management and shared memory usage
        - Storage protection mechanisms
    
    ## 5. I/O Operations
    Explain all input/output operations:
        - I/O methods used (BSAM, QSAM, VSAM, etc.)
        - Device interaction and access methods
        - Buffer management and data transfer techniques
        - I/O error detection and recovery procedures
        - Performance optimization for I/O operations
    
    ## 6. System Services & Macros
    Document system service usage:
        - System macros utilized and their purposes
        - Supervisor calls (SVCs) and their functions
        - Operating system interfaces and dependencies
        - System resource usage (ENQ/DEQ, etc.)
        - z/OS services utilized and their implementation
    
    ## 7. Technical Processing Logic
    Analyze the core technical processing:
        - Algorithms and processing methods
        - Bit manipulation and binary operations
        - Mathematical or computational techniques
        - Data transformation and conversion procedures
        - Optimization methods and performance considerations
    
    ## 8. Error Handling & Return Codes
    Detail error handling mechanisms:
        - Error detection techniques
        - Return code generation and interpretation
        - Error recovery procedures
        - Abend prevention strategies
        - Diagnostic information provided
    
    Format your response with appropriate headings and subheadings, providing thorough analysis while maintaining clarity.
    """
```

## Copybooks

```python
elif prog_type == COPYBOOK_TYPE:
    base_prompt += """
    # Copybook Documentation: {filename}
    
    ## 1. Data Structure Overview
    Provide a comprehensive explanation of this copybook's purpose and the business entities it represents. Describe how it's used across the system and its significance in the data architecture.
    
    ## 2. Field Definitions & Business Meaning
    Document each field with detailed information:
        - Field name and technical characteristics (type, length, format)
        - Business meaning and significance
        - Valid values and their business interpretations
        - Default values and initialization requirements
        - Dependencies or relationships with other fields
    
    ## 3. Structural Analysis
    Analyze the structure's organization:
        - Hierarchical relationships between fields
        - Group items and their business purpose
        - Redefines and their alternative interpretations
        - Repeating structures and their business context
        - Alignment and padding considerations
    
    ## 4. Data Validation & Constraints
    Detail all business rules and technical constraints:
        - Value range limitations and their business justification
        - Field interdependencies and conditional requirements
        - Format restrictions and standardization rules
        - Data integrity rules and validation requirements
        - Cross-field validation rules
    
    ## 5. Usage Context
    Document how this copybook is utilized:
        - Programs or systems that incorporate this copybook
        - Usage patterns (input, output, working storage)
        - Interface specifications for external systems
        - Version management and compatibility considerations
        - Reusability aspects across the system
    
    ## 6. Data Transformation Considerations
    Explain any data transformation aspects:
        - Format conversions for different environments
        - API mapping considerations
        - Database mapping correlations
        - Integration mapping requirements
        - Internationalization or localization aspects
    
    ## 7. Historical Context & Evolution
    Provide insights on the copybook's development:
        - Origin and design rationale
        - Major revisions and their business drivers
        - Deprecated fields and backward compatibility
        - Planned extensions or modifications
        - Migration considerations
    
    Format your response with appropriate headings and subheadings, providing thorough analysis while maintaining clarity.
    """
```
