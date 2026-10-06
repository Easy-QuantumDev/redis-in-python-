import redis
r = redis.Redis('127.0.0.1',7000,decode_responses=True)
pubsub  = r.pubsub()
pubsub.subscribe("notification")
print("waiting for message")
for message in pubsub.listen():
    print(f'message  : {message}')