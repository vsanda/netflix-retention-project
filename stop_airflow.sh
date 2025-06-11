#!/bin/bash

echo "Stopping Airflow webserver and scheduler..."

pkill -f "airflow webserver"
pkill -f "airflow scheduler"

echo "All Airflow processes stopped."
