# Install dependencies: Before you can get started, you should install Node.js which includes npm.
npm install -g azure-functions-core-tools@4 --unsafe-perm true
# Create an Azure Functions project: In the terminal window or from a command prompt, navigate to an empty folder for your project, and run the following command:
func init
# Create a function: This will prompt you to choose a template for your function. We recommend HTTP trigger for getting started.
func new
# Run your function project locally
func start
# Deploy your code to Azure
func azure functionapp publish "function_name"
# get URL and try to run the function.