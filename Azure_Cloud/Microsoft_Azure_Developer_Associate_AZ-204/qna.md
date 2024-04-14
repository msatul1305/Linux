1. You manage an Azure Cosmos DB container named container1.
You need to use the ReadItemAsync method to read an item from the Azure Cosmos service.
Which two parameters do you need to provide? Each correct answer presents part of the solution.
    - Ans. partitionKey, itemID
    - he consistencyLevel parameter is part of the optional requestOptions parameter of the ReadItemAsync
    - The eTag and sessionToken parameters are part of the optional requestOptions parameter of the ReadItemAsync method.
2.  The HTTP verb to define metadata is a PUT and not POST
3. You need to download blob content to a byte array after a transient fault happens. Which code statement should you use?
   - byte[] data; BlobClientOptions options = new BlobClientOptions(); 
   - options.Retry.MaxRetries = 10; 
   - options.Retry.Delay = TimeSpan.FromSeconds(20); 
   - BlobClient client = new BlobClient(new Uri("https://mystorageaccount.blob.core.windows.net/containers/blob.txt"), options); 
   - Response<BlobDownloadResult> response = client.DownloadContent(); 
   - data = response.Value.Content.ToArray();
4. A company implements an Azure Cosmos DB account named Account1 to store product details.
You need to write a parameterized SQL query to get items from the Products container based on category and price as parameters.
Which SQL query should you write?
    - SELECT * FROM Products p WHERE p.category = @Category AND p.price = @Price
    - Azure Cosmos DB supports SQL queries with parameters expressed by the @ notation
    - When writing SQL queries based on parameters, we need to mention the name of the container in the Azure Cosmos DB account.
5. You are developing an application. You need to set the standard HTTP properties of containers in Azure Blob Storage.
Which two HTTP properties can you set? Each correct answer presents part of the solution.
    - The only two HTTP properties that are available for containers are ETag and Last-Modified.
    - Last-Modified, Cache-Control, Origin and Range are properties only available for blobs.
6. You need to create a container in a container group and mount an Azure file share as volume.
Which code segment should you use?
   - az container create -g MyResourceGroup --name myapp --image myimage:latest --command-line "cat /mnt/azfile/myfile" --azure-file-volume-share-name myshare --azure-file-volume-account-name mystorageaccount --azure-file-volume-account-key mystoragekey --azure-file-volume-mount-path /mnt/azfile
7. You create an Azure web app locally. The web app consists of a ZIP package.
You need to deploy the web app by using the Azure CLI. The deployment must reduce the likelihood of locked files.
    - Run az webapp deploys to a staging slot with auto swap on.
8. You need to configure a web app to allow external requests from https://myapps.com.
Which Azure CLI command should you use?
   - az webapp cors add -g MyResourceGroup -n MyWebApp --allowed-origins https://myapps.com
9. You plan to create an Azure function app named app1.
You need to ensure that app1 will satisfy the following requirements:
Supports automatic scaling.
Has event-based scaling behavior.
Provides a serverless pricing model.
Which hosting plan should you use?
    - Consumption
10. You create a batch routine by using a timer trigger in Azure Functions.
You need to configure the batch routine to execute every 15 minutes.
Which code segment should you use?
    - [FunctionName("TimerTriggerCSharp")] 
    - public static void Run([TimerTrigger("0 */15 * * * 1-5")]
    - TimerInfo myTimer, ILogger log) 
    - { if (myTimer.IsPastDue) { log.LogInformation("Timer is running late!"); } 
    - log.LogInformation($"C# Timer trigger function executed at: {DateTime.Now}"); }
11. You have an Azure App Configuration instance named AppConfig1 and an Azure key vault named KeyVault1.
You plan to encrypt data stored in AppConfig1 by using your own key stored in KeyVault1.
You need to grant permissions in KeyVault1 to the identity assigned to AppConfig1.
Which three key-specific permissions should you use? Each correct answer presents part of the solution.
    - To use the custom key stored in KeyVault1, the identity assigned to AppConfig1 needs to have GET, WRAP, and UNWRAP permissions to the custom key. The DECRYPT and ENCRYPT permissions are not required to use the custom key stored in KeyVault1 in this scenario.
12. You plan to use Azure API Management for Hybrid and multicloud API management.
You need to create a self-hosted gateway for production.
Which container image tag should you use?
    - Ans. 2.0.1
    - This item tests the candidate’s knowledge of self-hosted gateways in Azure API Management. In production, the version must be pinned. The only way to achieve that is by using a tag that follows the convention {major}.{minor}.{patch}. The v3 tag will result in always running a major version with every new feature and patch. The latest tag is used for evaluating the self-hosted gateway. The V3-preview tag should be used to run the latest preview container image.
13. You have an Azure event hub.
You need to add partitions to the event hub.
Which code segment should you use?
    - az eventhubs eventhub update --resource-group MyResourceGroupName --namespace-name MyNamespaceName --name MyEventHubName --partition-count 12
    - The code segment that includes az eventhubs eventhub update adds partitions to an existing event hub. The code segment that includes az eventhubs eventhub consumer-group update updates the event hub consumer group. The code segment that includes az eventhubs eventhub consumer-group create will create an event hub consumer group. The code segment that includes az eventhubs eventhub create --resource-group segment will create an event hub with partitions, not change an existing one
14. You have an instance of Azure Event Grid.
You need to ensure an application can receive events filtered by values in the data field in the advanced filtering options.
Which filter should you use?
    - advanced
    - An advanced filter is used to filter events by values in the data fields and specify the comparison operator. An event type filter is used to send only certain event types to the endpoint. A subject filter is used to specify a starting or ending value for the subject. Topics is not a type of filter; the event grid topic provides an endpoint where the source sends events.
15. You manage an Azure Cache for Redis instance.
You need to load data on demand into the cache from a large database.
Which application architecture pattern should you use?
    - data cache
    - Databases often are too large to load directly into a cache, so it is common to use data cache pattern. Session store is used to store user-session information instead of storing too much data in a cookie that can adversely affect performance. Distributed transactions allow a series of commands to run on a back-end datastore as a single operation. By using content cache, you can provide quicker access to static content compared to back-end datastores. Session store, distributed transactions, and content cache cannot be used to load data on demand.
16. You plan to use Azure Cache for Redis as the caching layer for several applications.
You have the following requirements:
Prevent data loss if nodes are down.
Minimize storage costs.
Optimize performance.
    - Redis database (RDB) persistence with the soft-delete feature disabled on the associated storage account.
    - RDB persistence saves backups based on the configured backup interval with minimal effect on performance. Disabling the soft-delete feature on a storage account means Azure Cache for Redis can minimize storage costs by deleting the old backup data. Enabling the soft-delete feature on a storage account means Azure Cache for Redis cannot minimize storage costs by deleting the old backup data. AOF persistence saves every write to a log, which has a significant effect on throughput. Disabling and enabling the soft-delete feature on a storage account means Azure Cache for Redis cannot minimize storage costs by deleting the old backup data.
17. You have an Application Insights instance named insight1.
You need to configure a web app to send telemetry data to insight1.
Which Application Insights parameter should you use?
    - instrumentation key
    - To send telemetry data to an Application Insights resource from an app, you need to configure the app with the instrumentation key of the Application Insights instance. You can use alerts to ensure your team is aware of critical issues immediately. Alerts need to be configured inside insight1 and not the web app. You can use the data shown with each component to diagnose performance bottlenecks and failure hotspots. It needs to be configured inside insight1 and not the web app. Usage analysis provides information about an app's users and needs to be configured in insight1, not the web app.
18. You plan to use Application Insights to monitor the performance of an on-premises web application.
You need to identify a configuration that satisfies the following requirements:
Minimize the volume of data ingested into Application Insights.
Maximize the accuracy of the collected metrics.
     - Use standard metrics.
     - Using standard metrics both minimizes the volume of data ingested into Application Insights and maximizes the accuracy of the collected metrics. Applying sampling and filtering would negatively affect the accuracy of the collected metrics. Using log-based metrics does not minimize the volume of data ingested into Application Insights.
19. You need to generate a shared access signature token that grants the Read permission to a blob container.
Which code segment should you use?
    - BlobSasBuilder sasBuilder = new BlobSasBuilder() 
    - { BlobContainerName = containerClient.Name, Resource = "c" }; 
    - sasBuilder.ExpiresOn = DateTimeOffset.UtcNow.AddHours(1); 
    - sasBuilder.SetPermissions(BlobContainerSasPermissions.Read); 
    - Uri sasUri = containerClient.GenerateSasUri(sasBuilder);
    - The code segment that includes Resource = "c" and sasBuilder.SetPermissions(BlobContainerSasPermissions.Read); will generate the shared access signatures token that grants the Read permission to a blob container. The code segment that includes resource = ‘b’ will generate a shared access signatures token at the blob level. The code segments that include sasBuilder.SetPermissions(BlobContainerSasPermissions.Create); will generate a shared access signatures token with the Create permission at the blob level.
20. You need to group keys in Azure App Configuration.
What are two possible ways to achieve this goal? Each correct answer presents a complete solution.
    - Organize keys by using key prefixes.
    - Organize keys by using labels.
    - Key prefixes are the beginning parts of keys. A set of keys can be grouped by using the same prefix in names. Labels are an attribute on keys. Labels are used to create variants of a key. For example, labels can be assigned to multiple versions of a key. Authorizing role-based access control to read Azure App Configuration is not a valid way to group keys. Authorizing a managed identity to read Azure App Configuration is not a valid way to group keys.
21. You need to set a duration of 10 seconds for a key stored in Azure Cache for Redis.
Which code segment should you use?
    - using (var cache = ConnectionMultiplexer.Connect("")) { IDatabase db = cache.GetDatabase(); bool setValue = await db.StringSetAsync("test:key", "10", TimeSpan.FromSeconds(10)); }
22. You develop an Azure function that connects to a SQL database. The function is instrumented by using Application Insights.
You need to view the full SQL query text when inspecting the Dependency tab in Application Insights.
Which two settings in the host.json file should you use? Each correct answer presents part of the solution.
    - "enableDependencyTracking": true
    - "dependencyTrackingOptions": { "enableSqlCommandTextInstrumentation": true }
23. You need to implement an Azure Storage lifecycle policy for append blobs.
Which rule action should you use?
    - delete
    - The delete rule action supports both block blobs and append blobs. The enableAutoTierToHotFromCool, tierToArchive, and tierToCool rule actions only supports block blobs.
24. You are planning to host a static website in an Azure Storage account.
The website must be accessible only through HTTPS by using a custom domain name.
You enable the static website hosting feature. You set the default page to index.html and the error page to error.html.
Which two actions should you perform next? Each correct answer presents part of the solution.
    - Integrate the static website with Azure Content Delivery Network (CDN). 
    - Upload the index.html and error.html files to the web hosting container.
    - To host a static website in a storage account, the feature must be enabled. When enabling it, the names of the default and error documents must be informed. This creates a $web container, with private access, where the site files must be uploaded to. A custom domain can be added to the site. For HTTP only access, it can be registered to the networking tab of the storage account. For HTTPS access, Azure Content Delivery Network (CDN) must be used.
25. You need to delete an image with the tag dev/nginx:latest from an Azure container registry named devregistry.
Which code segment should you use?
    - az acr repository delete --name devregistry --image dev/nginx:latest
26. You plan to develop an Azure App Service web app named app1 by using a Windows custom container.
You need to load a TLS/SSL certificate in application code.
Which app setting should you configure?
    - WEBSITE_LOAD_CERTIFICATES
    - The WEBSITE_LOAD_CERTIFICATES app setting makes the specified certificates accessible to Windows or Linux custom containers as files. The WEBSITE_ROOT_CERTS_PATH app setting is read-only and does not allow comma-separated thumbprint values to be mentioned to the certificates and then be loaded in the code. The WEBSITE_AUTH_TOKEN_CONTAINER_SASURL app setting is used to instruct the auth module to store and load all encrypted tokens to the specified blob storage container. This setting is used for Azure Storage and cannot be used to load certificates inside a Windows custom container.
27. You have an Azure Key Vault named MyVault.
You need to use a key vault reference to access a secret named MyConnection from MyVault.
Which code segment should you use?
    - @Microsoft.KeyVault(SecretName=MyConnection;VaultName=MyVault)
28. You need to deploy an Azure Files share along with a container group to Azure Container Instances (ACI).
Which deployment method should you use?
    - Azure Resource Manager template
    - There are two common ways to deploy a multi-container group: use an Azure Resource Manager template or a YAML file. An Azure Resource Manager template is recommended when you need to deploy additional Azure service resources (for example, an Azure Files share) when you deploy the container instances. However, a YAML file does not support the deployment of additional Azure service resources along with container groups in ACI. Docker Compose and Azure CLI do not support the deployment of an Azure Files share along with a container group to ACI.
29. You manage an instance of Azure API Management. You define policies to multiple scopes.
You need to enforce a policy evaluation order.
What should you use?c
    - the <base /> element
    - The <base /> element provides the ability to enforce policy evaluation order. The <when /> element is part of the choose policy and is evaluated in order of its appearance within the policy. The follow-redirects attribute is part of the forward request policy, so it does not have any impact on the policy evaluation order. The condition attribute is part of the retry policy, so it does not have any impact on the policy evaluation order.
30. You need to capture events streaming from Azure Event Hubs.
To which three locations can you capture data? Each correct answer presents a complete solution.
    - Azure Blob storage 
    - Azure Data Lake Storage Gen1 
    - Azure Data Lake Storage Gen2
