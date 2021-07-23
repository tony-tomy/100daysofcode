#!python3

def my_function():
    print("Hello from function")

my_function()

def my_function(fname):
    print("Hello "+fname)

my_function("Alan")

# Arbitary arguments *args

def my_function(*args):
    print("The youngest child is "+ args[-1])

my_function("Emil","Max","Sam")

# Keyword arguments  : arguments order is not important

def my_function(child1,child2,child3):
    print("The elder child is "+child1)

my_function(child2="Max",child3="Sam",child1="Emil")

# Arbitary keyword arguments **kwargs

def my_function(**kwargs):
    print("His last name is "+kwargs["lname"])

my_function(fname = "sam", lname = "John")

# Default parametr value

def my_function(country = "Norway"):
    print("My country is "+country)

my_function(country="India")
my_function()

# Passing a list as arguments

def my_function(food):
    for x in food:
        print(x, end= " ")

fruits = ["Apple","Orange","Grapes"]

my_function(fruits)

print()

# Return values

def square_func(x):
    return x*x

print(square_func(9))

# The pass statement

"""
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

def myfunction():
  pass
"""

# Recursion

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
print()

# Lambda

"""
A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

lambda arguments : expression (syntax)
"""

x = lambda a : a + 10

print(x(5))

x = lambda a,b : a*b

print(x(5,6))

# Lambda as annonymous function inside a fucntion

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)   # Use that function definition to make a function that always doubles the number you send in

mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
