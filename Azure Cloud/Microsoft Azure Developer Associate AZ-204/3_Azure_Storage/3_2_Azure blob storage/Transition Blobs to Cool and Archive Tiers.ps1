$GlobomanticsAccountKey = (Get-AzureRmStorageAccountKey -ResourceGroupName pluralsight-resource-group -Name <storage account>).Value[0]
$GlobomanticsContext = New-AzureStorageContext -StorageAccountName <storage account> -StorageAccountKey $GlobomanticsAccountKey
#  lists all blobs in the archive container.
Get-AzStorageBlob -Container "archive" -context $GlobomanticsContext
# create an array of all blobs in the archive container, and transition all the blobs to the archive tier.
$Blobs = Get-AzureStorageBlob -Context $GlobomanticsContext -Container "archive"

Foreach($Blob in $Blobs){

    $blob.icloudblob.SetStandardBlobTier("archive")

}

# transition all the blobs in the public container to the cool tier:
$Blobs = Get-AzureStorageBlob -Context $GlobomanticsContext -Container "public"

Foreach($Blob in $Blobs){

    $blob.icloudblob.SetStandardBlobTier("cool")

}
# verify that all blobs in the public container have been transitioned to the Cool tier by running this:
Get-AzStorageBlob -Container "public" -context $GlobomanticsContext

