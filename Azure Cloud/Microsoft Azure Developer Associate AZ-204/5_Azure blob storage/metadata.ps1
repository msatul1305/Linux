$resourceGroup = 'pluralsight-resource-group'
Get-AzResourceGroup
$storageAccount =  Get-AzStorageAccount -Name <storage account name> -ResourceGroupName $resourceGroup

# list all containers in the storage account:
Get-AzStorageContainer -Context $storageAccount.Context

$carsAndEnginesContainer = Get-AzStorageContainer -Context
$storageAccount.Context -Name cars-and-engines

# View all the properties for cars-and-engines
$carsAndEnginesContainer.CloudBlobContainer.Properties

# create and set custom metadata
$carsAndEnginesContainer.CloudBlobContainer.Metadata.Add("content","pictures about cars and engine")
$carsAndEnginesContainer.CloudBlobContainer.Metadata.Add("pictures_count","4")
$carsAndEnginesContainer.CloudBlobContainer.SetMetadata()

# delete one pair of the custom metadata
$carsAndEnginesContainer.CloudBlobContainer.Metadata.Remove("content")
$carsAndEnginesContainer.CloudBlobContainer.SetMetadata()

# view the metadata that remains
$carsAndEnginesContainer.CloudBlobContainer.Metadata