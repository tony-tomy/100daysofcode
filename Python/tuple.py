#!python3

"""
Tuple : A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
"""

thistuple = ('apple','banana','cherry')

print(thistuple)

print(thistuple[1])

print(thistuple[-1])

# range of index

thistuple = ('apple','orange','banana','cherry','kiwi','mango')

print(thistuple[2:4])

# Remember that the first item has index 0.

print(thistuple[-4:-1])

"""
 Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
"""

x = ('apple','banana','cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

for i in thistuple:
    print(i)

if 'apple' in x:
    print("Yes, apple in the fruit tuple")

print(len(thistuple))

"""
Add Items
Once a tuple is created, you cannot add items to it. Tuples are unchangeable.
"""

"""
Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

thistuple = ('apple',)

print(type(thistuple))

print(thistuple)

# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely

del thistuple

# join two tuples

tuple1 = (1, 2, 3, 4)
tuple2 = ('a','b','c')

tuple3 = tuple1 + tuple2

print(tuple3)

"""
The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.
"""

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

"""
Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""