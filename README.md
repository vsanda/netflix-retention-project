# 🎬 Netflix Retention Project

This is a personal data engineering project where I’m modeling customer retention for a fictional streaming platform (basically, Netflix). The goal is to build something end-to-end for ingestion, transformation, and analysis using tools outside of Amazon I’d actually use in a real job.

Right now, my focus is on building solid dbt models and running some retention metrics. Eventually I’ll wire in orchestration (Airflow) and maybe explore ML features around churn.

---

## 🧠 What This Project Covers

- Ingesting mock user + event data
- Cleaning and modeling with dbt
- Snapshots + historical tracking
- Building features like churn risk, active days, cohort views
- Light exploration in notebooks (mostly for sanity checks)

---

## 🧰 Tools I’m Using

| Purpose        | Tools                         |
|----------------|-------------------------------|
| Ingestion      | Python (custom scripts)       |
| Transform      | dbt (with Postgres for now)   |
| Orchestration  | Might add Airflow later       |
| Storage        | Postgres, CSVs, local files   |
| Analysis       | Jupyter, SQL, notebooks       |
| Testing        | dbt schema + unit tests       |

---

## 📁 Repo Layout (will evolve)

```plaintext
.
├── etl/            # ingestion scripts
├── dbt/            # models, snapshots, tests
├── data/           # mock source data
├── analytics/      # notebooks & scratchpad stuff
└── README.md
