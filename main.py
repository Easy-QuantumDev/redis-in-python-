import redis

r = redis.Redis("127.0.0.1",7000,decode_responses=True)




        
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



# ////////// SORTED SET //////////////////////

# r.zadd("leaderboard",{
#     "mohammadreza":2000,
#     "alireza":3000
# })


# print(r.zrange("leaderboard",0,-1))

# print(r.zrevrange("leaderboard",0,-1,withscores=True))



# r.zincrby("leaderboard",2000,"mohammadreza")

# print(r.zrange("leaderboard",0,-1,withscores=True))

# print(r.zrevrange("leaderboard",0,-1,withscores=True))


# print(r.zscore("leaderboard","mohammadreza"))

# print(r.zrank("leaderboard","mohammadreza"))

# //////////////////////////////////////////////// key management /////////////////////////////////

# r.set("product:1","iphone18")

# print(r.type("user:1")) 
# print(r.type("product:1"))

 
# print(r.exists("user:1"))
# print(r.exists("user:10"))

# r.rename("product:1","phone:1")
# phone_1=r.get("phone:1")
# print(phone_1)

# print("////////////////////////////////// find key with keys() /////////////////////////")
# print(r.keys('*'))


# print("////////////////////////////////// find key with scan /////////////////////////")
# for key in r.scan_iter():
#     print(key)

# print("////////////////////////////////// find key with scan with filter(match) /////////////////////////")
# for key in r.scan_iter(match="users:*"):
#     print(key)





# print("////////////////////////////////// pipeline /////////////////////////")
# pipe = r.pipeline()
# pipe.set("user:1","mohammad")
# pipe.set("user:2","alireza")
# pipe.set("user:3","ali")
# pipe.set("user:4","mohammadreza")
# pipe.set("user:5","amir")
# pipe.get("user:1")
# pipe.get("user:2")
# pipe.get("user:3")
# pipe.get("user:4")
# pipe.get("user:5")
# result = pipe.execute()
# print(result)





# print("////////////////////////////////// Transaction /////////////////////////")

# r.incrby("balance",1000)

# with r.pipeline(transaction=True) as pipe:
    
#     pipe.watch("balance")
#     balance = int(pipe.get("balance"))
#     if balance >=1000:
#         pipe.multi()
#         pipe.decrby("balance",1000)
#         pipe.execute()
        
        
        
# print("////////////////////////////////// pub/sub /////////////////////////")