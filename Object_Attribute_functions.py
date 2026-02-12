#object attribute functions

#type(object,base=None,dict=None)
print(type(10))
print(type(None))
print(type([]))

#isinstance(object,classinfo,/) #check weather this object is instance of the class
x = 10
print(isinstance(x, int))
print(isinstance(x, float))
print(isinstance(x, str))
print(isinstance(x, (int,float)))
print(isinstance('sri',str))

#hasattr(object,attribute,default) checking if a string has a specified method or not(weather given class has so and so method or not)
text = 'hello'
print(hasattr(text,'lower'))
print(hasattr(text,'upper'))
print(hasattr(text,'search'))
print(hasattr(text,'find'))

#getattr(object,attribute,default) - if a class or module is having some members it gives  reference to that
import math
print(getattr(math,'pi'))
print(getattr(math,'sqrt')(25))

#id(object,/)
x =10
y =10
l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
print(id(x))
print(id(y))
print(id(l1))
print(id(l2))

#dir(object,/)- gives details of a class or module
print(dir(int))
print(dir(list))
print(dir(math))

#repr(object,/) - gives actual Representation of a data.
print(repr('hello world'))
