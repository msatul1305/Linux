Azure Cloud

1. Why Cloud?
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

2. CLI
   1. az create vm - To create a new VM 


3. Using PowerShell
Cmdlet - Small lightweight commands/scripts used to do some specific functions/tasks.
   1. New-AzVm - To create a new VM

4. ARM - Azure Resource manager
ARM Benefits
    - Group resource handling: deploy, manage and monitor resources as a group.
    - Consistency: consistent result of deployment.
    - Dependencies: define independency.
    - Access Control: built-in user right control.
    - Tagging: tag resources
    - Billing: bill for group of resources with similar tag.

5. Cloud Computing - On demand availability of computer resources split into 3 main categories:
    1. Compute
    2. Networking
    3. Storage

6. Cloud Economics - pricing
    Return on Investments(ROI)
    1. Capital Expenditure(Capex) - Fixed assets like land, building, equipment.
    2. Operational Expenditure(Opex) - ongoing day-to-day costs, annual costs.
    - Hourly pricing
    - consumption
        - per execution of function
        - per second
        - Combination

7. As a Service
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

8. Identifying Cloud Service Models - IaaS vs PaaS vs SaaS
    - IaaS: Org have complete control of infrastructure. e.g. VM, VNet, Storage
    - PaaS: Virtualized resources can cbe scaled up or down. e.g. App Services, Azure CDN, Cosmos DB
    - Saas: Remote server central location - e.g. Microsoft 365


9. Types of Cloud
    - Private - Similar to on premise where owning team is responsible for staffing, maintenance.
    - Public - Accessible anywhere across the globe. e.g. Azure, AWS, GCP.
    - Hybrid - Public + Private - For regulatory reasons.

10. Scale set
    - set of identical VMs.
    - Activated and deactivated as needed. - auto-scalability and load balancing. 
    - e.g. if VM1 takes up 90% ram, VM2 comes up automatically and now both have 45% utilisation.

11. App services
    - PaaS offering in Azure.
    - e.g. web apps - to host websites and web apps.
    - Web apps for containers
    - Api Apps.

12. Kubernetes(K8s)
    - Open Source container/Orchestration system - By Google
    - Orchestration makes sure that containers are configured correctly to work together.
    - For Automation of app deployment, Scaling and Management.
    - Pods and clusters
    - A no. of pods make a cluster.

13. Advantages of Containerization using Kubernetes/Docker
    - Managed Application Dependencies: dependencies included in container
    - Less Overhead: in compare to VM.
    - Increased Portability: can be deployed and used in any OS/Hardware.
    - Efficiency: Scaling and patching.
    - Consistency: always same.

14. Azure container registry(ACR) - keeps track of all containers
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

15. IPv4
    - CIDR notation: 10.0.0.0/16 means it will create 2^16 addresses:
        - i.e. 10.0.0.0 to 10.0.255.255
    - subnet mask:
        - 10.0.0.0/24 will give us 2^8 = 256 addresses.


16. Storage on Azure: Storage account = Unique Azure Namespace - each storage has its own web address. e.g. acloudguru.azure.com
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
        - If one copy fails/inaccessible, data is still available as another copy in other place.
        - Minimum 3 copies in primary region, 3 copies in secondary region(optional)
        - Multiple redundancy options:
            - Single Region
                - LRS: Locally redundant storage
                    - 3 copies within a single location.(within 3 different racks)
                    - low cost
                    - protection against single disk failure
                    - doesn't protect zone/regional failure/unavailability/outage.
                - ZRS: Zone redundant storage
                    - spans across 3 zones within a region. (eg. Chennai-east, west, north)
                    - protects against zone outage
                    - no protection against region wide outage
            - Multiple region
                - GRS: Geo-redundant storage
                    - 3 copies in primary regional physical location(LRS) - (Chennai-east)
                    - 3 copies in secondary(paired) regional physical location(LRS) - (Mumbai-east)
                    - protects against primary region failure but no primary zone redundancy.
                - GZRS: Geo-Zone-redundant storage
                    - 3 copies in primary regional physical location(ZRS) - (Chennai-east, west, north)
                    - 3 copies in secondary(paired) regional physical location(LRS) - (Mumbai-east)
                    - protects against primary region failure but no primary zone redundancy.
      - Moving data
        - AzCopy: CLI
            - for blobs and azure file formats. 
            - azcopy cp "xyz.mp4"  "https://container-url"
        - Azure Storage Explorer:
            - GUI, use-friendly
        - Azure File Sync:
            - Synchronizes azure files with on-premise file servers.
            - local file server performance + cloud availability.
            - uses:
                - backup local file server
                - sync files between multiple on-premises locations
      - Additional Migration options
        - Azure data box: 
            - To transfer lots of data over internet.
                - copy data to physical data storage device(Data Box): Encrypted and Rugged.
                - Ship data box to/from Azure.
            - Use cases:    
                - initial bulk data migration
                - restore backed up data in disaster recovery scenario of on-premise data.
                - Data security: move secure data without going to internet.
        - Azure migrate: 
            - moving non-azure resources into azure
            - servers, applications, databases.
      - Premium performance options
        - storage SSDs
        - for high performance
        - less redundancy options.
        - Types:
          - Premium Block blobs: blob objects in blob containers.
            - for low latency blob storage workloads
            - e.g. AI and IOT analytics
            - LRS and ZRS redundancy only.
          - Premium Page blobs(IaaS disks):
            - unmanaged virtual disk.
            - LRS redundancy only.
          - Premium File blobs:
            - Azure files as storage type
              - for high performance enterprise (file server)applications
              - supports Server Message Block(SMB): Windows file share
              - and Network File System(NFS): Linux file share
              - LRS/ZRS only.

17. Databases:
    - Cosmos DB: Globally scaled, fully managed db, powerful and fast read and write.
    - Azure SQL
    - MySQL
    - PostgreSQL
    - Database Migration Services.