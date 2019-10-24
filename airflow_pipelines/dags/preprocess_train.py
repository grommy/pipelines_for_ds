"""
The example of preprocessing - train pipeline

One of the problem of the workflow steps is how to pass files between the steps. See the
discussion under the link below
https://stackoverflow.com/questions/48755948/sharing-large-intermediate-state-between-airflow-tasks

Possible solution is to use cloud storage
"""
from datetime import timedelta

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

dag = DAG("some_id")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(1),
    'email': ['airflow@example.com'],
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    'dag': dag,
    # 'sla': timedelta(hours=2),
    'execution_timeout': timedelta(seconds=10),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'trigger_rule': u'all_success'
}

dag = DAG(
    'preprocessin-train-pipeline',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(minutes=10),
)

# [START howto_operator_bash]
preprocessing = BashOperator(
    task_id='preprocessing',
    bash_command='cd /Users/nickkon/projects/2021.AI/grace-enterprise-demo && '
                 'echo "\n Running preprocessing \n" && '
                 'python airflow_pipelines/src/preprocessing.py',
    dag=dag,
)
# [END howto_operator_bash]


training = BashOperator(
    task_id='train',
    bash_command='cd /Users/nickkon/projects/2021.AI/grace-enterprise-demo && '
                 'echo "\n Running training \n" && '
                 'python airflow_pipelines/src/train.py',
    dag=dag,
)


training >> preprocessing

if __name__ == "__main__":
    dag.cli()


