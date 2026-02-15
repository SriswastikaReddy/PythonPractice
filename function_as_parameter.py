#Function as Parameter - function takes function as parameter. If a function is taking another function as a parameter then its called Higher Order. Function
'''def welcome():
    print('welcome')

def fun(f):
    f()

fun(welcome)'''


'''def add(a, b):
    return a+b
def sub(a, b):
    return a-b

def arithmatic(f,a,b):
    return f(a,b)
a = 10
b = 5
plus = arithmatic(add,a,b)
print(plus)
minus = arithmatic(sub,a,b)
print(minus)'''


#Returning a Function - Outer Function Returns Inner Function, even if one function returns another function then its called higher order function.

'''def outer():
    def inner():
        print('welcome')

    return inner
f = outer()
f()'''

#Closure Function- it is a nested function, it returns function & Inner function Access Outer Variable.
'''def Outer(a):
    #a = 'welcome'
    def inner():
        print('*' * 10)
        print(a)
        print('*' * 10)

    return inner

f = Outer('welcome')
f()'''

def outercount():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

c1 = outercount()
c2 = outercount()
print(c1(),c1(),c1(),c1())
print(c2(),c2(),c2(),c2())

