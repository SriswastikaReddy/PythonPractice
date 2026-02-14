#Function as an Object - if a language is treating function as an object then we call that type of function as first class functions.
#print(print.__name__)

'''show = print
show('sri')
take = input
a = take('give number: ')'''

def fun():
    print('hello')
f = fun
f()


#Nested Functions - function inside function

def outer():
    print('outer')
    def inner():
        print('inner')

    inner()
outer()

#Area of a cuboid
def totalarea(l,b,h):
    def area(d1,d2):
        return d1*d2
    return 2*(area(l,b)+area(b,h)+area(l,h))
print(totalarea(10,5,3))

