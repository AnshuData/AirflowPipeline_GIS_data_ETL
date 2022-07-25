FROM apache/airflow:2.2.2

RUN pip install --no-cache-dir torch-optimizer==0.1.0 boto3==1.18 omegaconf==2.1.1 torch==1.9.0 pytorch-lightning==1.4.2 scp==0.13.6 numpy==1.21.1 pandas==1.3.2 fastavro==1.4.5 avro-python3==1.10.2 scikit-learn==0.24.1 xlrd==2.0.1 geopandas==0.11.0 pymysql==1.0.2 pandasql==0.7.3

