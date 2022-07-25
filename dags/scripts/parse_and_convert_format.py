import pandas as pd
import geopandas as gpd

def convert_file_format():
        """
        Read .shp file and convert it to csv file
        It will be used later to populate SQL tables or to move data lake or warehouse
        where we can query from
        """

        df_shp = gpd.read_file('/opt/airflow/dags/data/parcels_public.shp')
        # each row represent spatial object or one lot of land
        df_shp[:300].to_csv('/opt/airflow/dags/data/parcels_public.csv')


        new_column_list = ['Land Use Code', 'Descr', 'Direct Chrg Class', 'Dwelling Type', 'Use Category', 'BOECategory', 'Is Apply Inflation', 'Status', 'DTS']


        df_raw_excel_data  = pd.read_excel(
                io='/opt/airflow/dags/data/Land Use Code Report 10-2021.xls',
                nrows=139,
                skiprows=[0,1,2,3,4,5,6,7,8,9,10],
                usecols="B:AL"
                )

        df_clean_excel_data  = df_raw_excel_data.dropna(axis=1, how='all')
        df_clean_excel_data.columns = new_column_list

        # Export the clean excel data to csv files, it contains important data for ML.
        # It contains few categorical varibale that will be used as feature for ML

        df_clean_excel_data.to_csv('/opt/airflow/dags/data/Land_Use_Code_Report.csv', index=None)
