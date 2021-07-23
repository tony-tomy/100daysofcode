#!python3

import numpy as np

x = np.arange(4).reshape(2,2)
y = np.arange(4, 8).reshape(2,2)

print(np.hstack((x,y)))

x = np.arange(4).reshape(2,2)
print(np.isfinite(x))

z = np.eye(2)
print(z)

y = np.array([3+4j, 0.4+7.8j])
print(y.dtype)

x = np.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 1]])

x = np.arange(20).reshape(4,5)
print(x.mean(axis=1))

x = np.arange(30).reshape(5,6)
print(x.argmax(axis=1))

x = np.arange(6).reshape(2,3)

y = np.hsplit(x,(2,))
print(y[0])

x = np.array([[-2], 
              [2]])
y = np.array([[-3, 3]])
print(x.dot(y))

x = np.arange(4).reshape(2,2)
print(x.tolist())


x = np.arange(4)
y = np.arange(4)

print(x == y)