# set softdelete as true
($resource = Get-AzResource -ResourceId (Get-AzKeyVault -VaultName 'vname').ResourceId).Properties |
                                    Add-Member -MemberType "NoteProperty" -Name "enableSoftDelete" -Value "true"
# commit the change
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties


# Enable Purge Protection for new vault
New-AzKeyVault -Name "kvname" - ResourceGroupName "rgroup" - Location "eastus" - EnableSoftDelete "true"

# Enable Purge Protection for exisiting vault
($resource = Get-AzResource -ResourceId (Get-AzKeyVault -VaultName 'vname').ResourceId).Properties |
        Add-Member -MemberType "NoteProperty" -Name "enablePurgeProtection" -Value "true"
# commit the change
Set-AzResource -resourceid $resource.ResourceId -Properties $resource.Properties
