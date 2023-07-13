- Parameters
  - webAppName
  - sku
  - linuxFxVersion
  - location
- Deployment of ARM template via PowerShell
- Create new resource group
New-AzResourceGroup -Name "rgroup" -Location "loc"
- Deploy ARM template
New-AzResourceGroupDDeployment -ResourceGroupName "rgroup" -TemplateUri "https://raw.githubusercontent.com/Azure/azure-quickstart-template.json"
- Deployment of ARM template via CMD
az greoup create --name "rgroup" --location "loc" 
az group deployment create --resource-group "rgroup" --template-uri "https://raw.githubusercontent.com/Azure/azure-quickstart-template.json"
