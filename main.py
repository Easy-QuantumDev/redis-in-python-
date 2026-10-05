import redis

r = redis.Redis("127.0.0.1",7000,decode_responses=True)


r.zadd("leaderboard ",{
    'mohammadreza':1900,
    "mehrnaz":2000
})







#/////////////////////////////////document
# 
# import redis
# r = redis.Redis(
#     host='localhost',
#     port=6379,
#     decode_responses = True
    
# )
# print(r.ping())
# import redis
# r = redis.Redis(host='127.0.0.1',port=7000,decode_responses=True)
# r.set("name","mohammadreza")


# name = r.get("name")

# print(name)

# print(r.exists("name"))







# r.delete("name")
# print(r.get("name"))
# print(r.exists("name"))


# if r.exists("name"):
#     print("key is exists")
# else:
#     print("key is not exists\n")    


# r.set("views",0)
# print(r.get("views"))


# r.incr("views")
# print(r.get("views"))



# r.set("otp",'483921',ex=60)

# ////////////////////////////////////////////////SET///////////////
# import redis 
# r = redis.Redis("127.0.0.1",7000,decode_responses=True)
# r.set("user:1","mohammadreza")
# user_1= r.get("user:1")
# print(user_1)
# print(r.keys('user:*'))
# print(r.exists("user:1"))
# print(r.ttl('user:1'))


# //////////////////////HASH////////////////////////////

# r.delete("user:1")
# r.hset("user:1",'name',"mohammadreza")
# r.hset("user:1",'age',"22")
# r.hset("user:1",'city',"mashhad")
# r.hset("user:2",mapping={
#     "name":"alireza",
#     "age":"26",
#     "city":"tehran"
# })
# name = r.hget("user:1",'name')
# age = r.hget("user:1",'age')
# city = r.hget("user:1",'city')
# print(name)
# print(age)
# print(city)

# print(r.hgetall("user:1"))

# print(r.hgetall("user:2"))



# r.hdel("user:1","age")
# print(r.hgetall("user:1"))
# //////////////////////////////////// LIST /////////////////

# r.lpush("task:queue","send email")
# r.lpush("task:queue","generate report")
# r.lpush("task:queue","send sms")

# print(r.lrange("task:queue",0,-1))

# task = r.lpop("task:queue")
# print(task)

# ////////////////////////////////SET////////////////
# r.delete('online_users')
# r.sadd("online_users","user:2")
# r.sadd("online_users","user:3")
# r.sadd("iranian_food","kebab","koofteh")
# r.sadd("meat","kebab","pizza")
# print(r.smembers('online_users'))
# print(r.sismember('online_users',"user:1"))
# print(r.sinter('iranian_food','meat'))
# print(r.scard("online_users"))
# r.srem("online_users","user:2")
# print(r.scard("online_users"))