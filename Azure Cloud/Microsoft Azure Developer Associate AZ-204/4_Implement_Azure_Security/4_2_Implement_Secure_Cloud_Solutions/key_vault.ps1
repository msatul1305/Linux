# Create new key vault
New-AzKeyVault -VaultName 'vname' -ResourceGroupName 'rgroup' -Location 'East US'

# Syntax
($resource = Get-AzResource -ResourceId (Get-AzKyVault -VaultName 'vname').ResourceId)
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties

# enable soft-delete on existing vault
# use the Set-AzKeyVault cmdlet.
$resourceGroupName = "YourResourceGroupName"
$keyVaultName = "YourKeyVaultName"

# Get the existing Key Vault object
$keyVault = Get-AzKeyVault -VaultName $keyVaultName -ResourceGroupName $resourceGroupName

# Enable Soft Delete
$keyVault.EnableSoftDelete = $true
Set-AzKeyVault -VaultName $keyVaultName -ResourceGroupName $resourceGroupName -Vault $keyVault

# enable purge protection on existing vault
# use the Set-AzKeyVault cmdlet.
# Get the existing Key Vault object
$keyVault = Get-AzKeyVault -VaultName $keyVaultName -ResourceGroupName $resourceGroupName

# Enable Purge Protection
$keyVault.EnablePurgeProtection = $true
Set-AzKeyVault -VaultName $keyVaultName -ResourceGroupName $resourceGroupName -Vault $keyVault

# ChatGPT
