- Exam alert: Implement Azure Security
  - User authentication and authorization
  - Implement secure cloud solution
  - Key vault
  - M Graph

- Core Azure RBAC concepts
  - Security principal = users/groups/identities
  - role def
  - scope
  - role assignment

- SAS best practices
  - Always use HTTPS
  - use user delegation whenever possible(only for blob storage thou)
  - define Stored access policy for service specific SAS
  - use near-term expiration on ad hoc, service or account sas
  - follow least-privilege access for resources to be accessed
- Mutual TLS Auth
  - not supported on free/shared tiers
  - stores client certificate in http header in ***X-ARR-ClientCert*** header
    - Base64 encoded certificate
  - App code is required to validate certificate


- M graph integration with application process:
  - Register app with azure ad
  - use m Identity platform endpoint with defined scopes
  - user signs in with credentials and accepts the scopes
  - app receives authorization code
  - auth code can be used to get token from token endpoint
  - token can be leveraged to access M graph