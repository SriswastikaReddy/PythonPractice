#function is a piece of code that performs a specific task.function can be used multiple times, function takes parameters as input and give result as output. support team based develpment. built-in and user-defined
'''def fun1(<parameter>):
     ......
     ......
     return result'''

#find the volume of a cuboid
'''def volume(l,b,h):  #header contains name & formal parameters/arguments of a function
    cub = l*b*h
    return cub

cuboid = volume(10,5,3)  #function call (10,5,3 are actual parameters/arguments)
print(cuboid)'''

#positional vs keyword arguments
#positional - pass in same order, positional on left, keyword on right
#keyword  - pass in any order
''''def volume(l,b,h):
    print(l,b,h)
    cub = l*b*h
    return cub
#v = volume(10,5,3)
#v = volume(l=10,b=5,h=3)   #keyword arguments
v = volume(10, b=5,h = 3) #mixed arguments either psitional or keyword
print(v)'''

#Default Arguments - should fill from right side only, fun takes any type of argument, pass any type of argument
'''def volume(l=1,b=1,h = 1):
    print(l,b,h)
    cub = l*b*h
    return cub
#v = volume(10, 5, 3)
#v = volume(10,5)
#v = volume(10)
v = volume()

print(v)'''

'''def fun(a='sri',b=2.5, c =[1,2,3]):
    print(a,b,c)

#fun(5,10,[10,11])
fun()'''

'''def fun(l=[1,2,3]):
    l.append(len(l))
    print(l)
fun()
fun()
fun([10,11])
fun()'''

#Positional -only Arguments, / i end all positional only , / in begining invalid
#def fun(a,b,/,c,d): # before slash only positional after slash positional or keyword

'''def fun(a,/,b,c,d):
    print(a,b,c,d)

fun(1,2,3,4)
fun(1,2,c=3,d=4)'''

#keyword-only Arguments
'''def fun(a,b,*,c,d):   #after star keyword only before start can be keyword or positional
    print(a,b,c,d)
#fun(1,2,3,4)
fun(1,b=2,c=3,d=4)'''

#positional-only & Keyword-only Arguments
'''def fun(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
fun(5,10,15,d=20,e=3,f=5)'''


