from airflow import DAG
from airflow.operators.bash import BashOperator # type: ignore
from datetime import datetime

with DAG(
    dag_id='weather_data_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    collect = BashOperator(
        task_id='collect_data',
        bash_command='python /opt/airflow/scripts/collect_data.py',
        dag=dag,
    )

    preprocess = BashOperator(
        task_id='preprocess_data',
        bash_command='python /opt/airflow/scripts/preprocess_data.py',
        dag=dag,
    )

    collect >> preprocess  # Removed 'train' unless it's added back
