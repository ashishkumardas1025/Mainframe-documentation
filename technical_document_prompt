def create_technical_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive technical documentation"""
    return f"""Generate detailed, developer-focused technical documentation for the following code that provides a thorough explanation of its implementation details. Use complete paragraphs with precise technical explanations rather than bullet points. Focus on implementation details, code structure, algorithms, and technical architecture:

# Technical Documentation: {filename}

## 1. Code Architecture Overview
Provide a comprehensive technical overview of the code architecture. Describe the technical design patterns used, module organization, and how different components interact. Include a high-level technical diagram described in text if appropriate.

## 2. Technical Implementation Details

### 2.1 Data Structures & Storage
Document all data structures (classes, objects, arrays, etc.) used in the implementation. Explain their purpose, properties, relationships, and implementation details. Include memory considerations and performance characteristics where relevant.

### 2.2 Algorithms & Methods
Detail the core algorithms and methods implemented in the code. Provide line-by-line explanations of complex algorithms, including time and space complexity analysis. Explain the technical reasoning behind algorithmic choices and optimizations.

### 2.3 Technical Validation & Constraints
Document all technical validation mechanisms, including input sanitization, type checking, and boundary validations. Explain the implementation details of each validation method and its technical purpose.

## 3. Code Flow & Execution

### 3.1 Initialization & Bootstrapping
Explain the technical details of how the application initializes, including configuration loading, dependency injection, environment setup, and any bootstrapping processes.

### 3.2 Execution Pathways
Document all execution paths through the code with detailed technical explanations. Include thread management, asynchronous operations, event loops, and callback mechanisms if applicable.

### 3.3 Technical Subsystems
For each technical subsystem, provide detailed implementation explanations including initialization, operational flow, and termination procedures. Include technical interfaces, input/output specifications, and internal data transformations.

## 4. Data Processing Implementation

### 4.1 Data Ingestion & Parsing
Explain the technical implementation of data ingestion processes. Include details about parsing algorithms, tokenization, deserialization, and stream processing where applicable.

### 4.2 Data Transformation Implementation
Document all data transformation implementations with precise technical details. Include transformation algorithms, lookup tables, conversion methods, and optimization techniques.

### 4.3 Persistence & Storage Mechanisms
Detail how data is persisted throughout the system. Include database interactions, file I/O operations, caching mechanisms, and serialization techniques with their technical implementation details.

## 5. Technical Components & Libraries

### 5.1 Core Technical Components
For each core technical component, provide detailed explanations of its implementation, memory management, thread safety considerations, and performance characteristics. Include examples of internal method calls and data flows.

### 5.2 External Dependencies & APIs
Document all external dependencies and API integrations with their technical details. Include version requirements, authentication mechanisms, request/response formats, and error handling implementations.

## 6. System Integration Implementation

### 6.1 Interface Specifications
Document the technical specifications of all interfaces, including HTTP endpoints, RPC methods, message queues, and event subscriptions. Include request/response formats, authentication mechanisms, and rate limiting implementations.

### 6.2 Service Communication
Detail the technical implementation of inter-service communication. Include protocol details, serialization formats, connection pooling, retry mechanisms, and circuit breakers if applicable.

## 7. Error Handling Implementation

### 7.1 Exception Handling
Document the exception handling implementation throughout the codebase. Detail catch blocks, error propagation mechanisms, custom exception classes, and recovery strategies.

### 7.2 Logging & Monitoring Implementation
Explain the technical implementation of logging, monitoring, and observability features. Include log level management, structured logging formats, metric collection, and trace propagation.

## 8. Configuration & Environment

### 8.1 Configuration Management
Document the technical implementation of configuration management. Include details about configuration sources, override mechanisms, hot reloading, and environment-specific configurations.

### 8.2 Environment Variables & Secrets
Detail the technical handling of environment variables and secrets. Include encryption methods, secure storage, rotation mechanisms, and access control implementations.

## 9. Performance Considerations

### 9.1 Optimization Techniques
Document all performance optimization techniques implemented in the code. Include caching strategies, lazy loading, connection pooling, and computational optimizations with technical details.

### 9.2 Scalability Mechanisms
Explain the technical implementation of scalability features. Include details about statelessness, sharding, partitioning, and load distribution mechanisms.

## 10. Security Implementation

### 10.1 Authentication & Authorization
Document the technical implementation of authentication and authorization mechanisms. Include cryptographic methods, token handling, permission evaluation, and session management details.

### 10.2 Data Protection
Explain the technical implementation of data protection features. Include encryption algorithms, key management, data masking, and secure transmission protocols.

## 11. Testing & Quality Assurance

### 11.1 Unit & Integration Tests
Document the technical implementation of testing frameworks and methodologies. Include test coverage analysis, mocking strategies, test data generation, and CI/CD integration.

### 11.2 Code Quality Tools
Detail static analysis tools, linting configurations, code quality metrics, and automated review processes used in the codebase.

Please provide comprehensive, line-by-line technical explanations that would enable another developer to fully understand and recreate the implementation. Include code snippets with explanatory comments where appropriate. Focus on technical 'how' rather than business 'why' throughout the documentation.

{code_content}
"""
