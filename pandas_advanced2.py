#!python3

import pandas as pd 
import numpy as np

# Indexing

df = pd.DataFrame(np.random.rand(5,2))
df.index = ['row_' + str(i)  for i in range(1,6)]
print(df)

ufo = pd.read_csv('http://bit.ly/uforeports')

print(ufo.head())

print(ufo.dtypes)

# Date time indexes 

ufo['Time'] = pd.to_datetime(ufo.Time)  # Converting column from object to a date time field : dt.__ properties can be applied

print(ufo)

print(ufo.dtypes)

print(ufo.Time.dt.dayofyear.head())  # dt.__ properties examples

ts = pd.to_datetime('1/1/1999')

print(ufo.loc[ufo.Time >= ts, :].head())  # date time comparison. 

print(ufo.Time.max()) # mathematics functions

print((ufo.Time.max()-ufo.Time.min()).days)

# Bonus Graph plotting



ufo['Year'] = ufo.Time.dt.year

print(ufo.head())

print(ufo.Year.value_counts().sort_index().head()) # Can be used for graph plotting

# Hierarchical Indexing

# pd.MultiIndex.from_arrays()

# MultiIndex.levels

# df.set_index() where a set of columns are given as list values for setting index.

# df.index to show the index details


dates = pd.date_range('1-Sep-2017','15-Sep-2017')

print(dates[2])

# Questions

d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
print(len(d[d.isin(pd.to_datetime(['12-09-2017', '15-09-2017']))]))

d = pd.date_range('11-Sep-2017', '17-Sep-2017', freq='2D')
print(d)
print(d + pd.Timedelta('1 days 2 hours'))

# Data Cleaning 

