# create a queue
az servicebus queue create --namespace-name "namespace" --name "queue_name" --resource-group "rgroup"

# delete a queue
az servicebus queue delete --namespace-name "namespace" --name "queue_name"

# to view messages of service bus: use service bus explorer in portal or SDK(not available via CLI)
