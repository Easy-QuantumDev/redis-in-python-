import redis

r = redis.Redis(
    "127.0.0.1",
    7000,
    decode_responses=True
)

messages = r.xpending_range(
    "orders",
    "orders_workers",
    min="-",
    max="+",
    count=10
)

for message in messages:
    print("ID:", message["message_id"])
    print("Consumer:", message["consumer"])
    print("Idle time:", message["time_since_delivered"], "ms")
    print("Delivery count:", message["times_delivered"])
    print("-" * 30)