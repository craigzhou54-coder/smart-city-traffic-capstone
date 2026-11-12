import pandas as pd
import sqlite3

#read CSV
df = pd.read_csv('data/Metro_Interstate_Traffic_Volume.csv')

#connect SQLite
conn = sqlite3.connect('traffic.db')

#import data
df.to_sql('traffic_data',
          conn,
          if_exists='replace',
          index=False
)

print(f"Imported {len(df)} rows")

conn.close()