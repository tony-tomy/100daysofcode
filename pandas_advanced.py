#!python3

import pandas as pd 
import numpy as np

# Knowing a series - describe() method

temp = pd.Series(28 + 10*np.random.randn(10))
print(temp.describe())

# Knowing a DataFrame - info() and describe()

df = pd.DataFrame({'temp':pd.Series(28 + 10*np.random.randn(10)), 
                'rain':pd.Series(100 + 50*np.random.randn(10)),
             'location':list('AAAAABBBBB')})
print(df.info())

print(df.describe()) # method by default provides details of only numeric fields

print(df)

print(df.describe(include=['object'])) # include attribute is used to provide details for other columns

# I/O with Pandas  - read_csv, to_csv

df = pd.read_csv('D:/Python Workspace/Visual Studio Code/Files/annualenterprisesurvey2019.csv')

print(df.head())

#df.set_index('column_name', inplace= True)  setting index

df.to_csv('test.csv') # Write output to csv

# Rename the columns

df.columns = ['Year', 'Code','Industry','Size','Variable','Value','Unit']

print(df.head())

df.to_csv('test1.csv', header=False)

# Convert to another type

df.to_html('example.html')

df.rename(columns ={'Value' : 'Cost'}) # Rename a column




