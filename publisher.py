# send message with a channel with r.publish
import redis
r = redis.Redis('127.0.0.1',7000,decode_responses=True)
# result = r.publish("notification",'hello from redis')
# print(result)

# /////////////////////////or

result = r.publish("notification:user","hello form user channel")
result2 = r.publish("notification:product","hello form product channel")
result3 = r.publish("notification:sale","hello form sale channel")
result4 = r.publish("notification:buy","hello form buy channel")
print(result)
print(result2)
print(result3)
print(result4)