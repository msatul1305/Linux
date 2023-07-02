# Create webapp from cli
# Create a resource group
az group create -n "rgroup" -l "location"
# create ***appservice plan*** with sku type as s1(standard plan) and linux os:
az appservice plan create --name "appserviceplanname" --resource-group "rgroup" --sku "s1" --is-linux
# create the webapp
az webapp create -g "rgroup" -p "planname" -n "webappname" --runtime "node|10.14"
