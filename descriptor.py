#!python3

# Descriptors

'''
Python allows a programmer to manage the attributes simply with the attribute name, without losing their protection.

This is achieved by defining a descriptor class, that implements any of __get__, __set__, __delete__ methods.
'''
'''
class EmpNameDescriptor:
    def __get__(self, obj, owner):
        return self.__empname
    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value

class EmpIdDescriptor:
    def __get__(self, obj, owner):
        return self.__empid
    def __set__(self, obj, value):
        if hasattr(obj, 'empid'):
            raise ValueError("'empid' is read only attribute")
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value

class Employee:
    empid = EmpIdDescriptor()           
    empname = EmpNameDescriptor()       
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)  
e1.empname = 'Williams'
print(e1.empid, '-', e1.empname)
#e1.empid = 76347322  
'''

'''
The descriptor, EmpNameDescriptor is defined to manage empname attribute.

It checks if the value of empname attribute is a string or not.
'''

# Descriptors can also be created using property() type.

# It is easy to create a descriptor for any attribute using property()

'''
Syntax of defining a Property : property(fget=None, fset=None, fdel=None, doc=None)

where, 
fget : attribute get method
fset : attribute set method
fdel – attribute delete method
doc – docstring
'''

'''
class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    def getEmpID(self):
        return(self.empid)
    def setEmpID(self, value):
       if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
            self.empid = value

    empid = property(getEmpID, setEmpID)


def getEmpName(self):
    return self.__empname

def setEmpName(self, value):
    if not isinstance(value, str):
        raise TypeError("empname' must be a string.")
    self.__empname = value

def delEmpName(self):
    del self.__empname

empname = property(getEmpName, setEmpName, delEmpName)
e1 = Employee(123456, 'John')

print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
#print(e1.empname) #Raises 'AttributeError'
'''

# Normal Implementation

'''

class SimpleClass():
    x = 1
    y = 2

s = SimpleClass()

print(s.x)
print(s.y)
'''

# Descriptors implementation with __get__ and __set__

class DescriptorsClass():
    def __init__(self, initial_value = None, name = 'var'):
        self.value = initial_value
        self.name = name
    def __get__(self, obj, objtype):
        print('Retrieving ',self.name)
        return(self.value)
    def __set__(self, obj, val):
        print('Setting ',self.name)
        self.value = val

class SimpleClass():
    x = DescriptorsClass(1, 'Variable "x"')
    y = 2

s = SimpleClass()

print(s.x)
print(s.y)

s.x = 5

print(s.x)


# Propety Decorators

# Descriptors can be created with property decorators.  Ref. https://www.youtube.com/watch?v=jCzT9XFZ5bw

class Employee:
    def __init__(self, emp_id, emp_name):
        self.empid = emp_id
        self.empname = emp_name
    @property
    def empid(self):
        return self.__empid
    @empid.setter
    def empid(self, value):
        if not isinstance(value, int):
            raise TypeError("'empid' must be an integer.")
        self.__empid = value

    @property
    def empname(self):
        return self.__empname
    @empname.setter
    def empname(self, value):
        if not isinstance(value, str):
            raise TypeError("'empname' must be a string.")
        self.__empname = value
    @empname.deleter
    def empname(self):
        del self.__empname

e1 = Employee(123456, 'John')
print(e1.empid, '-', e1.empname)    # -> '123456 - John'
del e1.empname    # Deletes 'empname'
# print(e1.empname) #Raises 'AttributeError'

class Celsius( object ):
    def __init__( self, value=0.0 ):
        self.value= float(value)
    def __get__( self, instance, owner ):
        return self.value
    def __set__( self, instance, value ):
        self.value= float(value)
        
class Farenheit( object ):
    def __get__( self, instance, owner ):
        return instance.celsius * 9 / 5 + 32
    def __set__( self, instance, value ):
        instance.celsius= (float(value)-32) * 5 / 9

class Temperature( object ):
    celsius= Celsius()
    farenheit= Farenheit()

a = Temperature()
print(a)



'''  Lab output

#!/bin/python3

import sys
import os


# Add Celsius class implementation below.
class Celsius:

    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5



# Add temperature class implementation below.
class Temperature:

    celsius = Celsius()

    def __init__(self, initial_f):
        self.fahrenheit = initial_f
        
t1 = Temperature(32)
t1.celsius = 0           

        
#Check the Tail section for input/output
if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        t1 = Temperature(int(input()))
        res_lst.append((t1.fahrenheit, t1.celsius))
        t1.celsius = int(input())
        res_lst.append((t1.fahrenheit, t1.celsius))
        fout.write("{}\n{}".format(*res_lst))

'''

