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

