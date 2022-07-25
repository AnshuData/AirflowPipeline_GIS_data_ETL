import pymysql
import pandas as pd

"""
Populate Land_Use_Code_Report table directly from csv file
"""

def populate_SQL_table(host, dbUserName, dbUserPassword, cusrsorType):
    conn   = pymysql.connect(host=host,
                         user=dbUserName,
                         password=dbUserPassword,
                         cursorclass=cusrsorType)

    dbCursor = conn.cursor()                              

    # Populate "Land_Use_Code_Report" table    
    reportData = pd.read_csv('/opt/airflow/dags/data/Land_Use_Code_Report.csv')
    reportData = reportData.where(pd.notnull(reportData), None)

    for i,row in reportData[:100].iterrows():
        # SQL query string
        sql = "INSERT INTO test.`Land_Use_Code_Report_v3` VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        dbCursor.execute(sql, tuple(row))
        print("Record inserted")
        conn.commit()

    conn.close()

