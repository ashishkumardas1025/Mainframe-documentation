def create_master_documentation_generator(content, filename):
    """Create a complete documentation generation function that combines all documentation types"""
    return f"""
# Master Documentation Generator

def generate_comprehensive_documentation(code_content, filename, doc_type="all"):
    """
    Generate comprehensive documentation for the given code content
    
    Parameters:
    - code_content: The source code to document
    - filename: Name of the source file
    - doc_type: Type of documentation to generate ("technical", "functional", "workflow", or "all")
    
    Returns:
    - A dictionary containing the requested documentation types
    """
    documentation = {{}}
    
    if doc_type in ["technical", "all"]:
        documentation["technical"] = create_technical_documentation_prompt(code_content, filename)
    
    if doc_type in ["functional", "all"]:
        documentation["functional"] = create_functional_documentation_prompt(code_content, filename)
    
    if doc_type in ["workflow", "all"]:
        documentation["workflow"] = create_workflow_documentation_prompt(code_content, filename)
    
    return documentation


def create_technical_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive technical documentation"""
    return f'''Generate detailed, developer-focused technical documentation for the following code that provides a thorough explanation of its implementation details. Use complete paragraphs with precise technical explanations rather than bullet points. Focus on implementation details, code structure, algorithms, and technical architecture:

# Technical Documentation: {{filename}}

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

{{code_content}}
'''

def create_functional_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive functional documentation"""
    return f'''Generate comprehensive, narrative-style functional documentation for the following code that thoroughly explains its business purpose and functionality. Use complete paragraphs and detailed explanations rather than bullet points. Focus on business rules, user requirements, and functional capabilities:

# Functional Documentation: {{filename}}

## 1. Business Purpose Overview
Provide a thorough introduction that explains the core business purpose of this code. Describe what business problem it solves and its role in the larger system. Explain the key business capabilities it provides and any assumptions or prerequisites for its operation. Include the business value delivered and stakeholder benefits.

## 2. Functional Requirements

### 2.1 Primary Business Capabilities
Document all primary business capabilities the system provides to users and other systems. Explain each capability's purpose, business value, and expected outcomes. Describe the business processes supported by each capability.

### 2.2 Business Rules & Policies
Provide a detailed explanation of all business rules and policies implemented in the system. Describe the business context, regulatory requirements, and organizational policies that dictate these rules. Explain the reasoning behind each rule and its impact on system behavior.

### 2.3 Business Data Model
Document the business entities represented in the system and their relationships. Describe the attributes of each entity from a business perspective, explaining their significance, valid values, and business constraints. Include business-level entity relationship diagrams described in text if appropriate.

## 3. User Interactions & Workflows

### 3.1 User Roles & Permissions
Describe all user roles that interact with the system. Explain each role's responsibilities, permissions, and limitations within the system. Include the business justification for access controls and separation of duties.

### 3.2 User Workflows
Document each major workflow from a user perspective. Walk through the steps users take to accomplish business tasks, explaining the business decisions made at each point. Include business conditions, exceptions, and alternate paths that may be encountered.

### 3.3 User Interface Requirements
Explain the functional requirements for user interfaces. Describe the business information that must be displayed, input requirements, and user experience considerations. Include accessibility requirements and business justifications.

## 4. Business Data Processing

### 4.1 Data Input Requirements
Document the business requirements for data inputs. Explain the business context of each input field, its purpose, validation requirements, and acceptable formats. Include the business impact of valid and invalid inputs.

### 4.2 Business Calculations & Transformations
Provide detailed explanations of all business calculations and data transformations. Break down complex formulas, explain the business logic behind each calculation step, and describe how the results are used in business processes.

### 4.3 Business Output Requirements
Explain the business requirements for system outputs. Describe the purpose of each output, its audience, required format, and business significance. Detail how outputs support business decision-making and operations.

## 5. Business Process Flows

### 5.1 End-to-End Business Processes
Document the end-to-end business processes supported by the system. Explain how business activities flow from initiation to completion, including decision points, approval steps, and handoffs between different business units or systems.

### 5.2 Business Events & Triggers
Describe the business events that trigger system actions. Explain the business context of each event, its significance, and the expected system responses. Include timing considerations and business impact of processing delays.

### 5.3 Business States & Transitions
Document the business states that entities can have within the system. Explain what each state represents from a business perspective, the conditions for state transitions, and the business implications of state changes.

## 6. Integration Requirements

### 6.1 Upstream Systems & Data Sources
Document the business requirements for integration with upstream systems and data sources. Explain what business data is received, its purpose, timing requirements, and business dependencies.

### 6.2 Downstream Systems & Consumers
Describe the business requirements for integration with downstream systems and data consumers. Explain what business data is provided, when it's needed, and how it's used by receiving systems to support business operations.

## 7. Business Rules for Exception Handling

### 7.1 Business Validation Rules
Document the business validation rules applied to data and processes. Explain the business reasoning behind each validation and the appropriate business response to validation failures.

### 7.2 Business Exception Handling
Describe how business exceptions should be handled. Explain the business impact of different types of exceptions, appropriate business responses, notification requirements, and escalation procedures.

## 8. Business Configuration Options

### 8.1 Configurable Business Parameters
Document all business parameters that can be configured. Explain the business purpose of each parameter, its impact on system behavior, and the business considerations for different configuration options.

### 8.2 Business Customization Points
Describe the aspects of the system that can be customized for different business scenarios. Explain the business justification for customization options and the implications of different configurations.

## 9. Business Scenarios & Examples

### 9.1 Common Business Use Cases
Provide detailed examples of typical business scenarios. Walk through each scenario step by step, explaining the business context, user actions, system responses, and business outcomes. Include realistic business data examples.

### 9.2 Edge Business Cases
Document unusual or complex business scenarios the system must handle. Explain the business conditions that lead to these cases, their importance, and the expected system behavior in each situation.

## 10. Business Compliance & Reporting

### 10.1 Regulatory Compliance Requirements
Explain the regulatory and compliance requirements the system fulfills. Describe the specific regulations, the business processes affected, and how the system ensures compliance.

### 10.2 Business Reporting Requirements
Document the business reporting requirements. Explain what business information must be tracked, aggregated, and reported, including the business purpose of each report and its audience.

Please provide comprehensive, business-focused explanations that would help business analysts, product managers, and end users understand the system's functionality without requiring technical knowledge. Use domain-specific business terminology appropriate to the application area. Focus on business 'why' rather than technical 'how' throughout the documentation.

{{code_content}}
'''

def create_workflow_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive workflow documentation"""
    return f'''Generate detailed, narrative-style workflow documentation for the following code that thoroughly explains its process flows and operational sequences. Use complete paragraphs with step-by-step explanations rather than bullet points. Focus on process flows, decision points, and operational sequences:

# Workflow Documentation: {{filename}}

## 1. Process Overview
Provide a comprehensive introduction that explains the end-to-end workflow this code implements. Describe the overall process from initiation to completion, identifying key stages, participants, and outcomes. Include a high-level process diagram described in text if appropriate.

## 2. Workflow Trigger Points

### 2.1 Initiation Events
Document all events that can trigger this workflow. For each trigger, explain when and how it occurs, what data or conditions are required, and which actors (human or system) are involved in initiation. Include timing patterns, frequencies, and dependencies.

### 2.2 Prerequisite Conditions
Detail all conditions that must be satisfied before the workflow can begin. Explain how these conditions are verified, what happens if they're not met, and how prerequisite issues are resolved or escalated.

## 3. Process Participants

### 3.1 Human Actors
Identify all human participants in the workflow. For each role, describe their responsibilities, actions they must take, decisions they must make, and information they need at each workflow stage.

### 3.2 System Actors
Document all systems, services, and automated agents participating in the workflow. Explain when each system is engaged, what actions it performs, what data it provides or consumes, and how it interacts with other participants.

## 4. Core Process Sequence

### 4.1 Main Path Execution
Describe the main workflow sequence step-by-step, walking through each activity in exact order of execution. For each step, explain what occurs, which actor is responsible, expected inputs and outputs, and transition conditions to the next step.

### 4.2 Decision Points & Branches
Detail all decision points in the workflow where the process may branch into different paths. For each decision point, explain what criteria are evaluated, who makes the decision, what options are available, and the sequence that follows each possible choice.

### 4.3 Processing States
Document the various states that work items or entities pass through during the workflow. Explain what each state represents in the process, how long items typically remain in each state, and what conditions prompt state transitions.

## 5. Subprocess Workflows

### 5.1 Dependent Subprocesses
Identify all subprocesses incorporated within the main workflow. For each subprocess, explain when and how it's initiated, its sequence of steps, how it interacts with the main workflow, and how it returns control to the parent process.

### 5.2 Parallel Processes
Document workflow components that can execute concurrently. Explain which activities can proceed in parallel, how parallel execution is managed, and how synchronization occurs when parallel paths must reconverge.

## 6. Data Flow Throughout Process

### 6.1 Information Inputs & Outputs
For each workflow stage, detail the exact information required as input and produced as output. Explain where input data comes from, how it's validated before processing, how output data is formatted, and where it's directed next.

### 6.2 Data Transformations in Workflow
Document how information is transformed as it moves through the workflow. Describe each transformation in sequence, explaining how data is enriched, calculated, aggregated, or otherwise modified at each step of the process.

## 7. Time Constraints & SLAs

### 7.1 Processing Timeframes
Detail time constraints for each workflow stage and the process as a whole. Specify expected durations, maximum allowed times, and factors that may impact processing speed. Include business hours considerations if applicable.

### 7.2 Deadline Management
Explain how deadlines are tracked throughout the workflow. Describe warning thresholds, notification procedures when deadlines approach, and escalation protocols if deadlines are missed.

## 8. Exception Flows

### 8.1 Error Handling Procedures
Document the complete workflow for handling each type of error that may occur. For each exception scenario, explain detection mechanisms, immediate actions taken, recovery attempts, and alternate paths to resolution.

### 8.2 Retry & Recovery Mechanisms
Detail the workflow for retry attempts and recovery procedures. Explain retry logic, maximum attempt limits, cooling-off periods between attempts, and conditions for abandoning recovery efforts.

### 8.3 Manual Intervention Points
Identify points in the workflow where manual intervention may be required. Explain what conditions trigger the need for human involvement, how work is routed to appropriate personnel, what actions they must take, and how the process resumes afterward.

## 9. Status Tracking & Monitoring

### 9.1 Progress Indicators
Document how progress through the workflow is tracked and measured. Explain what milestones or checkpoints exist, how completion percentage is calculated, and how participants can view current status.

### 9.2 Auditing & Logging Procedures
Detail the workflow's audit trail generation. Describe what events are logged, what information is captured at each step, how the audit history can be accessed, and retention policies for historical workflow data.

## 10. Workflow Completion

### 10.1 Successful Completion Paths
Explain all possible paths to successful workflow completion. For each path, describe the final processing steps, completion criteria, outputs produced, and notifications generated.

### 10.2 Cancellation & Termination Procedures
Document the procedures for premature workflow termination. Explain what conditions may trigger cancellation, who has authority to cancel, what cleanup actions occur, and how resources are released.

## 11. Cross-Process Dependencies

### 11.1 Upstream Dependencies
Identify all dependencies on processes that must complete before this workflow can begin or proceed. Explain the nature of each dependency, how fulfillment is verified, and contingency plans if dependent processes fail.

### 11.2 Downstream Impacts
Document processes that depend on the outputs or completion of this workflow. Explain how downstream processes are notified of completion, what they expect to receive, and how delays or failures are communicated.

## 12. Process Variations

### 12.1 Conditional Pathways
Detail all possible variations in the workflow based on conditions, input types, or business scenarios. For each variation, explain the triggering conditions and how the process sequence differs from the standard path.

### 12.2 Regional or Business Unit Variations
Document any variations in the workflow specific to different regions, departments, or business units. Explain what aspects of the process change, why these variations exist, and how the system determines which variation to apply.

Please provide comprehensive, step-by-step explanations that would allow process participants, workflow analysts, and operations personnel to fully understand the entire process flow. Include realistic examples of how the workflow progresses through different scenarios. Focus on operational sequencing rather than technical implementation details or business justifications.

{{code_content}}
'''

# Example usage:
# 1. Import this module
# 2. Call generate_comprehensive_documentation with your code and filename
# 3. Process the generated prompts with your LLM

# Example:
# documentation = generate_comprehensive_documentation(code_content, "inventory_management.py", "all")
# technical_doc_prompt = documentation["technical"]
# functional_doc_prompt = documentation["functional"]
# workflow_doc_prompt = documentation["workflow"]
"""
