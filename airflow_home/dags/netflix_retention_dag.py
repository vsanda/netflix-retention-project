import os
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# 1) Compute file-system paths relative to this DAG file
dag_file_dir = os.path.dirname(__file__)                # .../airflow_home/dags
airflow_home  = os.path.dirname(dag_file_dir)           # .../airflow_home
project_root  = os.path.dirname(airflow_home)           # .../netflix-retention-project

default_args = {
    'owner': 'airflow'
}

with DAG(
    dag_id='netflix_retention_dag',
    default_args=default_args,
    schedule_interval='@daily',
    start_date=days_ago(1),
    catchup=False
) as dag:

    # 2) Print working directory for debugging, then run the script
    generate_data = BashOperator(
        task_id='generate_mock_data',
        bash_command=(
            f'echo "PWD=$(pwd)"; ls -la; '
            f'cd {project_root} && '
            'python etl/generate_data.py'
        )
    )

    load_to_postgres = BashOperator(
        task_id='load_csv_to_postgres',
        bash_command=(
            f'echo "PWD=$(pwd)"; ls -la; '
            f'cd {project_root} && '
            'python etl/load_csv_to_postgres.py'
        )
    )

    dbt_snapshot = BashOperator(
        task_id='run_dbt_snapshot',
        bash_command=(
            f'echo "PWD=$(pwd)"; ls -la; '
            f'cd {project_root}/dbt && '
            'dbt snapshot'
        )
    )

    dbt_run = BashOperator(
        task_id='run_dbt_run',
        bash_command=(
            f'echo "PWD=$(pwd)"; ls -la; '
            f'cd {project_root}/dbt && '
            'dbt run'
        )
    )

    generate_data >> load_to_postgres >> dbt_snapshot >> dbt_run


