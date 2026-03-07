def fun(a,b):
    if b != 0:
        c = a/b
        return c
    else:
        return ZeroDivisionError


try:
    res = fun(10,0)
    print(res)
except:
    print('Division by zero error')


