#!python3

import pandas as pd 
import numpy as np

ser = pd.Series()

print(ser)


# Create a series from an array

import numpy as np

data = np.array(['g','e','e','k','s'])

ser = pd.Series(data)

print(ser)

# Creating serires from array with index

ser = pd.Series(data, index=[10, 11, 12, 13, 14])

print(ser)

# Creating a series from list

l = ['g','e','e','k','s']

ser = pd.Series(l)

print(ser)

print(ser.shape) # returns the shape of series 

print(ser.dtype) # shows data types

# Creating dataframe from series


author = ['Jitender', 'Purnima', 'Arpit', 'Jyoti'] 
article = [210, 211, 114, 178] 

auth_series = pd.Series(author) 
article_series = pd.Series(article) 

frame = { 'Author': auth_series, 'Article': article_series } 

result = pd.DataFrame(frame) 

print(result) 

print(result.shape)

np.random.seed(100)

x = 170.0 + 25.0 * np.random.randn(5)

print(x)

ser = pd.Series(x)

print(ser)

print(ser.mean())

for col in result.columns:
    print(col)


# Creating a panel from data frames

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
#p = pd.Panel(data)  --old method
#print(p.shape)

data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df_O = pd.DataFrame(data, columns=['a', 'b'])
print(df_O.shape)

s = pd.Series([9.2, 'hello', 89])
print(s.dtype)

df_2 = pd.DataFrame(data)
print(df_2.shape)

s = pd.Series([99, 32, 67],list('abc'))
print(s)

# Accessing a single value

print("Acessing a single value")

z = np.arange(10, 16)
s = pd.Series(z, index=list('abcdef'))
#Accessing 3rd element of s.
print(s[2]) # ---> Returns '12' 
#Accessing 4th element of s.
print(s['d']) # ---> Returns '13'

print(s.get(2))
print(s.get('d'))

# Accessing a slice

print(s[1:3])  
print(s['b':'d'])  # Elements corresponding to start and end index values are included, when index values are used for slicing.

# Accessing rows

print(result[:2])

# Accessing column

print(result['Author'])

# Accesing multiple columns 

print(result[['Author','Article']])  # Column names are given as list