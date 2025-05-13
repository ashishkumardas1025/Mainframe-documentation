# Enhanced Mainframe Documentation Prompts

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
