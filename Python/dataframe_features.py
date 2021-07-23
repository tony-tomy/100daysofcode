#!python3

import pandas as pd 

print(pd.__version__)

# Python pandas DataFrame

"""
A Data frame is a two-dimensional data structure, i.e., data is aligned in a tabular fashion in rows and columns.

Features of DataFrame
Potentially columns are of different types
Size – Mutable
Labeled axes (rows and columns)
Can Perform Arithmetic operations on rows and columns

pandas.DataFrame( data, index, columns, dtype, copy)

data : data takes various forms like ndarray, series, map, lists, dict, constants and also another DataFrame.
index : For the row labels, the Index to be used for the resulting frame is Optional Default np.arange(n) if no index is passed.
columns : For column labels, the optional default syntax is - np.arange(n). This is only true if no index is passed.
dtype : Data type of each column.
copy : This command (or whatever it is) is used for copying of data, if the default is False.

"""

# Create an empty dataframe

df = pd.DataFrame()

print(df)

# Create a dataframe from list

data = [1,2,3,4,5]

df = pd.DataFrame(data)

print(df)

data = [['Bob',10],['Alex',20],['Ciril',30]]

df = pd.DataFrame(data)

print(df)

df = pd.DataFrame(data, columns=['Name','Age'], dtype= float) # Age column value changes to float

print(df)

# Create a Dataframe from dict of ndarrays/ lists

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]} 
df = pd.DataFrame(data) # default index will be assigned using range(n)
print(df)

# Create an indexed DataFrame

df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)

# Create a DataFrame from list of dictionaries 

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]  # NaN (Not a Number) is appended in missing area.
df = pd.DataFrame(data)
print(df)

# Create a DataFrame with a list of dictionaries, row indices, and column indices.

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)

# Create a DataFrame from Dict of Series

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df)
print(df['one'])

# Adding a new column to an existing DataFrame object with column label by passing new series

df['three'] = pd.Series([10,20,30],index = ['a','b','c'])

df['four'] = df['one'] + df['two']

print(df)

# Column deletion

del df['one']

print(df)

# pop function

df.pop('two')

print(df)

# Row Selection

print(df.loc['b'])

# Selection by integer location

print(df.iloc[2])

# slice row

print(df[1:3])

# Addition of rows

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df)

# deletion of rows

df = df.drop(0)

print(df)