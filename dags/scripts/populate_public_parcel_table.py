import pymysql
import pandas as pd

"""
populate parcels_public table directly from csv file

"""

def populate_SQL_table_v2(host, dbUserName, dbUserPassword, cusrsorType):
    conn   = pymysql.connect(host=host,
                         user=dbUserName,
                         password=dbUserPassword,
                         cursorclass=cusrsorType)

    dbCursor = conn.cursor()                              

    # Populate "Land_Use_Code_Report" table    
    reportData = pd.read_csv('/opt/airflow/dags/data/parcels_public.csv')
    reportData = reportData.where(pd.notnull(reportData), None)

    for i,row in reportData.iterrows():
        print(tuple(row))        
        sql = "INSERT INTO test.`parcels_public_v2` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbCursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()

    conn.close()

