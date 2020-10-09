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

# Reading data from URL

import urllib.request
import urllib.parse
import re

url = 'http://pythonprogramming.net'
values = {'s':'basics',
            'submit':'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for eachP in paragraphs:
   print(eachP)


# Reading data from databases

import sqlite3 

#db connection

try:
   conn = sqlite3.connect()
   print('Database connection was successful ')

except Exception as e:
   print('Error during connection ', str(e))

#results = conn.execute("select * from company")

#for row in results:
#   print(row)

#conn.close()

# Read data from json

EmployeeRecords = [{'EmployeeID':451621, 'EmployeeName':'Preeti Jain', 'DOJ':'30-Aug-2008'},
{'EmployeeID':123621, 'EmployeeName':'Ashok Kumar', 'DOJ':'25-Sep-2016'},
{'EmployeeID':451589, 'EmployeeName':'Johnty Rhodes', 'DOJ':'04-Nov-2016'}]

import json
emp_records_json_str = json.dumps(EmployeeRecords)
df = pd.read_json(emp_records_json_str, orient='records', convert_dates=['DOJ'])
print(df)
