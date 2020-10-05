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
