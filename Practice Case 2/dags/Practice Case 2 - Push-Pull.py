from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime
import json
from typing import Dict
import requests
import logging

# URL for getting ethereum price
API = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true"

# Getting response from the URL
def _extract_ethereum_price():
    return requests.get(API).json()['ethereum']

# Getting the value in the .json dictionary
def _process_data(ti):
    response = ti.xcom_pull(task_ids='_extract_ethereum_price')
    logging.info(response)
    processed_data = {'usd': response['usd'], 'change': response['usd_24h_change']}
    ti.xcom_push(key='processed_data', value=processed_data)

# Pulling the value of ethereum price
def _store_data(ti):
    data = ti.xcom_pull(task_ids='process_data', key='processed_data')
    logging.info(f"Store: {data['usd']} with change {data['change']}")

# Creating DAG object
with DAG('iykra_dag', schedule_interval='@daily', start_date=datetime(2022, 9, 22), catchup=False) as dag:
    
    _extract_ethereum_price = PythonOperator(
        task_id='_extract_ethereum_price',
        python_callable=_extract_ethereum_price
    )

    process_data = PythonOperator(
        task_id='process_data',
        python_callable=_process_data
    )

    store_data = PythonOperator(
        task_id='store_data',
        python_callable=_store_data
    )

    _extract_ethereum_price >> process_data >> store_data