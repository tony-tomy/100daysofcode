#!python3

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# All classes have a function called __init__(), which is always executed when the class is being initiated

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):  # Object Methods
        print("Hello my name is ",self.name)

p1 = Person("John", 24)

print(p1.name , p1.age)
p1.myfunc()

"""
Note : The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
"""

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40  # modify object properties

print(p1.age)

# delete object properties

del p1.age

# delete objects

del p1


# Python __str__()

# This method returns the string representation of the object. 
# This method is called when print() or str() function is invoked on an object.

# This method must return the String object. If we don’t implement __str__() function for a class, then built-in object implementation 
# is used that actually calls __repr__() function.

# Python __repr__()

# Python __repr__() function returns the object representation. 
# It could be any valid python expression such as tuple, dictionary, string etc.

# This method is called when repr() function is invoked on the object, in that case, __repr__() function must return a String 
# otherwise error will be thrown.

# Example 1

class Person:
  name = ''
  age = 0
  def __init__(self,name, age):
    self.name = name
    self.age = age

p = Person("Anson",26)

print(p.__str__())
print(p.__repr__())

# Example 2


class Person:
    name = ""
    age = 0

    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def __repr__(self):
        return '{name:'+self.name+', age:'+str(self.age)+ '}'

    def __str__(self):
        return 'Person(name='+self.name+', age='+str(self.age)+ ')'


p = Person('Pankaj', 34)

# __str__() example
print(p)
print(p.__str__())

s = str(p)
print(s)

# __repr__() example
print(p.__repr__())
print(type(p.__repr__()))
print(repr(p))
