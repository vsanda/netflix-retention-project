import pandas as pd
from faker import Faker
import random
from datetime import datetime, date, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)

# Parameters
NUM_USERS = 1000
NUM_VIDEOS = 200
NUM_TICKETS = 300

# 1. Generate users with timestamps
users = []
for i in range(NUM_USERS):
    signup = fake.date_between(start_date='-1y', end_date='today')
    created_at = signup - timedelta(days=random.randint(0, 30)) 
    updated_at = created_at + timedelta(days=random.randint(0, 30)) # Account creation date
    users.append({
        "user_id": i + 1,
        "signup_date": fake.date_between(start_date='-1y', end_date='today'),
        "country": fake.country(),
        "device_type": random.choice(["mobile", "tablet", "smart_tv", "web"]),
        "plan_type": random.choice(["basic", "standard", "premium"]),
        "created_at": created_at,
        "updated_at": updated_at
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

# 3. Generate viewing history (append-only with created_at)
viewing = []
for _ in range(NUM_USERS * 5):
    date_watched = fake.date_between(start_date='-6m', end_date='today')
    created_at = date_watched + timedelta(hours=random.randint(0, 48))
    viewing.append({
        "user_id": random.randint(1, NUM_USERS),
        "video_id": random.randint(1, NUM_VIDEOS),
        "watch_time": random.randint(1, 180),
        "date_watched": date_watched,
        "created_at": created_at
    })
view_df = pd.DataFrame(viewing)
view_df.to_csv("data/raw/viewing_history.csv", index=False)

# 4. Generate subscriptions (versioned for SCD2)
subscriptions = []
for user in users:
    user_id = user["user_id"]
    start = user["signup_date"]
    num_versions = random.randint(1, 2)  # some users get upgraded
    for v in range(num_versions):
        plan_type = random.choice(["basic", "standard", "premium"])
        version_start = start + timedelta(days=30 * v)
        version_end = version_start + timedelta(days=30)
        is_current = v == num_versions - 1
        subscriptions.append({
            "user_id": user_id,
            "plan_type": plan_type,
            "start_date": version_start,
            "end_date": None if is_current else version_end,
            "is_active": is_current,
            "created_at": version_start,
            "updated_at": version_start + timedelta(days=1)   
        })
subs_df = pd.DataFrame(subscriptions)
subs_df.to_csv("data/raw/subscriptions.csv", index=False)

# 5. Generate support tickets with updates for snapshot testing
tickets = []
for ticket_id in range(NUM_TICKETS):
    user_id = random.randint(1, NUM_USERS)
    ticket_date = fake.date_between(start_date='-90d', end_date='-2d')
    created_at = ticket_date + timedelta(hours=random.randint(0, 12))
    updated_at = created_at + timedelta(days=random.choice([0, 1, 7, 14]))
    resolved = random.choice([True, False])
    
    tickets.append({
        "ticket_id": ticket_id + 1,
        "user_id": user_id,
        "issue_type": random.choice(["billing", "technical", "account", "content"]),
        "ticket_date": ticket_date,
        "resolved": resolved,
        "created_at": created_at,
        "updated_at": updated_at
    })
tickets_df = pd.DataFrame(tickets)
tickets_df.to_csv("data/raw/support_tickets.csv", index=False)


# 6. Generate churn labels
churn = []
for user in users:
    user_id = user["user_id"]
    signup_date = user["signup_date"]

    churned = random.choice([True, False])
    if churned:
        churn_date = fake.date_between(start_date=signup_date, end_date='today')
    else:
        churn_date = None

    churn.append({
        "user_id": user_id,
        "churned": churned,
        "churn_date": churn_date,
        "created_at": datetime.now()
    })

churn_df = pd.DataFrame(churn)
churn_df.to_csv("data/raw/churn_labels.csv", index=False)


print("Data generation complete. Files saved in 'data/raw/' directory.")
print("Users, videos, viewing history, subscriptions, support tickets, and churn labels generated successfully.")
print("You can now proceed with the ETL pipeline to process this data.")


