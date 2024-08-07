https://app.pluralsight.com/explore/certifications/topics/azure?trackId=670a6dc5-deec-40ff-a0f0-f41d900a38a6&examPrepId=06d2533c-d8b0-4f3b-9610-52f520045571
https://app.pluralsight.com/library/courses/microsoft-azure-developer-introduction-az-204-exam/table-of-contents
Microsoft Azure Developer: Introduction to the AZ-204 Exam by Matthew Kruczek

1. Exam
    - Topics
        - ***Develop Azure Compute Solutions(25%-30%)***
            - Containerization
              - Configure container images for solutions
              - Publish an image to the Azure Container Registry
              - Run containers by using Azure Container Instance 
            - Create Azure App Service Web Apps(PaaS solution)
                - Create an Azure App Service Web App
                - Enable diagnostic logging
                - deploy code to a web app
                - Configure web app settings
                - Implement autoscaling rules, including scheduled autoscaling, and scaling by operational or system metrics
            - Implement Azure Functions(API)
                - Create and deploy Azure functions
                - Implement input and output bindings for a function
                - Implement function triggers by using data operations, timers, and webhooks.
                - Implement Azure durable functions.
                - Implement custom handlers
        - ***Develop for Azure Storage(15%-20%)***
            - Develop Solutions that use Cosmos DB Storage: Non-relational, NoSQL DB
                - Select appropriate API and SDK for solution
                    - Cassandra, MongoDB, Gremlin, Table etc.
                - Implement partitioning schemes and partitioning keys
                    - Primary key, compound key etc.
                - Perform operations on data and Cosmos DB containers
                - Set the appropriate consistency level for operations
                    - Strong consistency level vs
                    - bounded staleness
                - Manage change feed notifications
        - ***Implement Azure Security(20%-25%)***
            - Implement user authentication and authorization - Workflow based
                - Authenticate and Authorize users by using the Microsoft Identity platform
                - Authenticate and Authorize users by using Azure Active Directory
                - Create and implement shared access signatures
            - Implement Secure Cloud Solutions
                - Secure app configuration data by using the App Configuration and Azure Key Vault.
                - Develop code that uses keys, secrets and certificates stored in Azure Key Vault
                - Implement solution that interact with Microsoft Graph
                    - Series of APIs that allows to connect to M365 subscription for both getting and setting data.
        - ***Monitor, troubleshoot, and optimize Azure solutions(15%-20%)***
            - Optimize
                - Integrate Caching and Content Delivery within Solutions
                    - Configure Cache and expiration policies for Azure Redis Cache
                    - Implement secure and optimized application cache patterns including data sizing, connections, encryption, and expiration
                - Instrument Solutions to Support Monitoring and Logging
                    - Configure an app or service to use Application Insights
                    - Analyze and troubleshoot solutions by using Azure Monitor
                    - Implement Application Insights web tests and alerts
        - ***Connect to and consume Azure Services, and third party services(15%-20%)***
            - Implement API management
                - Create an APIM instance
                - Configure authentication for APIs
                - Define policies for APIs
            - Develop Event-Based Solutions
                - Implement solutions that use Azure Event Grid: for more reactive-based programming
                - Implement solutions that use Azure Event Hub: for more enterprise streaming-based scenarios.
            - Develop Message-Based Solutions
                - Implement solutions that use Azure Service Bus
                - Implement solutions that use Azure Queue Storage Queues
- Exam Pointers
    - Review Azure App Service
        - capability of each tier
        - order of steps to create and deploy application
            - App service plan must be created before we can create an application
        - deployment slots and slot swapping
            - when to use auto swap and not
            - initialization steps when doing auto swap
        - Configure scaling and tiers
        - which use cases require isolated tier
        - process of deploying containers
        - Accessing logs(Historical and real time)
        - Review CLI commands
        - ASE(Azure App Service Environment)
        - Custom warm up for deployment slots
            - proper warm up happens before slot deployment before getting into prod
    - Review Azure functions
        - configuration of I/O bindings
        - Integrations with other services
        - Durable functions uses cases best fit scenarios
        - function metrics and logging info
- Note: Azure Kubernetes Service(AKS) is out of scope for this certification exam, Also VM(IaaS)