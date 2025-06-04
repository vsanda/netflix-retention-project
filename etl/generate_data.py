# etl/generate_data.py

import pandas as pd
import random
from datetime import datetime, timedelta
import os

# Ensure output directory exists
os.makedirs("data/raw", exist_ok=True)

# Simulate dummy users and videos
user_ids = [f"user_{i}" for i in range(1, 51)]
video_ids = [f"video_{i}" for i in range(1, 21)]

records = []
base_date = datetime(2024, 1, 1)

for user in user_ids:
    for _ in range(random.randint(5, 20)):  # # of views
        watch_date = base_date + timedelta(days=random.randint(0, 180))
        records.append({
            "user_id": user,
            "video_id": random.choice(video_ids),
            "watch_time": random.randint(1, 120),  # minutes
            "date_watched": watch_date.date()
        })

# Save to CSV
df = pd.DataFrame(records)
df.to_csv("data/raw/viewing_history.csv", index=False)

print("✅ viewing_history.csv generated.")
