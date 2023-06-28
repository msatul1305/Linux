# All powershell commands are of the syntax: "Verb-Action"
# Check if az powershell is installed:
get-command az
# Install Azure PowerShell on Windows: install-module -name az -allowclobber  (allowclobber means forced update rewriting prev installation)
Get-ExecutionPolicy -List
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Install-Module -Name Az -Repository PSGallery -Force
Update-Module -Name Az -Force
# 2. Sign in:
#    -


# Deploy ARM template via Powershell:
New-AzResourceGroupDeployment -Name mydeployment -ResourceGroupName 'rgroup' -TemplateFile './template/template.json' -TemplateParameterFile './template/parameter.json'

# Using Azure Powershell to deploy VM:
# Steps:
# Login to Azure
Connect-AzAccount -SubscriptionName 'Demo Acc'
# Ensure pointed to correct subscription:
Set-AzAccount -SubscriptionName 'Demo Acc'
# Create a resource group:
New-AzResourceGroup -Name "rgroup" -Location "CentralUS"
# Create a PSCredential Object with username and password:
$username = 'demoadmin'
$password = ConvertTo-SecureString 'password' -AsPlainText -Force
$WindowsCred = New-Object System.Management.Automation.PSCredential ($username, $password)
# Create VM:
New-AzVM -ResourceGroupName 'rgroup' -Name 'vmname' -Image 'Win2019Datacenter' -Credential $WindowsCred -OpenPorts 3389
# or
New-AzVM -ResourceGroupName 'rgroup2' -Name 'vmname' -Image 'Ubuntu2204' -size "standard_b1s"
# To get public IP address of VM:(didn't work in free trial)
Get-AzPublicIpAddress -ResourceGroupName 'rgroup' -Name 'vmname' | Select-Object IpAddress
# To delete resource group:
Remove-AzResourceGroup -Name 'rgroup'
