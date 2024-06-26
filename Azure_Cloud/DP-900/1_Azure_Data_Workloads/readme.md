# Getting Started with Azure Data Workloads

- By Henry Been
  - Netherlands
  - Microsoft Azure
- Types of Data
  - Structured data
    - predefined schema
      - e.g. int for student ID, string for first and last name
    - tabular format
      - each table has primary key to uniquely identify each record
        - e.g. ID
      - Foreign key:
        - reference to the primary key in another table to establish relation between 2 tables
    - each row = record
      - adhere to description called
    - column = name and data type of records
    - each cell = field
    - e.g.
      - CRM(Customer Relations Management) Systems
      - ERP(Enterprise Resource Planning) Systems
      - Administrative systems
      - SQL
  - Unstructured data
    - NO predefined schema
    - NO notion of fields, labels or types
    - e.g
      - Video
      - Audio
      - Images
    - harder to process
    - processed using Machine Learning techniques
      - e.g.
        - video's transcript
        - analyze Images to identify faces and objects
  - Semi-structured data
    - NOT necessarily tabular
    - the shape of data can change with time
    - yet it has observable structure
    - e.g.
      - Log files: timestamp + info
      - data export formats like: XML, CSV, JSON etc.
- Types of databases
  - relational and non-relational databases
    - Relational databases
      - stores structured data in tables
      - transaction management system
      - scales vertically (e.g., adding 8GB ram instead of 4GB)
      - SQL: Structured Query Language
        - read, write data
        - declarative language
          - i.e., we don't write instructions on how to execute a query
          - we just describe the intended result
            - DB converts it into series of operations to execute
        - strict schema
          - describes tables, fields, field types, and relations between tables
          - specified at the time of creation
          - enforced on write
      - Examples:
        - Microsoft SQL Server
          - commercial—need to buy license 
          - High-performance system, 
          - integrated with Microsoft Azure Active Directory (AD)
          - PaaS (Platform as a service) version of this in Azure:
            - Azure SQL DB
        - MySQL
          - free, open-source SQL db
          - easy to install, manage, learn 
        - PostgreSQL
          - more features
          - more complex
        - SQL Server
        - MariaDB
    - Non-relational databases
      - data is not stored in tables but in collections or containers
      - dont enforce schema: schema-agnostic
      - used in IoT Apps, real-time analytics
      - scales horizontally (e.g., add another 4 gb ram parallel to exisiting)
      - collections store:
        - arbitrary snippets of data
          - like XML or JSON
      - Types of non-relational DBs
        - Table Storage
        - Blob Storage
        - File Storage
        - Cosmos DB
        - Document DB
          - stores small documents in XML or JSON
        - Wide-column stores
          - stores data in rows and columns but without a schema
          - each record can have different shape
        - Key-Value store
          - value stored inside locator keys
          - incredibly performant and scalable 
        - Graph databases
          - model specific problems
          - performance querying of specific problems
      - Examples
        - Redis
          - high performant
          - in-memory database
          - used for caching
          - implements key-value store
        - Cassandra
          - free to use, open source
          - wide-column store
          - highly distributed
          - highly distributed architecture
          - resistant to hardware failures
          - suitable for running on low-end cheap hardware
        - Azure CosmosDB
          - globally distributed
          - multi-model db
            - Document store
            - Graph DB
            - Key-Value store
          - available only on Azure
          - cloud native DB
- Data workloads
  - Transactional and analytical workloads
    - Transactional workloads
      - supports high volumes of reads and writes 
      - to support information systems
      - e.g. 
        - CRM-Customer Relationship Management
        - Tracking software
        - Record keeping
          - banking
          - grade keeping systems
        - ***OLTP***: Online Transactional Processing
          - respond fast(in milliseconds)
          - answers must be correct and complete
          - transaction
            - unsplittable update to db bound together and should be executed as a whole
              - e.g., transfer of money in the bank
                - withdrawal in one account
                - deposit in another
                - i.e., either both the transactions should be processed or neither
            - ***ACID properties***
              - A: Atomicity
                - all transactions should be atomic/unsplittable
                - either transaction is committed and all changes are saved
                - or transaction is aborted and no changes are saved
                - Solutions:?
              - C: Consistency
                - DB should be in a consistent state before and after the transaction
                  - i.e., all schema and relational requirements are met
                  - Solutions:?
              - I: Isolation
                - transactions should not run in parallel
                - i.e., one transaction should not see intermediate results of another uncommitted transaction
                - Solutions: Locking until dependent transaction is committed
              - D: Durability
                - changes should persist even if a database system fails/crashes
                - i.e., db should recover
                - Solutions:?
    - Analytical workloads
      - support queries for getting insights
      - or overview over large amounts of data for
        - KPIs
        - analysis
        - reports and 
        - Business Intelligence
    - less frequent queries but each query is data intensive
      - i.e., low number of reads but over large data
        - e.g.
          - Batch-based (warehousing)
            - data is queried after processing
            - called as ***OLAP***: Online Analytical Processing
              - data is not stored 
              - only analyzed as they come through, calculating the results needed
              - also called data warehouses as data can get huge
              - e.g., Azure Synapse—also called Azure SQL Data Warehouse(previously)
          - Streaming data
            - works based on continuous export of new and changed data 
            - from transactional system into query engine to answer queries on the fly
            - e.g.
              - Azure Stream Analytics
                - can receive new order records from any data source and
                - use that to update in near real-time result sets
                - can receive streams of data from the OLTP database
              - we need a messaging system in between Azure SQL DB and Stream Analytics
                - to get data
                - e.g.
                  - Azure Event Hubs
                    - high-performance messaging system 
                    - producer-consumer based
                    - can store and forward messages from multiple producers to multiple consumers
                  - i.e.
                    - Website -> Azure Event Hub -> Azure SQl DB, Stream Analytics
- OLTP vs OLAP
  - use different schemas to store the same data to optimize schema for type of query
  - separating both helps as:
    - analytical queries will not impact transactional workload by consuming too much resources
  - Issue:
    - we need to get/copy/move data from OLTP to OLAP
      - ETL tools are used
        - E: Extract
          - Extract data from one or more database
        - T: Transform
          - transform data from source(transactional) model to destination(analytical) model
        - L: Load
          - load to another DB
        - e.g. 
          - Azure Data Factory
            - built in support to run on a schedule
- Batch data vs streaming data
  - Batch data
    - data executes on a schedule
    - not always up to date
    - All data produced by ETL pipeline is stored in OLAP warehouse
    - data can be queried after loading
    - easy joining of datasets
      - combining many sources of data into a single data warehouse
    - cost efficient
  - Streaming data
    - executes near real-time answers to queries
    - stores only result, not any data
    - queries are predefined
      - new or different queries cannot be processed on data that has already gone through the engine
    - can process a massive amount of data
    - combining data sets is difficult
    - 
- services
- PowerBI
  - from Microsoft
  - for analyzing and visualizing data
  - Office 365 product
  - SaaS product
- Pipeline setup
  - Query source datasets
    - orders-table
      - import data from source
    - customers-table
      - import data from source-customers
  - Combine datasets
    - add age to order
      - inner join on order table and customer table
  - select columns
    - select age, order_amount
      - renaming add age to order to select age, order_amount with customer_id, order_amt, name and age
  - write output to target datasets
    - write-to-warehouse
      - export data to target_orderamountbyage
- Further references:
  - Building your first data pipeline in azure data factory
    - by Emillio Melo
  - Building your first Power BI report
    - Stacia Misner Varga
  - Understanding Azure Stream Analytics
    - Alan Smith
