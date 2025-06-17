# etl/load_streaming_logs_postgres.py
import json
import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("PG_HOST"),
    dbname=os.getenv("PG_DB"),
    user=os.getenv("PG_USER"),
    password=os.getenv("PG_PASSWORD")
)

cur = conn.cursor()

with open("data/raw/streaming_logs.json") as f:
    events = [
        (
            e["user_id"], e["content_id"], e["event_type"],
            e["position"], e["device_type"], e["timestamp"]
        )
        for e in map(json.loads, f)
    ]

execute_values(
    cur,
    """
    INSERT INTO streaming_logs (user_id, content_id, event_type, position, device_type, timestamp)
    VALUES %s
    """,
    events
)

conn.commit()
cur.close()
conn.close()
print("Streaming logs loaded successfully into PostgreSQL database.")
