# Create a service principal for ACI to pull from ACR:
ACR_NAME='actual_acr_name_deployed_earlier'
ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query-id --output tsv)
# shellcheck disable=SC2034
SP_NAME=acr-service-principal
SP_PASSWD=$(az ad sp create-for-rbac --name http://$ACR_NAME-pull --scopes $ACR_REGISTRY_ID --role acrpull --query password --output tsv)  #create a password to be used for ACI.
SP_APPID=$(az ad sp show --id http://$ACR_NAME-pull --query appId --output tsv)

# Run container from ACR to ACI
ACR_LOGINSERVER=$(az acr show --name $ACR_NAME --query loginServer --output tsv)
az container create --resource-group rgroup \
                    --name "webappname" \
                    --dns-name-label "hostname_for_container(used for fully qualified domain)" # eg. of dns name label = psdemo-webapp.cli.centralus.azurecontainer.io
                    --ports 80 --image $ACR_LOGINSERVER/webappimage:v1 \
                    --registry-login-server $ACR_LOGINSERVER \
                    --registry-username $SP_APPID \
                    --registry-password $SP_PASSWD
