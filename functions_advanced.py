#!python3

#  Map function

def interest(amount):
    rate = 5
    year = 4
    return amount * rate * year / 100

amount = [1000, 5000, 7000]

interest_rate =list(map(interest, amount))

print(interest_rate)

name = ['cyril','kutty','jishnu']
cap = list(map(str.capitalize,name)) # map can be used with built in functions also
print(cap)

# Filter function

def eligibility(age):
    if(age>24):
        return True

age_list = [10,34,25,17,29]

age = filter(eligibility,age_list)

print(list(age))

# Reduce function

from functools import reduce

def add(a,b):
    return a+b

my_list = [1,2,3,4,5]

sum = reduce(add,my_list)

print(sum)

# Lambda with map

my_list = [10, 9 ,24, 16, 15, 25]

order = 2

result = map(lambda x : x ** order, my_list)

print(list(result))

# Lambda with filter 

even = filter(lambda x: x%2 == 0, my_list)

print(list(even))

# zip

from itertools import *

# Easy joining of two lists into a list of tuples
for i in zip([1, 2, 3], ['a', 'b', 'c']):  # python 3 zip works like izip of python 2.
    print(i)
# (1, 'a')
# (2, 'b')
# (3, 'c')

for i in zip (count(1), ['Emil','Cyril','Rahul']):   # count() generates consecutive integers 
    print(i)

# groupby() 

a = sorted([1,1,2,1,3,4,4,5,2,2,1,6,5])

for key, values in groupby(a):
    print(key,list(values))

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s." % (thing[1], key))
    print("")


# Passing function as argument in python

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout   # This assignment doesn’t call the function. 
               # It takes the function object referenced by shout and creates a second name pointing to it, yell.

print(yell('Hello'))

# Higer order functions

#Functions that can accept other functions as arguments are also called higher-order functions.

def shout(text):
    return text.upper()

def wisper(text):
    return text.lower()

def greet(func):
    # storing the fuction in a variable
    greeting = func('Hi, I am created by a fucntion passed as argument ')
    print(greeting)

greet(shout)
greet(wisper)

# Wrapper function or decorator

# allows programmers to modify the behavior of function or class

# importing libraries 
import time 
import math 

# decorator to calculate duration 
# taken by any function. 
def calculate_time(func): 
	
	# added arguments inside the inner1, 
	# if function takes any arguments, 
	# can be added like this. 
	def inner1(*args, **kwargs): 

		# storing time before function execution 
		begin = time.time() 
		
		func(*args, **kwargs) 

		# storing time after function execution 
		end = time.time() 
		print("Total time taken in : ", func.__name__, end - begin) 

	return inner1 



# this can be added to any function present, 
# in this case to calculate a factorial 
@calculate_time
def factorial(num): 

	# sleep 2 seconds because it takes very less time 
	# so that you can see the actual difference 
	time.sleep(2) 
	print(math.factorial(num)) 

# calling the function. 
factorial(10) 


########################################################################

def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("Before execution")
        
        # getting the returned value
        returned_value = func(*args, **kwargs)

        print("After execution")

        # returning the value to the original frame
        return returned_value

    return inner1

#adding decorator to the function
@hello_decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a+b

a, b = 7, 10

# getting the value throught the return of fucntion
print("Sum = " ,sum_two_numbers(a,b))

############################################################################

def decorate_msg(func):

    def addwelcome(str):
        return "Welcome to "+ func(str)

    return addwelcome

@decorate_msg
def site(site_name):
    return site_name

print(site("Google"))

############################################################################

# Decorators can also be useful to attach data (or add attribute) to functions.

# A Python example to demonstrate that 
# decorators can be useful attach data 

# A decorator function to attach 
# data to func 
def attach_data(func): 
	func.data = 3
	return func 

@attach_data
def add (x, y): 
	return x + y 

# Driver code 

# This call is equivalent to attach_data() 
# with add() as parameter 
print(add(2, 3)) 

print(add.data) 


