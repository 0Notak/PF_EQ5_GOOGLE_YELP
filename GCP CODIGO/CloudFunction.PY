from google.cloud import storage
import pyarrow.parquet as pq
import pandas as pd
from io import BytesIO
from sqlalchemy import create_engine

def pipeline(event, context):

    file = event
    print(f"Processing file: {file['name']}.")
    print(f"Event payload(event): {event}.")
    print(f"Metadata for the event(context): {context}.")

    # Set your GCS bucket and file path
    bucket_name = "datasetshenry"

    file_path1 = "REV_AZ.parquet"
    file_path2 = "REV_CA.parquet"
    file_path3 = "REV_FL.parquet"
    file_path4 = "business3estados.parquet"
    file_path5 = "checkin3estados.parquet"
    file_path6 = "user3estados.parquet"
    

    df1 = read_csv_from_gcs1(bucket_name, file_path1) # Read CSV file from Cloud Storage into a DataFrame
    df2 = read_csv_from_gcs2(bucket_name, file_path2)
    df3 = read_csv_from_gcs3(bucket_name, file_path3)
    df4 = read_csv_from_gcs4(bucket_name, file_path4)
    df5 = read_csv_from_gcs5(bucket_name, file_path5)
    df6 = read_csv_from_gcs6(bucket_name, file_path6)


    ddf1 = ETL(df1) # Apply transformation to DataFrame
    ddf2 = ETL(df2)
    ddf3 = ETL(df3)
    ddf4 = ETL(df4)
    ddf5 = ETL(df5)
    ddf6 = ETL(df6)

    
    engine = create_engine('mysql+pymysql://sqlhenry:soyhenry@proyecto-final-henry-419706:us-west1:sqlhenry/pf_henry')



    
    ddf1.to_sql("rev_az", connection, if_exists='append', index=False)
    ddf2.to_sql("rev_ca", connection, if_exists='append', index=False)
    ddf3.to_sql("rev_fl", connection, if_exists='append', index=False)
    ddf4.to_sql("business", connection, if_exists='append', index=False)
    ddf6.to_sql("user1", connection, if_exists='append', index=False)











def read_csv_from_gcs1(bucket_name, file_path1):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path1)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df1 = pd.read_parquet(io.StringIO(csv_data))
    return df1

def read_csv_from_gcs2(bucket_name, file_path2):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path2)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df2 = pd.read_parquet(io.StringIO(csv_data))
    return df2

def read_csv_from_gcs3(bucket_name, file_path3):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path3)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df3 = pd.read_parquet(io.StringIO(csv_data))
    return df3

def read_csv_from_gcs4(bucket_name, file_path4):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path4)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df4 = pd.read_parquet(io.StringIO(csv_data))
    return df4

def read_csv_from_gcs5(bucket_name, file_path5):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path5)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df5 = pd.read_parquet(io.StringIO(csv_data))
    return df5

def read_csv_from_gcs6(bucket_name, file_path6):
    """Reads a CSV file from Cloud Storage into a Pandas DataFrame."""
    storage_client = storage.Client()

    # Get the bucket and blob objects
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(file_path6)

    # Download the contents of the blob as a string
    csv_data = blob.download_as_text()

    # Read the CSV data into a Pandas DataFrame
    df6 = pd.read_parquet(io.StringIO(csv_data))
    return df6



def ETL (df1, df2, df3, df4, df5, df6):

    ddf4=df4.drop(columns=['address', 'postal_code', 'is_open', 'attributes', 'hours'])
    ddf6=df6.drop(columns=['compliment_hot'])
    ddf1=df1.drop(columns=['address', 'postal_code', 'stars_x', 'latitude', 'longitude'])
    ddf1 = df1.rename(columns={'stars_y':'stars'}, inplace=True)
    ddf1 = df1.rename(columns={ 'date' : 'fecha' })
    ddf3=df3.drop(columns=['address', 'postal_code', 'stars_x', 'latitude', 'longitude'])
    ddf3=df3.rename(columns={'stars_y':'stars'}, inplace=True)
    ddf3 = df3.rename(columns={ 'date' : 'fecha' })
    ddf2 = df2.rename(columns={ 'date' : 'fecha' })
    ddf5=df5



    ddf1.drop_duplicates()
    ddf2.drop_duplicates()
    ddf3.drop_duplicates()
    ddf4.drop_duplicates()
    ddf5.drop_duplicates()
    ddf6.drop_duplicates()

    return ddf1, ddf2, ddf3, ddf4, ddf5, ddf6



