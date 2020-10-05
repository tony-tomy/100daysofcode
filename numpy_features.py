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

# ndarray attributes 

"""
ndim : Returns number of dimensions.
shape: Returns Shape in tuple.
size : Total number of elements.
dtype : Type of each element.
itemsize : Size of each element in Bytes.
nbytes : Total bytes consumed by all elements.
"""
print(y.ndim, y.shape, y.size, y.dtype, y.itemsize, y.nbytes)

y = np.array([3+4j, 0.4+7.8j])
print(y.dtype)

n = [[-1, -2, -3, -4], [-2,-4, -6, -8]]

y = np.array(n)

print(type(y))

print(y.ndim, y.shape, y.size, y.dtype, y.nbytes)

# Array creation methods : zero method

x = np.zeros(shape=(2,4))
print(x)

# Array creation methos : full method

y = np.full(shape=(2,3), fill_value=10.5)
print(y)

# Numeric sequence generators
"""
arange : Numbers created based on step value.

Syntax - numpy.arange([start, ]stop, [step, ]dtype=None)
"""

x = np.arange(3, 15, 2.5) # 2.5 is step
print(x)

"""
linspace : Numbers created based on size value.

Syntax - numpy.linspace(start, stop, #num inbetween, endpoint=True, retstep=False, dtype=None)
"""

y = np.linspace(3, 15, 5) # 5 is size of array 'y'
print(y)

# Random number generation

np.random.seed(100) # setting seed
x = np.random.rand(2) # 2 random numbers between 0 and 1

print(x)

np.random.seed(100) # setting seed
y = np.random.randint(10, 50, 3) # 3 random integers between 10 and 50

print(y)

# Simulating Normal Distribution

np.random.seed(100)
x = np.random.randn(3) # Standard normal distribution

print(x)

np.random.seed(100)
x = 10 + 2*np.random.randn(3) # normal distribution with mean 10 and sd 2

print(x)

# Reading data from a file  loadtxt()

from io import StringIO
import numpy as np

x = StringIO('''88.25 93.45 72.60 90.90
72.3 78.85 92.15 65.75
90.5 92.45 89.25 94.50
''')

d = np.loadtxt(x,delimiter=' ')

print(d)

print(d.ndim, d.shape)

x = np.array([[-1,0,1], [-2, 0, 2]])

y = np.zeros_like(x)
print(y)

z = np.eye(2) # eye() is used for returning a matrix i.e. a 2D array having 1's at its diagonal and 0's elsewhere
print(z)

print(np.array(([1, 2], (3,4))).shape)

# Define a random 3-D array x4 of shape (3, 4, 2) and of numbers between 0 and 1.

x4 = np.random.rand(3,4,2)

print(x4)

x5 = np.arange(2,40,2)

print(x5)

# Reshaping an ndarray using reshape()

np.random.seed(100)
x = np.random.randint(10, 100, 8)
print(x, end='\n\n')
y = x.reshape(2,4)
print(y, end='\n\n')
z = x.reshape(2,2,2)
print(z, '\n\n')

# Stacking array vertically

x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
print(np.vstack((x,y)))

# Stacking array horizontally

x = np.array([[-1, 1], [-3, 3]])
y = np.array([[-2, 2], [-4, 4]])
z = np.array([[-5, 5], [-6, 6]])
print(np.hstack((x,y,z)))

# Spliting array vertically

x = np.arange(30).reshape(6, 5)
res = np.vsplit(x, 2)
print(res[0], end='\n\n')
print(res[1])

res = np.vsplit(x, (2, 5))  # Spliting array vertically to three arrays
print(res[0], end='\n\n')
print(res[1], end='\n\n')
print(res[2])

# Spliting array horizontally

x = np.arange(10).reshape(2, 5)
res = np.hsplit(x, (2,4))
print(res[0], end='\n\n')
print(res[1], end='\n\n')
print(res[2])

x = np.arange(6).reshape(2,3)

y = np.hsplit(x,(2,))
print(y[0])

x = np.arange(4).reshape(2,2)
y = np.arange(4, 8).reshape(2,2)

print(np.hstack((x,y)))

# Basic operations with scalar

x = np.arange(6).reshape(2,3)
print(x + 10, end='\n\n')
print(x * 3, end='\n\n')
print(x % 2)

# Basic Operations between Arrays

x = np.array([[-1, 1], [-2, 2]])
y = np.array([[4, -4], [5, -5]])
print(x + y, end='\n\n')
print(x * y)

# perform operations on arrays with varying size and shape.

x = np.array([[-1, 1], [-2, 2]])
y = np.array([-10, 10])
print(x * y)

# Universal function 

x = np.array([[0,1], [2,3]])
print(np.square(x), end='\n\n')
print(np.sin(x))

print(x.sum(), end='\n\n')
print(x.sum(axis=0), end='\n\n') # can use axis to sum a specific dimension
print(x.sum(axis=1))

x = np.arange(30).reshape(5,6)
print(x.argmax(axis=1)) # Return indices of maximum value along the axis

# Create a array x of shape (5, 6), having random integers between -30 and 30

x = np.random.randint(-30,30, size=(5, 6)) 

print(x)

# Compute the mean, standard deviation, and variance numpy.mean(), numpy.std(), numpy.var()

x = 10 + 2*np.random.randn(3) # mean 10 and stansard deviation.

print(np.mean(x))

print(np.std(x))

print(np.var(x))

# Iterating through array

x = np.array([[-1, 1], [-2, 2]])
for row in x:                           # using for
    print('Row :',row)

for a in np.nditer(x):                  # using nditer : iterate through each element.
    print(a)

# Boolean indexing : Checking if every element of an array satisfies a condition, results in a Boolean array

x = np.arange(10).reshape(2,5)
condition = x % 2 == 0
print(condition)
print(x[condition])

#

x = np.array([[0, 1], [1, 1], [2, 2]])
print(x.sum(-1))

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])

x = np.arange(30).reshape(3,5,2)
print(x[1,::2,1])

x = np.arange(4)
print(x.flatten())

x = np.arange(12).reshape(3,4)
print(x[-2])