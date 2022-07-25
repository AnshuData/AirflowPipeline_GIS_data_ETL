import os
import zipfile

"""
Download the zip file from GIS website for Napa Valley and unzip it in local folder
"""

def download_GIS_data():
        os.system("curl http://gis.napa.ca.gov/data/boundaries/parcels_public.zip  --output /opt/airflow/dags/data/parcels_public.zip")
        with zipfile.ZipFile('/opt/airflow/dags/data/parcels_public.zip', "r") as file:
                file.extractall('/opt/airflow/dags/data/')
        print('data downloaded to local folder !!')
