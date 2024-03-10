import pandas as pd
from datetime import datetime
import s3fs
import json
import os


def run_twitter_etl():
    df = pd.read_csv(r"C:\Users\SENTHA.JAY\Downloads\tweets\tweets.csv")
    #print(df.head())

    filtered_df = df[df['author']=='Twitter']

    print(filtered_df.head())

    filtered_df.to_csv('s3://sentha-airflow-etl-bucket/filtered_tweets.csv',index=False)





    #file_path = 'filtered_tweets.csv'
    #if os.path.isfile(file_path):
        #print("The file exists.")
    #else:
        #print("The file does not exist.")






