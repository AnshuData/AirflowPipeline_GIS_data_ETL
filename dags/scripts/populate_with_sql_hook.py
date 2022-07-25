import pandas as pd

"""
Populate table using AWS hook for MySQL; This is recommended way
"""

def populate_table():

        SQL_table_name = 'test."Land_Use_Code_Report"'
        df_clean_excel_data = pd.read_csv('/opt/airflow/dags/data/Land_Use_Code_Report_v2.csv')
        rows_to_update = list(df_clean_excel_data.to_dict('index').values())
        print(rows_to_update[:2])

        aws_hook = MySqlHook(SQL_conn_id='mysql_default')
        aws_hook.insert_rows(SQL_table_name, rows_to_update)
