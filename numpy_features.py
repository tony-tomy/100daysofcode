#!python3

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)

# checking numpy version

print(np.__version__)

print(type(arr))

# creating ndarray of numpy by passing a tuple

arr = np.array((1,2,3,4,5))

print(arr)

# 0-D array

arr = np.array(42)

print(arr)

# 1-D array 

arr = np.array([1,2,3,45])

print(arr)

# 2-D array

arr = np.array([[1,2,3],[4,5,6]])

print(arr)

# 3-D array

arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(arr)

# check number of dimensions 

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Higher dimensions array

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

# Array accessing elements

arr = np.array([1,2,3,4,5])

print(arr[1])

print(arr[2]+arr[3])

# Accessing a 2-D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st dim: ', arr[0, 1])

# Accessing a 3-D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

# Negative indexing

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

# Numpy array slicing [start:end:step]

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

"""
Note: The result includes the start index, but excludes the end index.
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""

# Negative slicing

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[-3:-1])

# Slicing with step 

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[::2])

# Slicing 2-D arrays 

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

print(arr[0:2, 1:4])

# Data types in Numpy
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""

print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])

print(arr.dtype)

# Creating an array with defined data type

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# For i, u, f, S and U we can define size as well.

arr = np.array([1, 2, 3, 4], dtype='i4')

print(arr)
print(arr.dtype)

# Converting data types on existing arrays astype()

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)

# The main difference between a copy and a view of an array is that the copy is a new array, 
# and the view is just a view of the original array.

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Check if array owns the data

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)