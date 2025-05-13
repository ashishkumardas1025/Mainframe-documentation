def create_workflow_documentation_prompt(code_content, filename):
    """Create a prompt for generating comprehensive workflow documentation"""
    return f"""Generate detailed, narrative-style workflow documentation for the following code that thoroughly explains its process flows and operational sequences. Use complete paragraphs with step-by-step explanations rather than bullet points. Focus on process flows, decision points, and operational sequences:

# Workflow Documentation: {filename}

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

{code_content}
"""
"""
