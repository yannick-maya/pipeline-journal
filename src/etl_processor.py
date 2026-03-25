import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName('ETLProcessor').getOrCreate()

# Extract
def extract_data(csv_file):
    return pd.read_csv(csv_file)

# Transform
def transform_data(df):
    # Example transformation: drop duplicates
    return df.drop_duplicates()

# Load
def load_data(df, destination):
    # Converting dataframe to Spark DataFrame
    spark_df = spark.createDataFrame(df)
    # Write to Parquet file (as an example)
    spark_df.write.parquet(destination)

if __name__ == '__main__':
    # Example usage
    data = extract_data('data/input.csv')
    transformed_data = transform_data(data)
    load_data(transformed_data, 'data/output.parquet')
