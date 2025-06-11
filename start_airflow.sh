#!/bin/bash

# Activate virtualenv
source venv/bin/activate

# Load .env file
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Set AIRFLOW_HOME if not already set
export AIRFLOW_HOME=${AIRFLOW_HOME:-$(pwd)/airflow_home}

# Initialize Airflow (safe to re-run)
airflow db init

# Start webserver in background if not running
if ! pgrep -f "airflow webserver" > /dev/null; then
  echo "Starting Airflow webserver at http://localhost:8080 ..."
  airflow webserver --port 8080 > "$AIRFLOW_HOME/webserver.log" 2>&1 &
else
  echo "Airflow webserver already running."
fi

# Start scheduler if not running
if ! pgrep -f "airflow scheduler" > /dev/null; then
  echo "Starting Airflow scheduler ..."
  airflow scheduler > "$AIRFLOW_HOME/scheduler.log" 2>&1 &
else
  echo "Airflow scheduler already running."
fi
