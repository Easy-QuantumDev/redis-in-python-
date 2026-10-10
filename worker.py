import redis
r = redis.Redis("127.0.0.1",7000,decode_responses=True)
while True:
    messages = r.xreadgroup("orders_workers",consumername='worker-1',streams={"orders":">"},count=1,block=5000)
    if not messages:
        continue
    for stream_name ,stream_messages in messages:
        for message_id , data in stream_messages:
            print("Stream:",stream_name) 
            print("ID:",message_id) 
            print("Data:",data) 
            result = r.xack("orders","orders_workers",message_id)
            