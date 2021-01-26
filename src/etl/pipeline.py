import wget
import os
from pyspark.sql import SparkSession


def extract(url, target_path):
    try:
        wget.download(url, target_path)
    except Exception as error:
        print(f'An error occurred: {error}')
    else:
        print('The file was downloaded with success!')


def transform(df, columns, data_types, missing_values):
    try:
        df = df.select(*columns)
        for column, data_type in data_types.items():
            df = df.withColumn(column, df[column].cast(data_type))
        df = df.fillna(missing_values)
    except Exception as error:
        print(f'An error occurred during the data transformation: {error}')
    else:
        print('The data transformation was made with success!')
        return df


def load(df, target_path):
    try:
        df.toPandas().to_csv(target_path)
    except Exception as error:
        print(f'An error occured during the data loading: {error}')
    else:
        print('The data was loading with success!')


def etl(url, dataset_path, target_path, columns, data_types, missing_values):
    try:
        extract(url, 'src/etl/raw_data/')
        spark = SparkSession.builder.getOrCreate()
        raw_df = spark.read.csv(dataset_path, header=True)
        transformed_df = transform(raw_df, columns, data_types, missing_values)
        load(transformed_df, target_path)
    except Exception as error:
        print(f'An error occured in the ETL process: {error}')
    else:
        print('The ETL process was done with success!')
