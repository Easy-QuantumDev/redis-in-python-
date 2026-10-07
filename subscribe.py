# making subscribe and channel

import redis

r = redis.Redis('127.0.0.1',7000,decode_responses=True)

pubsub = r.pubsub() #making pubsub

pubsub.psubscribe("notification:*")#channel

for message in pubsub.listen():#messages
    print(message)
    