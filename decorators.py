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


