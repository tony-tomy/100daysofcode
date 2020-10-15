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
