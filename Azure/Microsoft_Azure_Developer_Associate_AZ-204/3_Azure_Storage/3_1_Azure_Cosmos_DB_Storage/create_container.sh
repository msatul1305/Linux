# Create a SQL API cosmos db account
az cosmosdb create --name "account_name" --resource-group "rgroupname"

# create a SQL database
az cosmosdb sql database create --account-name "account_name" --name "db_name"

# create sql database container(table)
az cosmosdb sql container create --resource-group "rgroupname" --account-name "account_name" --database-name "db_name" --name "container_name" --partition-key-path "/employeeid"

# Insert items into container

# Query Items from container

