def create_pseudocode_prompt(problem_description, context=None):
    """Create a prompt for generating comprehensive, detailed pseudo-code"""
    
    context_section = f"\n## Implementation Context\n{context}\n" if context else ""
    
    return f"""Generate detailed, comprehensive pseudo-code for the following problem that provides a thorough implementation blueprint with precise algorithm steps. Use structured pseudo-code with proper indentation, clear naming conventions, and explicit control flow. Focus on algorithmic logic, data structures, processing steps, and edge case handling:

# Pseudo-Code Implementation: {problem_description}

{context_section}

## 1. Algorithm Overview
Provide a comprehensive overview of the algorithm design. Describe the overall approach, computational strategy, and key techniques used to solve the problem. Include asymptotic complexity analysis (time and space) and justify your algorithmic choices.

## 2. Data Structures & Variables

### 2.1 Primary Data Structures
Define all data structures with explicit type annotations and initialization values:
```
// Example:
structure UserProfile:
    id: Integer
    name: String
    email: String
    preferences: Dictionary<String, Object>
    lastLogin: DateTime
```

### 2.2 Helper Data Structures
Define any auxiliary data structures needed for intermediate processing or optimization:
```
// Example: 
structure CacheEntry:
    key: String
    value: Object
    timestamp: DateTime
    expiryTime: Integer
```

### 2.3 Global Variables & Constants
Declare all global variables, constants, and configuration parameters with their types and purposes:
```
// Example:
constant MAX_RETRY_ATTEMPTS = 3
constant DEFAULT_TIMEOUT_MS = 5000
variable currentUserSessions: Dictionary<String, UserSession>
```

## 3. Core Algorithm Implementation

### 3.1 Main Function
Provide the primary function or procedure with detailed parameter and return type specifications:
```
function processRequest(request: Request) -> Response:
    // Implementation steps...
```

### 3.2 Initialization Logic
Detail the initialization sequence with precise setup steps:
```
procedure initialize():
    // Step-by-step initialization logic...
```

### 3.3 Core Processing Steps
Break down the main algorithm into explicitly defined steps with detailed processing logic:
```
procedure processData(data: Array<DataPoint>):
    // Step 1: Data validation
    // Step 2: Transformation
    // Step 3: Computation
    // etc.
```

## 4. Helper Functions & Procedures

### 4.1 Utility Functions
Define all helper functions with their exact signatures and detailed implementations:
```
function calculateMetric(values: Array<Float>, weights: Array<Float>) -> Float:
    // Detailed implementation steps...
```

### 4.2 Transformation Methods
Specify data transformation functions with explicit input/output formats:
```
function transformInput(rawData: String) -> ParsedData:
    // Detailed transformation steps...
```

### 4.3 Validation Procedures
Detail all validation logic with specific conditions and error handling:
```
function validateInput(input: UserInput) -> ValidationResult:
    // Exhaustive validation steps...
```

## 5. Control Flow & Logic

### 5.1 Decision Trees
Provide detailed conditional logic with all branches explicitly defined:
```
if condition1 then
    // Detailed steps for condition1
else if condition2 then
    // Detailed steps for condition2
else
    // Default case handling
endif
```

### 5.2 Iteration Logic
Define all loops with initialization, termination conditions, and iteration steps:
```
for each item in collection from start to end do
    // Detailed processing for each iteration
endfor
```

### 5.3 Recursion Patterns
Detail recursive function implementations with base cases and recursive steps:
```
function recursiveProcess(data: Data, depth: Integer) -> Result:
    // Base case handling
    // Recursive step implementation
```

## 6. Error Handling & Edge Cases

### 6.1 Exception Handling
Define comprehensive error detection and handling for all anticipated failure modes:
```
try
    // Operation that might fail
catch ExceptionType1 then
    // Specific handling for ExceptionType1
catch ExceptionType2 then
    // Specific handling for ExceptionType2
finally
    // Cleanup operations
endtry
```

### 6.2 Edge Case Processing
Address all boundary conditions and special cases with dedicated handling logic:
```
// Handle empty input case
if collection.isEmpty() then
    return EmptyResult
endif

// Handle extreme values
if value > UPPER_THRESHOLD then
    // Upper bound handling
endif
```

### 6.3 Resource Management
Specify explicit resource acquisition and release steps:
```
// Resource acquisition
resource = acquireResource()

try
    // Use resource
finally
    // Guaranteed release of resource
    releaseResource(resource)
endtry
```

## 7. Asynchronous & Parallel Processing

### 7.1 Concurrent Operations
Detail any parallel processing logic with synchronization mechanisms:
```
parallel for each chunk in dataChunks do
    // Process each chunk independently
endparallel

// Synchronization point
waitForAllThreadsToComplete()
```

### 7.2 Asynchronous Handling
Specify asynchronous operations with callback or promise/future patterns:
```
function asyncOperation() -> Promise:
    // Initiate async operation
    promise = createPromise()
    
    // Separate execution thread/context
    in background:
        // Async processing steps
        result = performOperation()
        promise.resolve(result)
    
    return promise
```

## 8. External Interactions

### 8.1 I/O Operations
Define all input/output operations with specific formats and error handling:
```
procedure writeToDatabase(data: RecordSet):
    // Connect to database
    // Prepare statement
    // Execute operation
    // Handle potential errors
    // Close connection
```

### 8.2 API Interactions
Detail communications with external systems or services:
```
function callExternalAPI(endpoint: String, payload: Object) -> APIResponse:
    // Prepare request
    // Set headers and authentication
    // Send request with timeout handling
    // Process response
    // Handle error conditions
```

## 9. Performance Optimization

### 9.1 Caching Strategies
Specify any caching mechanisms with explicit invalidation logic:
```
function getCachedValue(key: String) -> Object:
    // Check if cache contains key and entry is valid
    if cache.contains(key) and not cache.isExpired(key) then
        return cache.get(key)
    endif
    
    // Cache miss handling
    value = computeExpensiveValue(key)
    cache.store(key, value, expiryTime)
    return value
```

### 9.2 Computation Optimizations
Detail any algorithmic optimizations or shortcuts:
```
// Optimization for special case
if isSpecialCase(input) then
    return optimizedComputation(input)
endif

// General case handling
return standardComputation(input)
```

## 10. Detailed Execution Example

### 10.1 Sample Input
Provide concrete example input values:
```
Example Input:
data = [1, 5, 3, 9, 2]
parameters = {"threshold": 4, "mode": "filter"}
```

### 10.2 Step-by-Step Execution Trace
Trace the algorithm execution with this input, showing the state after each significant step:
```
1. Initial state: data = [1, 5, 3, 9, 2], result = []
2. After validation: Valid input confirmed
3. Processing element 1: Below threshold, not added to result
4. Processing element 5: Above threshold, result = [5]
...etc.
```

### 10.3 Final Output
Show the expected output from the sample input:
```
Final output: [5, 9]
```

Please provide comprehensive, step-by-step pseudo-code with explicit variable declarations, clear control flow, and detailed processing logic. The pseudo-code should be precise enough that it could be directly translated to actual code in any programming language with minimal interpretation required. Include comments explaining complex logic or non-obvious decisions.
"""
