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

Kubernetes(K8s)
    - Open Source container/Orchestration system - By Google
    - Orchestration makes sure that containers are configured correctly to work together.
    - For Automation of app deployment, Scaling and Management.
    - Pods and clusters
    - A no. of pods make a cluster.

Advantages of Containerization using Kubernetes/Docker
    - Managed Application Dependencies: dependencies included in container
    - Less Overhead: in compare to VM.
    - Increased Portability: can be deployed and used in any OS/Hardware.
    - Efficiency: Scaling and patching.
    - Consistency: always same.

Azure container registry(ACR) - keeps track of all containers

- Serverless and Functions
- Networking
  - Virtual Network: (VNet) -> eg. 172.169.2.0 to 172.169.2.255
      - Subnets: eg. 172.169.2.0 to 172.169.2.100 etc. 
    - Helps in - 
      -  Resource grouping: group together resources on same subnet.
      - Address allocation: efficiently allocate address.
      - Subnet security: secure group of resources together.
      - Scaling: adding more VNets or address if required
      - High availability: using load balancer, using VPN gateway to increase availability.
      - Isolation
  - Load Balancer
    - Inbound traffic from user sends data to -> Load balancer[Frontend] sends data to -> actual VM(VM1 vs VM2)[called 
      backend pool] sends data back to -> load balancer.  
    - Scenarios where load balancing is used:
      - Internet traffic management
      - Internal network traffic
      - port forwarding(Traffic forwarding to applications running on specific ports).
      - Outbound traffic
  - VPN gateway: for Hybrid cloud architecture. [VNet Gateways + VPN = VPN gateways]
    - used to send data/communicate from VM to on-premise server via public internet.
    - Gateway sits between VM and on-premise server.
      - Components of VPN gateway:
        - Its own public IP address.
        - Tunnel: secure connection with an encryption algorithm via which data will flow/communication will be made.
        - On-premise network with a complementary gateway to receive the data. -> called [Site-to-Site connection]
        - [Multisite connection]: 1 vpn gateway connecting to >1 on-premise network connecting to it.
  - Application gateway
    - Load balancer + cloud = app gateway
    - http requests can be routed based on URI paths(URL) or host headers - header of the segment/packet sent with the 
    request.
      - Benefits of application gateway:
        - Scaling
        - Encryption
        - Zone redundancy: span multiple availability zones and improve fault resilience.
        - Multi-site hosting: use same application gateway for up to 100 websites.
  - CDN: Content Delivery Network
    - CDN keeps a copy of websites and routes each user's request to the nearest location(called edge nodes).
    - It updates th web data using caching and data invalidation.  i.e. each data has expiry - data is copied from 
      master again on expiry/if data has changed.
    - Benefits:
      - Better performance
      - Scaling
      - Distribution
  - ExpressRoute
    - Superfast private connection to azure
    - For companies with hybrid on-premise and azure connection. 
    - Private, secure, low-latency connection
    - Don't go over internet.

IPv4
    - CIDR notation: 10.0.0.0/16 means it will create 2^16 addresses:
        - i.e. 10.0.0.0 to 10.0.255.255
    - subnet mask:
        - 10.0.0.0/24 will give us 2^8 = 256 addresses.


Storage on Azure: Storage account = Unique Azure Namespace - each storage has its own web address.
        e.g. acloudguru.azure.com 
    - Blob
        - Binary large object - anything with bits and bytes.
        - Images, Videos, audio, logs, archives, data store - backup, restore, disaster recovery, etc.
        - Types:
            - Block blob: text and binary data upto 4.7TB. made up of individually managed blocks of data.
            - Append block blobs: block blobs optimized for append operations like logging.
            - Page blobs: Any type of data upto 8TB.
        Pricing:
            - Hot: Low access time, high cost
            - Cool: higher access time, lower cost
            - Archive: highest access time, the lowest cost.
    - Disk
        - HDD: backups, low cost.
        - Standard SSD: standard for production. higher reliability, scalability and lower latency over HDD.
        - Premium SSD: Super fast, high performance, low latency. used for critical workloads.
        - Ultra Disks: for demanding, data-intensive workloads. (upto 64TB)
    - File Storage
        - Benefits:
            - Sharing
            - Managed
            - Resilient
    - Archive
        - Requirement
        - low price
        - durable, encrypted, stable.
        - free up premium on-premise storage.
        - secure
        - blob
    - Storage redundancy
        - 
    - Moving data
    - Additional Migration options
    - Premium performance options