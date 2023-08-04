# Create new key vault
New-AzKeyVault -VaultName 'vname' -ResourceGroupName 'rgroup' -Location 'East US'

# enable soft-delete on existing vault
($resource = Get-AzResource -ResourceId (Get-AzKyVault -VaultName 'vname').ResourceId)
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties

# enable purge protection on existing vault(once enabled, it can not be disabled
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties
