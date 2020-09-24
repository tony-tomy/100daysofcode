#!python3

#Dictionary : a collection which is unordered, changeable and indexed. 
#In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

print(thisdict)

print(thisdict['brand'])

print(thisdict.get('model'))

thisdict['year'] = 2019

print(thisdict)

#Loop through dictionary

for i in thisdict:
    print(i)

for i in thisdict:
    print(thisdict[i])

for i in thisdict.values():
    print(i)

for i,j in thisdict.items():
    print(i,j) 

if 'model' in thisdict:
    print("Yes, model is one of the keys in the dictionary")

print(len(thisdict))

#adding items in dictionary

thisdict['color'] = 'Red'

print(thisdict)

#removing items in dictionary

thisdict.pop('model')

print(thisdict)

#remove last added item
thisdict.popitem()

print(thisdict)

#delete a specific item

del thisdict['brand']

print(thisdict)

#delete whole dictionary

del thisdict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#clear a dictionary
thisdict.clear()
print(thisdict)


# copy a dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()

print(mydict)

#another method to copy

mydict = dict(thisdict)

print(mydict)

# Nested dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# The dict() constructor 

thisdict = dict(brand = 'Ford', model = 'Mustang', year = 2020)

print(thisdict)

"""
Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""