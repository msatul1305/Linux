- Azure Key Vault
  - Allows to securely store and access secrets like connection strings.
  - Types of secrets that can be stored in key vault:
    - Keys
      - Cryptographic keys e.g. used in Azure Disk Encryption, Azure Storage Account Encryption at Rest(SSE)
    - Secrets
      - sensitive info like DB connection strings, passwords
    - Certificates
      - x509 certificates used in HTTPS/SSL/TLS communications(encryption in transit)
  - Pricing Tiers
    - Standard
      - Secrets protected by Software
    - Premium
      - Standard + HSM-protected(store keys in Hardware security modules)
    - Provision Azure Key Vault
      - Azure Portal
      - Programmatically
        - PowerShell
        - Azure CLI
        - REST API
        - ARM templates
  - Implementing and configuring Azure Key Vault
  - Soft-delete and Purge-protection
  - Azure Key Vault References for Function Apps and App Services
    - used to move configuration settings for Function apps services to key vault without any code change.
  - Using Azure Key Vault
  - Configuring Authentication for Azure Vault Key(for access to key)
    1. Using azure AD app registration
       - register application via Azure AD and assign permissions to the app registration service through Azure Service Principal in key vault.
    2. Using Managed Identity(***preferred option***)
       - don't need to store client id and client secret in applications registration file
       - no code change required in app
         - Portal -> Key Vault -> Open Key vault -> Secrets -> Add the secret
         - enable system managed identities in the app that we can to access this secret from.
         - Application -> App settings -> update value of configuration settings with azure key vault reference(syntax= https://docs.microsoft.com/en-us/azue/app-service/app-service-key-vault-references)
    3. Using Key Vault References(New)
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
    - Protect Azure Key Vault using Soft delete and Purge Protection
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