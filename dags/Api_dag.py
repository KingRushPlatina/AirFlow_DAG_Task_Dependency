import json;
from datetime import datetime
from pickle import FALSE
from airflow.models import DAG
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator



with DAG(
    dag_id='api_dag',
    description='Http dag DAG',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False
) 
as dag:
  task_is_api_active = HttpSensor(
    task_id='is_api_active',
    http_conn_id='api_dag',
    endpoint='module/'
  )
  #to test the call from the terminal
  #airflow tasks test api_dag is_api_active 2024-1-1