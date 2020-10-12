#!python3

# Higher Order Functions 
'''
A Higher Order function is a function, which is capable of doing any one of the following things:
It can be functioned as a data and be assigned to a variable.
It can accept any other function as an argument.
It can return a function as its result.
'''

# Function as a Data

def greet():
    return('Hello everyone !')

print(greet())
wish = greet
print(type(wish))
print(wish())

# Function as arguments

def add(x,y):
    return(x+y)

def sub(x,y):
    return(x-y)

def prod(x,y):
    return(x*y)

def do(func,x,y):
    return(func(x,y))

print(do(add,10,7))
print(do(sub,9,6))
print(do(prod,5,5))

# Returning a function

def outer():
    def inner():
        s = 'Hello inner function'
        return(s)
    return(inner())

print(outer())

# Note : Parenthesis after the inner function are removed so that the outer function returns inner function.

# Closures

# Closure is a function returned by a higher order function, whose return value depends on the data associated with the higher order function.

def multiple_of(x):
    def multiple(y):
        return x*y
    return multiple
c1 = multiple_of(5)  # 'c1' is a closure
c2 = multiple_of(6)  # 'c2' is a closure
print(c1(4))
print(c2(4))
