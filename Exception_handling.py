#Types of errors
#syntax error(python(interpreter/Compiler) itself help to solve these) , logical error(not getting expected result, remove by using debuger), Runtime error(program is execuited but suddenly stops)
#

'''a = input('enter a number')
b = input('enter a number')

if a > b:
    print(a)
else:
    print(b)

c = a//b
print(c)'''

#Who Handles Errors?
#Developer- syntax and logical
#user - runtime error - 1. user input(may be he given differ type of input then expected)  2. File access 3.Datebase Connections 4.Internet Connections 5. Peripherals(print,mic etc)  if user gets any error in runtime develver should guide to give right input, these are called resourses
#develper should write the programs to handle those exception cases also which is called exception handling
#Resourses - y user gets errors as he was nt using the resources properly or providing resources properly

#Examples Of Exceptions

'''#Zero division error, Type error
a = int(input('enter a number: '))
#b = int(input('enter a number: '))
#b = 'x'

try:
    c = a // b
    print(c)
except ZeroDivisionError:
    print('you can\'t divide by zero')


print('program end')'''

#index error

'''l1 = [1,2,3,4,5]
try:
    index = 6
    print(l1[index])
except IndexError:
    print('index out of range')
except:
    print('something went wrong')

print('program end')'''


#key error
'''d = {1:'one',2:'two',3:'three',4:'four'}
print(d[8])'''

'''#ValueError
print(int('xyx'))'''


#Exception Handling - help to handle the program smoothly or else program will crash


'''a = 10
b = 0
try:
    c = a // b
    print(c)
except:
    print('invalid')

print('program end')'''


'''l = [1,2,3,4,5]
try:
    index = int(input('enter a number: '))
    print(l[index])
    print('end of try')
except:
    print('index out of range')

print('program end')'''

#Multiple Exception
'''l = [1,2,3,4,5]

try:
    index = int(input('enter a number: '))
    print(l[index])
except IndexError:
    print('index out of range')
except TypeError:
    print('index should be an integer')
except:
    print('something went wrong')


print('end of program')'''


l = [1,2,3,4,5]
try:
    index = int(input('enter a number: '))
    print(l[index])
except (IndexError,TypeError,ValueError) as a:
    print(a)
except:
    print('something went wrong')

print('program end')







