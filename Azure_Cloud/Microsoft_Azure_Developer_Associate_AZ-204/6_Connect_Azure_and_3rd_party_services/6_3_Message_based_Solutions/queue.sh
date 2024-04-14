# create a queue
az storage queue create --name "queue_name"

# delete a queue
az storage queue delete --name "queue_name"

# view messages in a queue(without affecting visibility)
az storage message peek --queue-name "queue_name"

# delete all messages in a queue
az storage message clear --queue-name "queue_name"


# Interact with queue
# Open bash shell in Portal
export AZURE_STORAGE_ACCOUNT=storage_acc_name
az storage message peek --queue-name "qname" # return only 1 message
az storage message peek --queue-name "qname" --num-messages 32 # returns 32 messages max
# this will only peek the message but not get it/use or consume it

# to get/consume a message from queue
az storage message get --queue-name "qname"
# after consuming, delete that consumed message from queue using:
az storage message delete --id "msg_id" --pop-receipt "pop_receipt" --queue-name "qname"

