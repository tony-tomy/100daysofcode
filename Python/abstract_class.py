#!python3

# Abstarct Base Classes

'''
An Abstract Base Class or ABC mandates the derived classes to implement specific methods from the base class.
It is not possible to create an object from a defined ABC class.
Creating objects of derived classes is possible only when derived classes override existing functionality of all 
abstract methods defined in an ABC class.
an Abstract Base Class can be created using module abc
'''

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

# s1 = Shape() # TypeError: Can't instantiate abstract class Shape with abstract methods area, perimeter

'''
class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
c1 = Circle(3.9)  #TypeError: Can't instantiate abstract class Circle with abstract methods perimeter
'''
# Corrected code

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius
    @staticmethod
    def square(x):
        return x**2
    def area(self):
        return 3.14*self.square(self.__radius)
    def perimeter(self):
        return 2*3.14*self.__radius
c1 = Circle(3.9)
print(c1.area())