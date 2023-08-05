# pip install redis
import redis
# Replace 'your-redis-host-name' and 'your-access-key' with the actual values for your Azure Cache for Redis instance.
redis_host = 'your-redis-host-name.redis.cache.windows.net'
redis_port = 6380
redis_password = 'your-access-key'

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, ssl=True)

# Reload Redis data from disk (RDB snapshot):
# Trigger the background rewrite of the AOF file (reload data from disk)
redis_client.bgrewriteaof()
# This command will trigger a background process to rewrite the append-only file (AOF) on disk.
# The AOF contains all the commands to recreate the data in Redis.
# By triggering the rewrite, you effectively reload the data into Redis.

# Purge all cache content (flush all data):
redis_client.flushall()
