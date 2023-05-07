Azure Cloud

Why Cloud?
1. High availability
2. Reliability(Fault Tolerance/Disaster Recover) - Resilience -> Deployed in multiple locations, Load balancing.
3. Scalability - Adding more resources as need. Scaling out = Adding more resources. Scale up/down - make current resources bigger/smaller.
4. Predictability - performance and cost. Auto-scaling, load balancing.
5. Security - Full control - Patching, Maintenance, Network traffic control.
6. Governance - Regulatory, Auditory requirements.
7. Manageability - 
   Management of the cloud
    - AutoScaling
    - Monitoring
    - Template-based deployments
   Management in the cloud
    - Portal
    - CLI
    - APIs

CLI
1. az create vm - To create a new VM 


Using PowerShell
Cmdlet - Small lightweight commands/scripts used to do some specific functions/tasks.
1. New-AzVm - To create a new VM

ARM - Azure Resource manager
ARM Benefits
    - Group resource handling: deploy, manage and monitor resources as a group.
    - Consistency: consistent result of deployment.
    - Dependencies: define independency.
    - Access Control: built-in user right control.
    - Tagging: tag resources
    - Billing: bill for group of resources with similar tag.

Cloud Computing - On demand availability of computer resources split into 3 main categories:
    1. Compute
    2. Networking
    3. Storage

Cloud Economics - pricing
    Return on Investments(ROI)
    1. Capital Expenditure(Capex) - Fixed assets like land, building, equipment.
    2. Operational Expenditure(Opex) - ongoing day-to-day costs, annual costs.
    - Hourly pricing
    - consumption
        - per execution of function
        - per second
        - Combination

As a Service
 - On-Premises - Old practice where company own the hardware. 
 - IaaS - Infrastructure as a service: Provides Servers, Storages, Networking.
   - actual servers, scaling is fast, no ownership of hardware.
 - PaaS - Platform as a service
   - IaaS + Middleware + Tools like data-warehouses, Database, API etc.
 - SaaS - Software as a service
   - IaaS + PaaS + Software - eg. Gmail for email, Tally for accounting, Office 365, Azure SQL server, Azure active directory
 - Serverless - Extreme PaaS
    - You don't have to manage any servers.
    - you are effecively using someone's server to run on. 
    - e.g. Azure functions
    - Azure functions -> Completely extracting away the server in such a way that single functon of code can be
    hosted, deployed, run and managed without having to maintain full application.

Identifying Cloud Service Models - IaaS vs PaaS vs SaaS
    - IaaS: Org have complete control of infrastructure. e.g. VM, VNet, Storage
    - PaaS: Virtualized resources can cbe scaled up or down. e.g. App Services, Azure CDN, Cosmos DB
    - Saas: Remote server central location - e.g. Microsoft 365


Types of Cloud
    - Private - Similar to on premise where owning team is responsible for staffing, maintenance.
    - Public - Accessible anywhere across the globe. e.g. Azure, AWS, GCP.
    - Hybrid - Public + Private - For regulatory reasons.

Scale set
    - set of identical VMs.
    - Activated and deactivated as needed. - auto-scalability and load balancing. 
    - e.g. if VM1 takes up 90% ram, VM2 comes up automatically and now both have 45% utilisation.

App services
    - PaaS offering in Azure.
    - e.g. web apps - to host websites and web apps.
    - Web apps for containers
    - Api Apps.

Advantages of Containerization using Kubernetes/Docker
    - Managed Application Dependencies: dependencies included in container
    - Less Overhead: in compare to VM.
    - Increased Portability: can be deployed and used in any OS/Hardware.
    - Efficiency: Scaling and patching.
    - Consistency: always same.

