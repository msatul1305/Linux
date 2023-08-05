# Reload Redis data from disk (RDB snapshot):
az redis force-reboot --resource-group YourResourceGroupName --name YourRedisCacheName --reboot-type AllNodes

# Purge all cache content (flush all data):
az redis delete --resource-group YourResourceGroupName --name YourRedisCacheName --yes
# Please exercise caution while using the az redis delete command,
# as it will permanently remove all data from the Redis cache,
# and there is no way to recover the data once it is deleted.
