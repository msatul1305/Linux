# Azure PowerShell module install
Install-Module -Name Az -Force
#  Sign in to Azure:
Connect-AzAccount

# Select the correct subscription (if you have multiple subscriptions):
Select-AzSubscription -SubscriptionName "YourSubscriptionName"

# Reload Redis data from disk (RDB snapshot):
Invoke-AzRedisCacheReboot -ResourceGroupName "YourResourceGroupName" -Name "YourRedisCacheName" -RebootType AllNodes

# Purge all cache content (flush all data):
Invoke-AzRedisCacheFlush -ResourceGroupName "YourResourceGroupName" -Name "YourRedisCacheName"
