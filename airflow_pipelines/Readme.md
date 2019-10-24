# Examples of the Apache Airflow pipelines

## To run, you must spin up airflow server:
See [installation instructions](https://airflow.apache.org/installation.html)
* install `pip install apache-airflow==1.10.5`
* modify the `airflow.cfg`. Go through file and setup correct absolute path which applies to your machine.
* setup the config `export AIRFLOW_CONFIG=<PATH_TO_THE_ROOT>/grace-enterprise-demo/airflow_pipelines/airflow.cfg`
* initialize db `airflow initdb`
* spin up the scheduler `airflow scheduler`
* spin up the webserver `airflow webserver -p 8080`


### Useful links:

1. https://airflow.apache.org/concepts.html
1. http://bytepawn.com/luigi-airflow-pinball.html#luigi-airflow-pinball
1. https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753
1. https://github.com/mumoshu/kube-airflow
1. https://www.techatbloomberg.com/blog/airflow-on-kubernetes/
1. https://www.sicara.ai/blog/2019-04-08-apache-airflow-celery-workers
1. https://medium.com/swlh/building-a-big-data-pipeline-with-airflow-spark-and-zeppelin-843f31ef220c

