- [Azure Functions](azure_functions.png)
  - serverless application platform: abstract servers
  - run functions(small pieces of code) in cloud
  - FaaS: Function as a Service
  - Choice of programming languages: C#, Java, JavaScript, Python, PowerShell etc.
  - Hosting choices: Service plan on Azure App Service
    - ***Consumption plan***:
      - Serverless pricing
      - bills only when functions are running
      - automatic scaling
      - Time limit for each function invocation: 5 min
    - ***App Service plan***:
      - Traditional pricing model: monthly bills
      - No time limit
    - ***Premium plan***:
      - Faster
      - Secure
      - reserved instances
      - Serverless automatic scaling
    - Run Azure Functions on:
      - Docker Container
        - On-premise or on cloud
      - Locally
  - Development Environment choices: Azure portal, Visual Studio(c#), Azure Functions Core Tools(CLI, VS code)
- Implement Azure Functions:
  - Implement function triggers by using data operations, timers and webhooks
  - Implement input and output bindings for a function
  - Implement Azure Durable Functions
- Create Azure function in Azure portal app
  - Create a resource -> function app -> deploy function app
  - Open deployment -> Go to functions  -> create
- Azure function triggers(Triggers are what causes the function to run)
  - HTTP request Trigger(webhooks): runs in response to a web request. - use for APIs and webhooks
    - trigger based on HTTP methods - e.g. GET, POST
    - trigger based on Route/URL
    - secured via authorization key
      - Anonymous: no key required
      - Function: key per function
      - Admin: key per function app
    - Create HTTP function trigger
      - open function app -> create function
      - [see create_functions.sh file for further detail.](create_functions.sh)
  - Timer Trigger(scheduled tasks): create scheduled tasks(e.g. at 12 am every night)
    - run scheduled tasks in the cloud.
    - using CRON expression
      - To run trigger function every 5 mins:
        - 0 */5 * * * *
  - Queue Trigger - run in response to a message on a queue
  - Cosmos DB Trigger - run when a document is created or updated in cosmos db storage
  - Blob Storage Trigger(data operation) - run when a new file is uploaded to blob storage.
  - Other triggers:
    - Event grid
    - Microsoft Graph
- Implementing Input and Output Bindings
  - Binding(helps to declaratively connect resources for both Input and Output).
    - collection of data within the function
    - A function can have multiple I/O bindings.
  - Input Bindings
    - get data into functions
    - read-access to data from external service to our function
    - e.g. 
      - Blob Storage binding: read contents of file in blob storage
      - Cosmos db binding - look for document in Cosmos DB
      - Microsoft Graph binding - access OneDrive
  - Output Bindings
    - send messages, add document to database
    - write data to external service
    - e.g. 
      - Blob storage binding: create new file in blob storage
      - Queue storage binding: Post a message to Queue
      - Cosmos DB binding: create new document in Cosmos DB
      - Others: Even Hub, Service Bus
      - Connectors to 3rd party services: SendGrid(for sending emails), Twilio(for sending text messages) etc.
  - Azure Functions and Core Tools
    - Develop locally
- [Azure Durable Functions](create_durable_function_workflow_c%23.md) - C# and JavaScript
  - Extension to Azure Functions
  - Used to create stateful, serverless workflows ("Orchestrations")
  - 3 types of functions:
    - Client("Starter Function")
      - Initiate a new orchestration
      - use any trigger
    - Orchestrator Function
      - Defines the steps in the workflow
      - handle errors
    - Activity Function
      - Implement a step in the workflow
      - use any bindings
  - Orchestration Patterns for durable functions
    - ***Function Chaining***
      - Sequence of activity functions in specified order(Activity 1-> Activity 2->Activity 3)
    - ***Fan-out Fan-in***
      - Multiple activities in parallel
    - ***Asynchronous HTTP APIs***
      - e.g. Multiple Image downloads, processing those images in parallel  
      - used when we have an API that we need to pull repeatedly for progress.
      - Orchestrator keeps on pulling whereas long-running function keeps on running.
    - ***Monitor Process***
      - Do work/check status when something is completed/when a specific condition is met.
      - Poll and sleep
    - ***Human Interaction***
      - Request Approval
      - Process Approval
      - Escalate
    - ***Aggregators***
      - stateful entities
      - aggregate data over period of time within a single function
- Custom Handlers
  - We can create Azure functions in C#, Java, JavaScript, Python. PowerShell, etc.
  - But for languages that are not current supported like Rust, Go
    - and for runtime that are not current supported like Deno(an alternative JavaScript runtime), 
    - we use ***custom handlers***.
  - Trigger -> Functions Host -> Custom Handler(Web Server: runs function code) -> Target(Output bindings)
  - Steps to create custom handler
    - Create function app using ***function init*** selecting Custom as language
    - Create Azure function using any trigger type e.g. HTTP Trigger
    - Create a web server using custom language of choice
    - Compile your custom handler e.g. go build handler.go
    - update host.json file(defaultExecutablePath and enableForwardingHttpRequest)
      - set defaultExecutablePath to name of the executable: e.g. handler.exe
      - enableForwardingHttpRequest = True
      - The web server would listen on /api/FunctionName
    - Test locally(func start) or publish to Azure
  - extensionBundle
    - needed to support bindings and triggers
- Any Function contains 2 important pieces:
  - Your code
  - config: [functions.json](functions.json) file
    - function.json file defines:
      - function's triggers
        - every function has one and only one trigger
      - other config settings
        - runtime uses this config to determine events to monitor and 
        - pass data into and return data from function execution. 
- Function app
  - provides execution context in Azure in which functions run
  - unit of deployment and management for the functions
  - can have one or more functions managed, deployed and scaled together
  - all functions in function app share same pricing plan, deployment method and runtime version.
  - function app helps to organize and manage functions collectively.
- Triggers and Bindings
  - C# and Java have inline methods in code
    - decorating methods and parameters in C# class library/attributes
    - decorating methods and parameters with Java annotations
  - JS/PowerShell/Python/TypeScript
    - update [functions.json](functions.json) file
  - Binding Direction
    - Triggers always have direction: "in"
    - Input and Output bindings use "in" and "out" respectively
    - some bindings support special direction "inout"
      - i.e. use same binding for both Input and Output 
      - use advanced editor via Integrate tab in portal for "inout"
    - when using attributes in a class library to configure triggers and bindings,
      - direction is ***provided*** in an attribute constructor
        - or inferred from parameter type.
- [JavaScript Example](js_example.js) for using triggers and bindings from [functions.json](functions.json)