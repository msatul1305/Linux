- App Service
  - http based service for hosting web apps
  - web hosting 
  - windows or linux
  - Egs of web apps: ASP.net, APS.net core, Node.js, Python, PHP etc.
- App service Plans
  - Isolated and Non-Isolated
  - Non-Isolated:
    - not inside a virtual network
    - can be accessed via internet
    - Types:
      - Free and shared(F1, D1): not for PROD apps, run on shared infrastructure
      - Basic(B1,B2,B3): low traffic requirement apps, no autoscaling and traffic management.
      - Standard(S1,S2,S3): for PROD workloads - price based on no. of instances run
      - Premium v2(P1v2, P2v2, P3v2) - enhanced performance
      - Premium v3(P1v3, P2v3, P3v3) - faster processor
  - Isolated with App Service Environments(ASE):
    - fully isolated and dedicated environment for running web apps
    - environment is dedicated to your app and able to put in VNet.
    - high scale, memory utilization
    - secure network access
    - control over network traffic
    - app can connect to VPN to on-premise resources
- Create Azure Service Web Apps
  - App service plans
  - App service environments
  - create web app in portal
  - create web app with CLI
  - create web app with powershell
  - create web app with ARM template
- Steps to create a web app:
  - Go to App Service in azure portal
  - or search for web app

- Configuring Azure App Service
  - Securing web app with SSL
    - Secure a domain with SSl/TLS Binding
      - Use Basic, Standard, Premium or Isolated plan(Free plan doesn't provide SSL)
      - Public(Commercial certificate from authority like VeriSign) - Commonly used vs Private certificates(self generated)
      - Managed(purchase certificate from Azure and map to our domain called app service certificate) vs un-managed certificates(Own self-signed certificates, commercial vendor)
      - enforce HTTPS and TLS(Transport Layer Security)
  - Process to map a custom domain to app service
    - Go to Create a resource in portal
    - Go to web app -> Custom domains -> Add custom domain, copy domain verification details and hostname
    - Search for ***App Service Domain*** -> Create doamin and add cname record to verify that you own the domain with alias as hostname(.azurewebsites.net)
    - Add record set type:txt, name:asuid.www, paste domain verification ID in value.
    - For TLS/SSL: Go to web app-> TLS/SSL settings -> upload certificates or create a new one.
  - Configuring a DB Connection String
    - so that we don't have to hardcode into code when trying to connect to db
    - instead we can directly use the connection string present in memory as a variable
    - Steps:
      - Create a sql database in same location and resource group as webapp
      - Open db and copy connection string
      - Go to webapp -> configuration -> Connection String -> new -> update password inside connection string
      - Connection strings can be kept in secure key vaults as well
- Enable Diagnostic Logging
    -  Go to App Services -> select your webapp -> App Service logs 
    - Types:
      - Application Logging: log messages generated by webapp - levels: warnings, critical, errors etc.
        - can be stored on file system where app/code is running
        - or azure storage
      - Web server logging: can be stored on App Service file system where app/code is running or Azure Storage
        - log raw HTTP requests that comes in: 
          - HTTP request made
          - method used
          - client IP etc.
      - Detailed Error Messages
        - For windows based app service
        - users can't see these errors but useful for developers
      - Failed request tracing
        - For windows based app service
        - Detailed information on failed requests
        - Includes Trace of IS components used to process the requests and time it takes in each component to finish that process. *?
      - Deployment logging
        - both linux and windows based app services
        - logs when code is pushed to app service
        - deployment time error handling.
- Deploying code to app service web app
  - Configuring continuous deployment
    - pulls code from GitHub, Bitbucket, Azure Repos(part of Azure DevOps) and updates the deployment
  - Configuring continuous delivery
    - Azure DevOps or some other CI/CD system
  - Steps:
    - Authorize Azure App Service
      - go to web app -> Deployment center -> 
      - Define source control: Git, Azure Repos, Bitbucket, Local Git repo, manual deployment(push/sync): onedrive, dropbox, external, FTP
      - build provider: .Net compiler 
        - App service build service: kudu engine
        - GitHub actions
        - Azure pipelines
      - configure
    - Enable Continuous Deployment
    - Disable Continuous Deployment
- Scaling Azure App Service
  - Autoscale: available for standard, premium,and isolated tiers only.
    - Vertical vs Horizontal scaling
      - Vertical: adding resources: scale up v down
      - Horizontal: adding extra VMs using load balancers - Scaling In(reducing VM count) vs OUT(adding more VM)
  - Manually scaling App Service
    - Scale up and scale out option in portal
  - Scaling on a schedule: based on time. scale out at 9 am, scale back in at 10pm
    - scale out -> custom autoscale
  - Implementing autoscaling in app service
    - Autoscaling profile
      - Autoscaling actions
        - inc/dec no. of VMs.
        - send email notification of scaling change
        - ping a webhook as a notification to start some automated process
      - Capacity settings: max, min and default no. of instances
      - Rules: based on conditions
      - Notifications: via Azure Monitor
    - Designing Autoscaling Rules
      - Metrics(resource/custom): CPU utilization, compute instances, memory pressure, etc.
      - Time(schedule): 