# Event Hubs namespace creation
# sku: Basic or Standard
az eventhubs namespace create --resource-group "rgrp"
                              --location "loc"
                              --name "namespace_name"
                              --sku Standard

# Event Hubs Creation
# namespace must be created before
# message retention can be between 1-7 days
# patition count cab be between 2-32 (default: 4)
az eventhubs eventhub create --name "event_hub_name"
                             --namespace "namespace_name"
                             --message-retention 3
                             --partition-count 4
                             -g "rgroup"
