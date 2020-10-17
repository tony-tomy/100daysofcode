#!python3

# Coroutine 

'''
A Coroutine is generator which is capable of constantly receiving input data, process input data and may or may not return any output.
Coroutines are majorly used to build better Data Processing Pipelines.
Similar to a generator, execution of a coroutine stops when it reaches yield statement.
A Coroutine uses send method to send any input value, which is captured by yield expression.
'''

def TokenIssuer():
    tokenId = 0
    while True:
        name = yield  # TokenIssuer is a coroutine function, which uses yield to accept name as input
        tokenId += 1
        print('Token number of', name, ':', tokenId)
t = TokenIssuer()  # 
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith') 

'''
Execution of coroutine function begins only when next is called on coroutine t.
This results in the execution of all the statements till a yield statement is encountered.
Further execution of function resumes when an input is passed using send, and processes all statements till next yield statement
'''

def TokenIssuer(tokenId=0):
    try:
       while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
next(t)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()

# First next function call can be avoided with a decorator

def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper

@coroutine_decorator  # coroutine_decorator takes care of calling next on the created coroutine t.
def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()

'''

Lab Question

#!/bin/python3

import sys



# Define the coroutine function 'linear_equation' below.

def linear_equation(a, b):
    while True:
        x = yield
        e = a*(x**2)+b
        print('Expression, '+str(a)+'*x^2 + '+str(b)+', with x being '+str(x)+' equals '+str(e))


if __name__ == "__main__":
    a = float(input())

    b = float(input())

    equation1 = linear_equation(a, b)
    
    next(equation1)
    
    equation1.send(6)
    
'''


'''

Lab Question : Linking coroutines

#!/bin/python3

import sys



# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args,**kwargs):
        c = coroutine_func(*args,**kwargs)
        next(c)
        return(c)
    return(wrapper)
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x= yield
        e = a*(x**2)+b
        print('Expression, '+str(a)+'*x^2 + '+str(b)+', with x being '+str(x)+' equals '+str(e))
    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    while True:
        y = yield
        equation1 = linear_equation(3, 4)
        equation2 = linear_equation(2, -1)
        # code to send the input number to both the linear equations
        equation1.send(y)
        equation2.send(y)
        
    
def main(x):
    n = numberParser()
    n.send(x)
    
if __name__ == "__main__":
    x = float(input())

    res = main(x);

'''
