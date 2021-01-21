import wget
import os
from pyspark.sql import SparkSession
from fastcovid.config import *


def extract(url, target_path):
    try:
        wget.download(url, os.getcwd() + target_path)
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


def etl():
    spark = SparkSession.builder.getOrCreate()
    raw_df = spark.read.csv(DATASET_PATH, header=True)
    transformed_df = transform(raw_df, COLUMNS_TO_SELECT, DATA_TYPES, MISSING_VALUES)
    load(transformed_df, TARGET_PATH)


if __name__ == '__main__':
    etl()
