from datetime import timedelta, datetime
from airflow import models
from airflow.operators.bash_operator import BashOperator

yesterday = datetime(2021, 6, 21)

default_dag_args = {
'owner': 'José Otón',
'start_date': yesterday
}

with models.DAG(
dag_id='1rst_exercise',
description='Hello World =)',
schedule_interval=timedelta(days=1),
default_args=default_dag_args) as dag:

    helloOp = BashOperator(
        task_id='hello_world',
        bash_command='echo "1rst Hello World!"'
    )

    helloOp2 = BashOperator(
        task_id='hello_world_2',
        bash_command='echo "2nd Hello World!"'
    )

helloOp >> helloOp2