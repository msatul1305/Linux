- Azure Key Vault
  - Allows to securely store and access secrets like connection strings.
  - Types of secrets that can be stored in key vault:
    - ***Keys***
      - Cryptic keys e.g. used in Azure Disk Encryption, Azure Storage Account Encryption at Rest(SSE)
      - Azure Key Vault keys library client
        - supports RSA keys and Elliptic Curve(EC) keys
        - offers operation to create, retrieve, update, list, purge, backup, restore and delete keys and its versions
    - ***Secrets***
      - sensitive info like DB connection strings, passwords
      - Azure Key Vault secrets client library
        - secretly store and control access to tokens, passwords and API keys and other secrets.
        - offers operation to create, retrieve, update, list, purge, backup, restore and delete secrets and its versions 
    - ***Certificates***
      - x509 certificates used in HTTPS/SSL/TLS communications(encryption in transit)
      - Azure Key Vault certificates client library
        - manage, create, update, list and delete certificates, policies, issuers and contacts.
  - Pricing Tiers
    - ***Standard***
      - Secrets protected by Software(RSA key)
    - ***Premium***
      - Standard (RSA key)+ HSM-protected(store keys in Hardware security modules)
  - Provision Azure Key Vault
    - Azure Portal
      - Portal -> new Azure Key Vault -> + Resource -> Key Vault -> select subscription, rgroup, region.
    - Programmatically
      - [PowerShell](key_vault.ps1)
      - [Azure CLI](key_vault.sh)
      - REST API
      - ARM templates
  - Implementing and configuring Azure Key Vault
  - Soft-delete and Purge-protection
    - Soft delete: Allows recovery of deleted values and key vault objects(7 to 90 days)
      - enabled by default for all new key vaults.
    - Purge-protection: Safeguard against permanently deleting the key/secret
  - Azure Key Vault References for Function Apps and App Services
    - used to move configuration settings for Function apps services to key vault without any code change.
  - Using Azure Key Vault
  - Configuring Authentication for Azure Vault Key(for access to key)
    - i.e. App to obtain an identity before accessing services
    1. Using azure AD app registration
       - register application via Azure AD and assign permissions to the app registration service through Azure Service Principal in key vault.
    2. Using Managed Identity(***preferred option***)
       - Types: 
         - System-assigned
         - User-assigned
       - when app is deployed on a vm, 
         - we can assign an identity to vm that has access to key vault.
         - for system-managed identities, account needs VM Contributor role assignment
         - no additional Azure AD role assignments are required
       - don't need to store client id and client secret in applications registration file
       - no code change required in app
         - Portal -> Key Vault -> Secrets -> Add the secret
         - enable system managed identities in the app that we can to access this secret from.
         - Application -> App settings -> update value of configuration settings with azure key vault reference(syntax= https://docs.microsoft.com/en-us/azure/app-service/app-service-key-vault-references)
           - e.g. az webapp config set --subscription <sub> -g <group-name> -n <app-name> --generic-configurations '{"vnetRouteAllEnabled": true}'
    3. Using Key Vault References(New)
       - Service Principal and certificate
         - use a service principal and an associated certificate which has access to key vault.
       - Service Principal and secret
         - ***not recommended***
       - access key vault from azure functions or app services.
         - Move the configuration setting to key vault
         - deploy your app service/azure function
         - create system-assigned managed identity for the app: App service or function
         - give GET KV SECRETS access to the app identity(Get-KeyVaultSecrets)
         - update the configuration values with KV reference syntax
         - verify your app functionality by testing it.
    - Portal -> Key vault -> open key vault -> add new key vault -> (left side-bar)keys, secrets, certificates, access controls
    - Syntax to set app setting values
      - syntax 1
      - @Microsoft.KeyVault(VaultName=vname;SecretName=blobConnString;SecretVersion=dnjwabkdlawbjdbjh)
      - syntax 2
      - @Microsoft.KeyVault(SecretUri=https://vname.vault.azure.net/secrets/blobConnectionString/dnjwabkdlawbjdbjh)
    - Protect Azure Key Vault using [Soft delete and Purge Protection](soft_delete_and_purge.ps1)
      - Soft delete
        - Allows recovery of deleted values and key vault objects(keys, secrets and certificates)
          - within 7 days to 90 days(configurable)
        - enabled by default for all new key vaults.
        - To recover deleted secrets
          - Portal -> Key vault -> secrets -> manage deleted secrets - recover
      - PURGE operation
        - used to permanently delete the key/secret
        - not recoverable
        - to prevent purge operation
          - enable Azure Key Vault purge protection
        - to enable purge for an account
          - Portal -> key vault -> access policies -> user -> secret permissions -> enable purge
    - Using Azure key Vault keys for Storage Service Encryption(SSE)
      - used to store keys and certificates instead of secrets
      - Portal -> key vault -> keys -> Generate/Import -> create
        - use this key in storage account
          - Portal -> storage account -> Encryption -> Customer managed keys -> Enter URI or select from key vault -> save