# Create variables
$webappname = "mywebapp$(Get-Random)"
$rgname = 'resourcegroupname'
$location = 'westus2'

# Create a resource group
New-AzResourceGroup -Name $rgname -Location $location

# Create an app service plan in s1 tier
New-AzAppServicePlan -Name $webappname -Location $location -ResourceGroupName $rgname -Tier S1

# Create the web app
New-AzWebApp -Name $webappname -Location $location -AppServicePlan $webappname -ResourceGroupName $rgname


# PowerShell cmdlet used to grant access to developer groups to publish code to web app via RBAC:
New-AzRoleAssignment
