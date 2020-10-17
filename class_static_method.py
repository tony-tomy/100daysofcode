#!python3

# Class Method & Static Method

# Class Method

# A method defined inside a class is bound to its object, by default. 
# However, if the method is bound to a Class, then it is known as classmethod.

# Example 1 : method bound to object

class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)
print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount(c3)) # -> 3
#print(Circle.getCirclesCount()) # -> TypeError: getCirclesCount() missing 1 required positional argument: 'self'


# Example 2 : method bound to class

class Circle(object):
    no_of_circles = 0
    def __init__(self, radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    @classmethod
    def getCirclesCount(self):
        return Circle.no_of_circles
c1 = Circle(3.5)
c2 = Circle(5.2)
c3 = Circle(4.8)

print(c1.getCirclesCount())     # -> 3
print(c2.getCirclesCount())     # -> 3
print(Circle.getCirclesCount()) # -> 3

# Static Method

# A method defined inside a class and not bound to either a class or an object is known as Static Method.
# Decorating a method using @staticmethod decorator makes it a static method.

# Example 1 : square function  defined outside the class as independent entity
'''
def square(x):
        return x**2
class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    def area(self):
        return 3.14*square(self.__radius)
c1 = Circle(3.9)
print(c1.area())
print(square(10))
'''
# Example 2 : 

class Circle(object):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
c1 = Circle(3.9)
print(c1.area())  
#print(square(10)) # -> NameError : name 'square' is not defined

'''
the square method is defined inside the class Circle and decorated with staticmethod. Then it is accessed as self.square.

You can also observe that square method is no longer accessible from outside the class Circle
'''

print(Circle.square(10)) # -> 100
print(c1.square(10))     # -> 100


'''

Lab answers

import os
import sys

#Add circle class implementation here
class Circle(object):
    no_of_circles =  0
    def __init__(self,radius):
        self.__radius = radius
        Circle.no_of_circles += 1
    def area(self):
        return(round((3.14 * self.__radius * self.__radius),2))
    @classmethod
    def getCircleCount(self):
        return Circle.no_of_circles
    @staticmethod
    def getPi(self):
        return(3.14 * self.__radius)
        
 # Check the Tail section for input/output

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        circcount = list()
        lst = list(map(lambda x: float(x.strip()), input().split(',')))
        for radi in lst:
            c=Circle(radi)
            res_lst.append(str(c.getCircleCount())+" : "+str(c.area()))
        fout.write("{}".format(str(res_lst)))

'''