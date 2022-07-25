# AirflowPipeline_GIS_data_ETL

This is airflow pipeline created with Airflow version 2.

To run the pipeline; you need docker installed and running

1. docker build -t airflow/kettle_takehome:1.0.1 .

2. docker compose up

3. Visit the link below once it is up and running
	http://localhost:8080/home

	username: airflowTest
	pwd: airflowTest


------------------------WARNING-------------------
4. I used AWS RDS to run the job. Before you can run this; provide your AWS RDS MySQL database host-name, user name and pwd in takehome.py
	Providing database credentials in code is NEVER RECCOMMENDED. I had bug identifying secrets from my Airflow UI connection. 



5. Run the Pipeline
