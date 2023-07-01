# To delete all resource groups
for rgname in `az group list -o tsv`; do
echo Deleting ${rgname}
az group delete -n ${rgname} --yes --no-wait
done

