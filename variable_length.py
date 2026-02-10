
#Variable Length Positional Arguments
#*args is used for variable length arguments
#Tuple is created for variable length arguments
'''def fun(*args):
    #print(args)
    for x in args:
        if type(x) is int:
            print(x)

#fun(1,2,3,4,5,6,7,8,9,10)
#fun(1)
fun(1,2.5,'hello')'''

#fun(a,b,*args) a and b must be passed as positional-only

'''def fun(a,b,*args):
    print(a,b,args)

fun(1,2,3,4,5,6)'''

#fun(*args,a,b) a and b must be passed as keyword-only

'''def fun(*args,a,b):
    print(a,b,args)

fun(1,2,3,4,a=10,b=20)'''

'''def fun(*args):
    print(args,len(args))
L1 = [1,2,3,4,5]
#fun(L1)
fun(*L1)     #unpacking actual arguments'''

#Variable Length keyword arguments
#kwargs is used for variable length keyword arguments
#Dictionary is created for keyword arguments
'''def fun(**kargs):
    print(kargs)

fun(a=5,b=6,c=7)'''

'''def fun(**kargs):
    for item in kargs.items():
        if item[0] == 'a':
            print(item[1])

fun(a=5,b=6,c=7)'''
#fun(**kwargs,a,b) arguments not allowed after **kwargs
#fun(a,b,**kwargs) a and b can be positional or keyword
#fun(*args,**kwargs) *args should be *args should be on left
#fun(*args,a,b,**kwargs)a and b should keyword-only
'''def fun(a,b,**kargs):
    print(kargs,a,b)

fun(b=6,c=7,a=2)'''

#Multiple Returns Functions
'''def fun(a,b,c):
    sum = a + b + c
    prod = a * b * c
    return sum, prod

print(fun(a=5,b=6,c=7))'''

'''def result(mrk1,mrk2,mrk3):
    total = mrk1 + mrk2 + mrk3
    average = total / 3
    if average >= 45:
        grade = 'pass'
    else:
        grade = 'fail'
    return total,average,grade
print(result(55,70,80))'''



