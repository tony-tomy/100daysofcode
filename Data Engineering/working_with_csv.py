import pandas as pd

df = pd.read_csv('Data Engineering/taxi.csv.bz2')
print(df.dtypes)

time_cols = ['tpep_pickup_datetime','tpep_dropoff_datetime']

df1 = pd.read_csv('Data Engineering/taxi.csv.bz2', parse_dates= time_cols)
print(df1.dtypes)