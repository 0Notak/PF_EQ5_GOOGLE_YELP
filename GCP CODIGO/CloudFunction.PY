from google.cloud import storage
import pyarrow
import pandas as pd
from io import BytesIO
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def pipeline(event, context):


    rev_az = pd.read_parquet('gs://datasetshenry/REV_AZ.parquet')
    rev_ca = pd.read_parquet('gs://datasetshenry/REV_CA.parquet')
    rev_fl = pd.read_parquet('gs://datasetshenry/REV_FL.parquet')
    buss = pd.read_parquet('gs://datasetshenry/business3estados.parquet')
    ch = pd.read_parquet('gs://datasetshenry/checkin3estados.parquet')
    user = pd.read_parquet('gs://datasetshenry/user3estados.parquet')
    rs = pd.read_parquet('gs://datasetshenry/resultado.parquet')
   

    engine = create_engine('mysql+pymysql://root:soyhenry@35.247.37.77/pf_henry')
    

    rev_az['ano']=rev_az['date'].dt.year
    rev_az['mes']=rev_az['date'].dt.month
    rev_az2=rev_az.drop(columns=['address', 'postal_code', 'stars_x', 'latitude', 'longitude', 'date','review_count', 'city'])
    rev_az2.rename(columns={'stars_y':'stars'}, inplace=True)
    rev_az2['state'] = rev_az2['state'] = 'az'


    rev_ca2=rev_ca.drop(columns='date')
    rev_ca2['state'] = rev_ca2['state'] = 'ca'
    rev_ca2['name'] = rev_ca2['name'] = 'pizza'
    rev_ca3=rev_ca2[['user_id','name','business_id', 'stars','useful', 'funny','cool', 'Polaridad del sentimiento', 'Sentimiento', 'ano','mes','state']]

    rev_fl2=rev_fl.drop(columns=['address', 'postal_code', 'stars_x', 'latitude', 'longitude', 'review_count', 'city'])
    rev_fl2['ano']=rev_fl2['date'].dt.year
    rev_fl2['mes']=rev_fl2['date'].dt.month
    rev_fl2.rename(columns={'stars_y':'stars'}, inplace=True)
    rev_fl2=rev_fl2.drop(columns='date')
    rev_fl2['state'] = rev_fl2['state'] = 'fl'


    

    rev3estados=pd.concat([rev_ca3, rev_az2, rev_fl2], ignore_index=True)

    buss2=buss.drop(columns=['hours', 'categories', 'attributes', 'address', 'postal_code', 'latitude', 'longitude'])

    user2=user.drop(columns='compliment_hot')



    rev3estados=rev3estados.drop_duplicates(keep='first')
    buss2=buss2.drop_duplicates(keep='first')
    user2=user2.drop_duplicates(keep='first')
    rs=rs.drop_duplicates(keep='first')




    rev3estados.to_sql('reviews3estados', con=engine,  if_exists='append', index=False)
    buss2.to_sql('business', con=engine,  if_exists='append', index=False)
    user2.to_sql('users', con=engine,  if_exists='append', index=False)
    rs.to_sql('reviews', con=engine,  if_exists='append', index=False)
