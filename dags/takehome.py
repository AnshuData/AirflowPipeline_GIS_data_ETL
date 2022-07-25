import os
import pymysql
import zipfile
import pandas as pd
import geopandas as gpd

from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook

from scripts.sql_table import create_SQL_table
from scripts.populate_land_use_code_report import populate_SQL_table
from scripts.parse_and_convert_format import convert_file_format
from scripts.download_and_unzip import download_GIS_data
from scripts.populate_public_parcel_table import populate_SQL_table_v2 


#
# Fill in the database credentials here !!! 
#
#           WARNING !!!
# For production, Never use this way, rather add connection from airflow UI,
# Due to some bug with my airflow version I can not do that, considering time constraint 
#
# Sample code for using airflow MySQL hook is provided in scripts/populate_with_sql_hook.py
#

host            = 'XYZ.us-east-1.rds.amazonaws.com'
dbUserName      = 'XXX'
dbUserPassword  = 'YYY'
cusrsorType     = pymysql.cursors.DictCursor


'''
Airflow pipeline that does the following tasks:
  1. pulls the data from GIS website for NAPA valley, unzip it
  2. parse the raw data files and convert necessary files to csv files,
  3. Create SQL tables in AWS RDS (database already created)
  4. Populate sample of entire data to SQL tables

'''

with DAG(
  "take_home",
  start_date=days_ago(1),
  schedule_interval=None,
  ) as dag:



   Download_GIS_data  = PythonOperator(
        task_id="Download_GIS_data", python_callable=download_GIS_data,
    )

   convert_schema  = PythonOperator(
        task_id="parse_data_and_change_file_format", python_callable=convert_file_format,
    )


   create_SQL_tables  = PythonOperator(
        task_id="create_SQL_tables", python_callable=create_SQL_table,
        op_args=[host, dbUserName, dbUserPassword, cusrsorType]
    )

   populate_report_tables  = PythonOperator(
        task_id="populate_land_use_code_report", python_callable=populate_SQL_table,
        op_args=[host, dbUserName, dbUserPassword, cusrsorType]
    )


   populate_parcel_table  = PythonOperator(
        task_id="populate_parcel_table", python_callable=populate_SQL_table_v2,
        op_args=[host, dbUserName, dbUserPassword, cusrsorType]
    )


Download_GIS_data  >> convert_schema  >> create_SQL_tables  >> populate_parcel_table >> populate_report_tables 
