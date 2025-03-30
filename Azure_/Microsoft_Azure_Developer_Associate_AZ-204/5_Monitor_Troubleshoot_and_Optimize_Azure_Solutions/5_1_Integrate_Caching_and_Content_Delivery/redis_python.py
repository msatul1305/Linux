# pip install redis
import redis
# Replace 'your-redis-host-name' and 'your-access-key' with the actual values for your Azure Cache for Redis instance.
redis_host = 'your-redis-host-name.redis.cache.windows.net'
redis_port = 6380
redis_password = 'your-access-key'

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, ssl=True)

# Write a key-value pair to the Redis cache
redis_client.set('my_key', 'my_value')

# Read the value of a key from the Redis cache
value = redis_client.get('my_key')
print(value)  # This will print the value of the key 'my_key'
