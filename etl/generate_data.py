import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Parameters
NUM_USERS = 1000
NUM_VIDEOS = 200
NUM_TICKETS = 300

# 1. Generate users
users = []
for i in range(NUM_USERS):
    users.append({
        "user_id": i + 1,
        "signup_date": fake.date_between(start_date='-1y', end_date='today'),
        "country": fake.country(),
        "device_type": random.choice(["mobile", "tablet", "smart_tv", "web"]),
        "plan_type": random.choice(["basic", "standard", "premium"])
    })
users_df = pd.DataFrame(users)
users_df.to_csv("data/raw/users.csv", index=False)

# 2. Generate videos
videos = []
for i in range(NUM_VIDEOS):
    videos.append({
        "video_id": i + 1,
        "title": fake.sentence(nb_words=3),
        "genre": random.choice(["drama", "comedy", "sci-fi", "action", "documentary"]),
        "duration": random.randint(30, 180),
        "release_year": random.randint(2000, 2024)
    })
videos_df = pd.DataFrame(videos)
videos_df.to_csv("data/raw/videos.csv", index=False)

# 3. Generate viewing history
viewing = []
for _ in range(NUM_USERS * 5):
    viewing.append({
        "user_id": random.randint(1, NUM_USERS),
        "video_id": random.randint(1, NUM_VIDEOS),
        "watch_time": random.randint(1, 180),
        "date_watched": fake.date_between(start_date='-6m', end_date='today')
    })
view_df = pd.DataFrame(viewing)
view_df.to_csv("data/raw/viewing_history.csv", index=False)

# 4. Generate subscriptions
subscriptions = []
for user in users:
    start = user["signup_date"]
    end = start + timedelta(days=random.randint(30, 365))
    subscriptions.append({
        "user_id": user["user_id"],
        "plan_type": user["plan_type"],
        "start_date": start,
        "end_date": end,
        "is_active": end >= datetime.today().date()
    })
subs_df = pd.DataFrame(subscriptions)
subs_df.to_csv("data/raw/subscriptions.csv", index=False)

# 5. Generate support tickets
tickets = []
for _ in range(NUM_TICKETS):
    user_id = random.randint(1, NUM_USERS)
    ticket_date = fake.date_between(start_date='-3m', end_date='today')
    resolved = random.choice([True, False])
    tickets.append({
        "user_id": user_id,
        "issue_type": random.choice(["billing", "technical", "account", "content"]),
        "ticket_date": ticket_date,
        "resolved": resolved
    })
tickets_df = pd.DataFrame(tickets)
tickets_df.to_csv("data/raw/support_tickets.csv", index=False)

# 6. Generate churn labels
churn = []
for user in users:
    churned = random.choice([True, False])
    churn_date = fake.date_between(start_date='-3m', end_date='today') if churned else None
    churn.append({
        "user_id": user["user_id"],
        "churned": churned,
        "churn_date": churn_date
    })
churn_df = pd.DataFrame(churn)
churn_df.to_csv("data/raw/churn_labels.csv", index=False)

print("Data generation complete. Files saved in 'data/raw/' directory.")
print("Users, videos, viewing history, subscriptions, support tickets, and churn labels generated successfully.")
print("You can now proceed with the ETL pipeline to process this data.")