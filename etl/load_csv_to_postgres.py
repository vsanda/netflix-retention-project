import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_csv_to_postgres():
    user = os.getenv("PG_USER")
    pw   = os.getenv("PG_PASS")
    db   = os.getenv("PG_DB")

    engine = create_engine(f"postgresql://{user}:{pw}@localhost/{db}")

    # Load users.csv
    users = pd.read_csv("data/raw/users.csv")
    users.to_sql("users", engine, index=False, if_exists="append")

    # Load videos.csv
    videos = pd.read_csv("data/raw/videos.csv")
    videos.to_sql("videos", engine, index=False, if_exists="append")

    # Load viewing_history.csv
    viewing_history = pd.read_csv("data/raw/viewing_history.csv")
    viewing_history.to_sql("viewing_history", engine, index=False, if_exists="append")

    # Load subscriptions.csv
    subscriptions = pd.read_csv("data/raw/subscriptions.csv")
    subscriptions.to_sql("subscriptions", engine, index=False, if_exists="append")

    # Load support_tickets.csv
    support_tickets = pd.read_csv("data/raw/support_tickets.csv")
    support_tickets.to_sql("support_tickets", engine, index=False, if_exists="append")

    # Load churn_labels.csv
    churn_labels = pd.read_csv("data/raw/churn_labels.csv")
    churn_labels.to_sql("churn_labels", engine, index=False, if_exists="append")
    print("Data loaded successfully into PostgreSQL database.")

if __name__ == "__main__":
    load_csv_to_postgres()