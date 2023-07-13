# 1
az role definition list --query "[?roleName == 'Owner']"
# 2
az role definition list --query "[?roleName == 'Storage Account Contributor']"