# list all management policies currently set up on the storage account
Get-AzStorageAccountManagementPolicy -ResourceGroupName rgroup 
                                     -AccountName <storage account>

# creates a variable holding the actions to be taken as part of the policy you are setting up.
$action = Add-AzStorageAccountManagementPolicyAction -BaseBlobAction TierToArchive 
                                                     -daysAfterModificationGreaterThan 90

$action = Add-AzStorageAccountManagementPolicyAction -InputObject $action 
                                                     -BaseBlobAction TierToCool 
                                                     -daysAfterModificationGreaterThan 30

# creates a variable holding the filter, which the policy will use to determine which blobs the policy applies to.
$PublicFilter = New-AzStorageAccountManagementPolicyFilter -DefaultProfile $GlobomanticsContext 
                                                            -PrefixMatch public

# creates a variable holding the rule which will be executed as part of the policy you are setting up.
$PublicLifecyleRule = New-AzStorageAccountManagementPolicyRule -Name PublicLifecyleRule 
                                                               -Action $action 
                                                               -Filter $PublicFilter

# set up the actual policy.
Set-AzStorageAccountManagementPolicy -ResourceGroupName rgroup 
                                     -StorageAccountName <storage account> 
                                     -Rule $PublicLifecyleRule

Get-AzStorageAccountManagementPolicy -ResourceGroupName rgroup 
                                     -AccountName <storage account>
