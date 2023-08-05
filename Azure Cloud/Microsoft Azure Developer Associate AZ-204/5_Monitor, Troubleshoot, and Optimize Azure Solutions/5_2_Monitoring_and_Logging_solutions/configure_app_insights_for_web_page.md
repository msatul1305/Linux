## Configure Application Insights for a Web Page

### Step 1: Create an Application Insights Resource

1. Sign in to the Azure portal at [https://portal.azure.com](https://portal.azure.com).
2. Click on "Create a resource" in the left-hand menu.
3. Search for "Application Insights" and select "Application Insights" from the list of services.
4. Click on the "Create" button.
5. Fill in the required details:
   - **Name**: Provide a name for the Application Insights resource.
   - **Subscription**: Choose the appropriate subscription (if you have multiple).
   - **Resource group**: Select an existing resource group or create a new one.
   - **Application Type**: Choose "Web" for a web app.
   - **Web test location**: Choose the location closest to your web app's primary location.
6. Click on the "Review + create" button and then "Create" to create the Application Insights resource.

### Step 2: Add Application Insights JavaScript SDK to Your Web Page

1. Include the Application Insights JavaScript SDK in your web page. You can either reference it directly from the Azure CDN or download it and host it yourself. The latest SDK URL from the Azure CDN is:
   ```html
   <script src="https://js.monitor.azure.com/scripts/bundle/ai.2.min.js"></script>
Initialize Application Insights with your Instrumentation Key. Add the following script just before the closing </body> tag:
<script>
  var appInsights = window.appInsights || function(config) {
    function s(config) { t[config] = function() { var i = arguments; t.queue.push(function() { t[config].apply(t, i) }) } }
    var t = { config: config }; t.queue = []; s('trackPageView'); s('trackEvent');
    var r = document.createElement('script'); r.src = "https://js.monitor.azure.com/scripts/bundle/ai.2.min.js";
    document.getElementsByTagName('script')[0].parentNode.appendChild(r); return t;
  }({
    instrumentationKey: "YOUR_INSTRUMENTATION_KEY"
  });

  window.appInsights = appInsights;
  appInsights.trackPageView();
</script>
Replace "YOUR_INSTRUMENTATION_KEY" with the Instrumentation Key you obtained in Step 1.

### Step 3: Verify Data Collection
-  After adding the JavaScript SDK to your web page and deploying it, 
  - open the web page in your browser and interact with it.
  - After a few minutes, go to the Application Insights resource in the Azure portal (Monitoring > Application Insights). 
  - You should see telemetry data and metrics related to your web page's usage, 
  - including page views, browser and OS details, exceptions, and more.
