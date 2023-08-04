# List of all resource groups available
az group list --output table

# Delete resource group:(All resources in the resource group will be deleted as well)
az group delete --name "rgroup-name"

# To delete all resource groups
for rgname in `az group list -o tsv`; do
echo Deleting ${rgname}
az group delete -n ${rgname} --yes --no-wait
done
