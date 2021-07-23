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

df_3  = result.loc[1:3]  # slicing function based on label or boolean

print(df_3)

df_4 = result.iloc[:2]   # slicing function based on integer position

print(df_4)

df_1 = result.iloc[[2,3,0]]  # Selecting rows via integer listing

print(df_1)

df_5 = result.loc[((result.index % 10 == 1) | (result.index % 10 == 3))]  # Boolean function for selecting rows.

print(df_5)

# Pass a boolean function which checks if an index string ends with 1 or 4 

heights_A=pd.Series([176.2,158.4,167.6,156.2,161.4], index=['s1','s2','s3','s4','s5'])
weights_A=pd.Series([85.1,90.2,76.8,80.4,78.9], index=['s1','s2','s3','s4','s5'])
df_A=pd.DataFrame({'Student_height':heights_A, 'Student_weight':weights_A})
df_s1s4 = df_A.loc[(df_A.index.str.endswith('1') | df_A.index.str.endswith('4'))]

print(df_s1s4)

df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])

print(df.B)

df['C'] = [12,98,45]  # Expression to add new column to the existing df

print(df)

print(df.iloc[1])  # returns the second row

df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])

df.loc['r4'] = [67, 78]  # Adding new row

print(df) 


# Pnadas final quiz
print('Final Answers')

df = pd.DataFrame({'A' : [1,2,3], 'B' :[4,5,6], 'C':[7,8,9], 'D':[10,11,12]},index = ['r1', 'r2', 'r3'])
print(df[lambda x : x.index.str.endswith('3')])

df = pd.DataFrame({'A':[34, 78, 54], 'B':[12, 67, 43]}, index=['r1', 'r2', 'r3'])

print(df.loc[:'r3'])

df.loc['r4'] = [67, 78]

print(df[:2])

df = pd.DataFrame({'A' : [1,2,3], 'B' :[4,5,6], 'C':[7,8,9], 'D':[10,11,12]},index = ['r1', 'r2', 'r3'])

print(df.loc[:, lambda x: x.columns.isin(['C','D'])])

del df['D']

np.random.seed(100)
df = pd.DataFrame({ 'A' : 100 + 25 * np.random.randn(10), 'B': 50 + 12 *np.random.randn(10)},
index=[ 'r1', 'r2', 'r3', 'row4', 'row5', 'row6', 'r7', 'r8', 'r9', 'row10'])

g = df.groupby(df.index.str.len())
print(df)
print(g.aggregate({'A':len, 'B':np.sum}))

s = pd.Series([89.2, 76.4, 98.2, 75.9], index=list('abcd'))
print('b' in s)

s = pd.Series([9.2, 'hello', 89])
print(s.dtype)

df = pd.DataFrame({'A' : [1,2,3], 'B' :[4,5,6], 'C':[7,8,9], 'D':[10,11,12]},index = ['r1', 'r2', 'r3'])
print(df.loc[df.B > 5])