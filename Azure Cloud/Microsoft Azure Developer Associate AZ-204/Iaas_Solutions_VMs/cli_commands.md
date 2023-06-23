1. Azure CLI:
   - Installation: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows 
   - Download the latest version
   - After that open cmd prompt to use cli
   
- Commands
  - az: get help of commands available
  - az login: login to azure via terminal



- Using Azure CLI to deploy VM:
    - create group:
        - az group create --name "rgroup-name"  --location "centralus"
        - az vm create --resource-group "rgroup-name" --name "atulvm2" --image "win2019datacenter"  or "Ubuntu2204"  --admin-username "atul" --authentication-type "ssh" --generate-ssh-keys
        - SSH key files: 'C:\Users\msatu\.ssh\id_rsa', 'C:\Users\msatu\.ssh\id_rsa.pub'
        
- Enable remote access with azure cli:
    - az vm open-port -resource-group "rgroup-name" --name "vm_name" --port "3389"(for RDP) or "22"(for ssh)

- Retrieve public ip address of VM:
    - az vm list-ip-addresses --resource-group "rgroup-name" --name "vm_name"

- List of all resource groups available
    - az group list --output table

- Delete resource group:(All resources in the resource group will be deleted as well)
    - az group delete --name "rgroup-name"