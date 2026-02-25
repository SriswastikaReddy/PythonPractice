#why try and except

'''a = 10
b = 0
try:
    c = a//b
    print(c)
except:
    print('b should not be o')

print('end of program')'''

'''a = 10
b = 0
if b != 0:
    c = a//b
    print(c)
else:
    print('b should not be 0')

print('end of a program')'''

'''def div(a,b):
    if b != 0:
        c = a//b
        return c
    else:
       return -1

k = div(10,-10)
if k != -1:
    print(k)
else:
    print('division by zero')'''

#functions also raise exception
'''def div(a,b):
    if b != 0:
        c = a//b
        return c
    else:
        raise ZeroDivisionError

try:
    k = div(10,-10)
    print(k)
except:
    print('division by zero')'''

#Exception Handling(else)  # else block is executed only if try block executes completely without exception

'''a = int(input('enter a number: '))
b = int(input('enter a number: '))
try:
    c = a//b      #only statement causing exception is written in try

except:
    print('division by zero')
else:
    print(c)     #dependent statement written in else block'''

#Exception Handling(finally)

'''def fun():
    try:
        x = int('abc')
        return x
    except Exception as e:
        raise e
    finally:
        print('end of function')

try:
    res = fun()
    print(res)
except:
    print('name error')'''

# when python program using resources like a file/database/network then the procedure is it should request for resources then open and use resources and close it or release them.
'''def fun():
    try:
        open resource  #for example it opened a resouce while using got an exception so in this case we finally block
        use resource

    except Exception as e:
        raise e
    else:
        return result
    finally:
        close resource'''





