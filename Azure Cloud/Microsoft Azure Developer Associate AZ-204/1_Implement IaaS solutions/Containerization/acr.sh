# Creating and authenticating to ACR:
# create a global and unique ACR name to access the ACR
ACR_NAME='psdemoacr'

# create acr
az acr create --resource-group 'rgroup' --name $ACR_NAME --sku standard

# Login to ACR
az acr login --name $ACR_NAME

# Steps to push Image to ACR using Docker Tools:
#1. Login
ACR_NAME='psdemoacr'
ACR_LOGINSERVER=$(az acr show --name $ACR_NAME --query loginServer --output tsv)  #eg output = psdemoacr.azurecr.io

#2. Add alias to local container image using this login server and a new name and tag.
# This new tag tells docker when it needs to send the image when we execute docker push.
docker tag webappimage:v1 $ACR_LOGINSERVER/webappimage:v1     # Syntax: docker tag "source_image"  "Loginserver/name:tag"
docker push $ACR_LOGINSERVER/webappimage:v1

#3. Check if image is present in acr:
az acr repository list --name $ACR_NAME --output table
az acr repository show-tags --name $ACR_NAME --repository webappimage --output table

#4. use ACR tasks to read the Dockerfile in the current working directory and
# then zip up all the resources and code and upload into ACR to build the container image to use.
az acr build --image "webappimage:v1-acr-task" --registry $ACR_NAME .  # new name is used, "." is used to locate the dockerfile in pwd.
