def create_functional_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive functional documentation"""
    return f"""Generate comprehensive, narrative-style functional documentation for the following code that thoroughly explains its business purpose and functionality. Use complete paragraphs and detailed explanations rather than bullet points. Focus on business rules, user requirements, and functional capabilities:

# Functional Documentation: {filename}

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

{code_content}
"""
