#Local & Global Variable
#Local Variable - Declared inside a function
#Global Variables -
#declared outside a function, can be read inside all functions.
#Cannot be modified unless global g is declared
#Must be declared before function call


'''g = 2
print('outside-1:',g)
def fun():
    global g
    global a
    a = 10
    g = 12
    print('local:',a)
    print('global:',g)


fun()
print('outside-2:',g)
print('outside-3:',a)'''

'''x,y,z = 4,5,'sri'
def fun2():
    a,b,c = 1,2,3
    print(locals())
    print(globals())

fun2()
print(globals())'''
