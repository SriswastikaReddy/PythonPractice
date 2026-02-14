#module is also called as library in other languages they are called as libraries or packages.
#modules contains predefined variables, functions, classes, objects
#exmples- math(from math import*) ,DataTime(import datetime as dt) , RegularExp(import re) there are three ways to import a module
#every python program can act as a modules
#how to write a Module?

data = 500
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b

if __name__ == '__main__':
    print('sum:', add(10, 5))
    print('diff:' ,sub(10, 5))
#print('Name:', __name__)      #for every python program file this is the buit-in variable and its value is main when it is runed as simple python program


