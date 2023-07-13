# syntax
azcopy copy
  "<source-path>"
  "<target-path>"
  --recursive=true

# Upload a local folder, SAS = shared access signature
azcopy copy
  "C:\Documents\*"
  "https://storage-acc-url/[container]?[SAS]"
  --recursive=true

# copy between containers
azcopy copy
  "https://storage-acc-01-url/[container]?[SAS]"
  "https://storage-acc-02-url/[container]?[SAS]"
  --recursive=true
