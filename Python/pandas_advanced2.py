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

# Standard missing values .isnull() : Nan will only be true

# Non standard missing values 

# missing_values = ['n/a','na','--']
# df = pd.read_csv('file_name',na_values= missing_values)  df will be populated with NaN where ever the missing values are present

"""
Another method to clean a boolean column from int vales is

cnt =0
for row in df['column']:
    try:
        int(row)
        df.loc[cnt, 'column'] = np.nan
    except ValueError:
        pass
    cnt+=1

"""

# Sumarizing missing values 

# df.isnull().sum()

# df.isnull().values.any() -- any missing values

# df.isnull().sum().sum()  -- Total missing values

# df.['col'].fillna(value, inplace = True)   inplace attribute is set to true to makes df changes permenantly

# df.loc[row,col] = for replacing 

# df.dropna() drops all rows with atleast one null value

# Data Aggregation

"""
Filtering

df[df.col > val]   - numeric filtering

df[df[col] != 'String Val']  - filtering character data

& (and),  | (or), isin(list)      are the connctors used 


"""
df = pd.DataFrame({'temp':pd.Series(28 + 10*np.random.randn(10)),
                   'rain':pd.Series(100 + 50*np.random.randn(10)),
                   'location':list('AAAAABBBBB')
})
print(df.head(2))

replacements = {
'location': {'A':'Hyderabad', 'B':'Mumbai'}
}
df = df.replace(replacements, regex=True)  # code replace A with Hyderabad and B with Mumbai
print(df.head(2))

mumbai_data = df.loc[df.location.str.contains('umb'),:]  # filtering loction containing 'umb'

print(mumbai_data.head(2))

regions = df.groupby('location')
print(regions.groups)
print(regions.mean())  # groupby method can be used to group data and perform various function on each group.


# Merging data  -- merge

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

print(pd.merge(df1,df2, on = 'HPI'))  # merge on single column default inner join (how) - control the join

print(pd.merge(df1,df2, on = ['HPI','Int_rate'])) # merge on multiple columns to remove duplicate

df1.set_index('HPI', inplace= True)
df3.set_index('HPI', inplace= True)

Joined = df1.join(df3)  # join uses index value to join two dfs
print(Joined)


s1 = pd.Series([0, 1, 2, 3])
s2 = pd.Series([0, 1, 2, 3])
s3 = pd.Series([0, 1, 4, 5])
d = pd.concat([s1, s2, s3], axis=1)

print(d)
print(d.shape)
