# step 1: create user-assigned managed identity
az identity create -g "rgroup" -n "identity-name" -l "location"
# or
az identity create -group "rgroup" -name "identity-name" -location "location"

# step 2(optional): assign identity to a resource
az vm identity assign -g "rgroup" -n "vmname" --identities "identity-resource-id"
