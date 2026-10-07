import redis
r = redis.Redis('127.0.0.1',7000,decode_responses=True)
last_id = '0'
while True:
    messages =r.xread({
        'orders':last_id
    },
            count=10,
            block=1000        
            )
    if messages:
        for stream_name , stream_message in messages:
            
            for stream_id ,data in stream_message:
                print(f'stream id {stream_id} and data : {data}')
                last_id = stream_id
    