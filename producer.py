import redis
r = redis.Redis('127.0.0.1',7000,decode_responses=True)
r.xadd('orders',{"name":"mohammadreza","age":22})
print('message added')
