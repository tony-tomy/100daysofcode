#!python3

# Decorators

'''
A decorator function is a higher order function that takes a function as an argument and returns the inner function.

A decorator is capable of adding extra functionality to an existing function, without altering it.

The decorator function is prefixed with @ symbol and written above the function definition.
'''

def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return(func())
    return(inner)
def greet():
   print('Hello!')
wish = outer(greet)
wish()   # wish is the closure function obtained by calling an outer function with the argument greet.

def outer(func):
    def inner():
        print("Accessing :", 
                  func.__name__)
        return(func())
    return(inner)
def greet():
   print('Hello!')
greet = outer(greet) # decorating 'greet'  -- This makes outer a decorator to greet()
greet() # calling new 'greet'

def outer(func):
    def inner():
        print("Accessing :", 
                func.__name__)
        return func()
    return inner
@outer                    # greet = outer(greet) expression is same as @outer
def greet():
    return 'Hello!'
greet()


# Decorator with parameters

def f1(func):
    def wrapper(*args):
        print('Started')
        func(*args)
        print('Ended')
    return(wrapper)

@f1
def f(a,b=9):   # accept a parameter
    print(a,b)

f('Hello')

# Decorator with parameters and returns the values

def f1(func):
    def wrapper(*args):
        print('Started')
        val =func(*args)   # same decorator modified for cathering the requirements of both functions.
        print('Ended')
        return(val)
    return(wrapper)

@f1
def f(a,b=9):   # accept a parameter
    print(a,b)

@f1
def add(x,y):   # accept a parameter and returns a value
    return(x+y)

f('Hello')

print(add(5,9))

# Example 1  -  Decorated method

import time

def before_after(func):
    def wrapper(*args):
        print('Before')
        func(*args)
        print('After')

    return(wrapper)

class Test:
    @before_after
    def decorated_method(self):
        print('Run')

t = Test()
t.decorated_method()

# Example 2 - Timer decorator

def timer(func):
    def wrapper():
        before = time.time()
        func()
        print('Time taken for execution', time.time() - before, 'Seconds')
    return(wrapper)

@timer
def run():
    time.sleep(2)

run()

# Example 3 - log decorator

import datetime

def log(func):
    def wrapper(*args, **kwargs):
        with open('logs.txt','a') as f:
            f.write('Called function with ' + ' '.join([str(arg) for arg in args]) + ' at ' + str(datetime.datetime.now()) + '\n')
        val = func(*args, **kwargs)
        return(val)
    return(wrapper)

@log
def run(a,b,c=9):
    print(a+b+c)

run(1,3)