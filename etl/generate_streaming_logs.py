# etl/generate_streaming_logs.py
from faker import Faker
import random, json
from datetime import datetime

fake = Faker()
EVENT_TYPES = ["play", "pause", "seek", "stop", "device_change"]
DEVICES = ["web", "mobile", "tablet", "smart_tv"]

def generate_event(user_id, content_id):
    return {
        "user_id": user_id,
        "content_id": content_id,
        "event_type": random.choice(EVENT_TYPES),
        "position": round(random.uniform(0, 5400), 1),  # seconds
        "device_type": random.choice(DEVICES),
        "timestamp": datetime.utcnow().isoformat()
    }

with open("data/raw/streaming_logs.json", "w") as f:
    for _ in range(10000):
        event = generate_event(fake.uuid4(), fake.uuid4())
        f.write(json.dumps(event) + "\n")
