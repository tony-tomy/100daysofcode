#!python3

import logging

'''
logging.warning('A Warning')
logging.info('A info')
logging.error('An error')
logging.debug('Debugging')
'''
'''
def smart_divide(func):
    def wrapper(*args):
        a,b = args
        if b == 0:
            print('Oops cannot divide')
            return
        return(func(*args))
    return(wrapper)

@smart_divide
def divide(a,b):
    return(a/b)

print(divide.__name__)
print(divide(4,16))
print(divide(8,0))

'''
'''
d1 = dict()
d1 = {1,4}
print(d1)
d2 = {1:4}
print(d2)
d3[4+1] = 15
print(d3)
d4[3] = 9
print(d4)
'''
'''
class A:pass
class B(A) : pass
class C(object) : pass
class D(C) : pass

a = A()
b = B()
c = C()
d = D()

print(isinstance(a,type(b)))
print(issubclass(C,C))
print(isinstance(d,D))
print(issubclass(C,(D,A,B,C)))
'''
'''
import sys
print(sys.builtin_module_names)
'''
'''
z =10

def func(**kw):
    x = 1,2,3
    a,b,c = 1,2,3
    y = z
    d,e = 1,2,3 # error
    print(x)
    print(a,b,c)
    print(y)
    print(d,e)

print(func())
'''

'''
keys = [1,2,3]
values = ['a','b','c']
d = dict(zip(keys,values))
print(d)
'''
'''
class MyType(type): pass

class SubType(MyType): pass

class MyObject(object):
    __metaclass__ = MyType

print(MyType.__class__)
print(SubType.__class__)
print(MyObject.__class__)
'''
'''
import builtins
print(builtins.__dict__.keys())
'''

'''
def f1(a,b):
    f1.s = 'some value'
    return(a+b)

try:
    print(f1.s)
except Exception as e:
    print(str(e))

f1(3,4)

try:
    print(f1.s)
except Exception as e:
    print(str(e))

'''

'''
class class1:
    a=1
    def f1():
        a =2
        class1.a +=1
        print(class1.a)
        print(a)

class1.f1()
class1.f1()
'''
'''
a = (5)
print(type(a))
'''
'''
class MyError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return(repr(self.value))

try:
    print('Hello World')
    raise MyError('Oops something went wrong')
except MemoryError as e:
    print('Error Message :',e)
'''

'''
print('{0:$>2d} * {1:$>2d} = {2:$>2d}'.format(5,10,5*10))
'''
'''
def foo(n):
    if(n<3):
        yield 1
    else:
        return
    yield 2

n =2
f =foo(n)
for i in range(n): print(f.__next__())

n =5
f =foo(n)
for i in range(n): print(f.__next__())
'''
'''
class gradpa(object):
    pass

class father(gradpa):
    pass

class mother(object):
    pass

class child(mother,father):
    pass

print(child.__mro__)

'''
'''
import re

def f1(data):
    p = re.compile('(?P[A-Z]{2,3}) (?P[0-9]{3})')
    return(p.search(data))

obj = f1('CS 101')
num = obj[0], obj[1]
'''

'''
class Base(object):
    def __init__(self):
        print('Base Created')

class Child(Base):
    def __init__(self):
        super(Child).__init__()
        print('Child created')

b = Base()
c = Child()
'''

'''
def check_twice1(lst,ele):
    return(lst.count(ele)>1)

print(check_twice1([1,2,3,1,2],1))

def check_twice2(lst,ele):
    return(ele in lst and ele in lst[lst.index(ele)+1:])

print(check_twice2([1,2,3,1,2],1))

def check_twice4(lst,ele):
    try:
        lst.remove(ele)
        lst.remove(ele)
    except:
        return(False)
    return(True)

print(check_twice4([1,2,3,1,2],1))

'''

class Person(object):
    def __init__(self,name):
        print('My name is ',name)

class Bob(Person):
    def __init__(self,name= 'Bob'):
        print('My name is Bob')

def ClassID(self):
    print('I am the father')

class Sue(Person):
    def __init__(self,name = 'Sue'):
        print('My name is Sue')

def ClassID(self):
    print('I am the monther')

class Child(Bob,Sue):
    def __init__(self,name='X'):
        super(Child,self).__init__(name)

def ClassID(self):
    print('I am the child')

Ann = Child('Ann')
Ann.ClassID()