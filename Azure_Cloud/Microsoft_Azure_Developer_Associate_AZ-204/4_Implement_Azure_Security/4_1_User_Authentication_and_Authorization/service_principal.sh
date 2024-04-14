# Step 1: Create a Service Principal
az ad sp craete-for-rbac --name "service_principal_name"
                         --role "role"
                         --scopes "/subscriptions/sub-id/resourceGroups/rgroup"

# Step 2: Assign Roles to the Service Principal
az role assignment create --assignee "service-principal_object_id"
                          --role "role"
                          --scope "/subscriptions/sub-id/resourceGroups/rgroup"

# Step 3: Obtain Credentials of the Service Principal
# After creating the Service Principal,
# you will get the credentials in output(Client ID and Client Secret) needed for authentication.

# Step 4: Access Azure Resources using the Client ID(App ID) and Client Secret(Certificate or Directory ID)
