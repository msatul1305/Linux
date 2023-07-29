# create a topic
az servicebus topic create --namespace-name "namespace" --name "topic_name" --resource-group "rgroup"

# delete a topic
az servicebus topic delete --namespace-name "namespace" --name "topic_name"

# create a subscription
az servicebus topic subscription create --namespace-name "namespace" --name "subscription_name" --topic-name "topic_name"
