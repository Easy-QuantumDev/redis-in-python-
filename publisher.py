import redis
r = redis.Redis('127.0.0.1',7000,decode_responses=True)
result  = r.publish("notification","hello from redis")
print(result) 