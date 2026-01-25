#It prints <class ‘str’> - it means object hello is created in class type string.
'''s1 = 'hello'
print(type(s1))'''

#class str contains data and operations perform on that data.
#class: we group related data and methods or operations related to that data.

#methods of class str
'''s1 = 'hello'
print(type(s1))'''
#s1.#will show methods related to that class
#If you want to see any methods available in particular class there is a function called dir.
'''print(dir(str))
help(str)'''

#find & index - string methods

#find(sub,start,end)
'''s = 'hello how are you'
#x =s.find('how')
x = s.find('o',5,10)
x = s.find('k') #this gives -1 as k is not there in string
print(x)'''

#rfind(sub,start,end)
'''s = 'hello how are you'
#x = s.rfind('o')
x = s.rfind('how',4,9)
print(x)'''

#index(sub,start,end) - works same as find
'''s = 'hello how are you'
#x = s.index('o')
x = s.index('h')  # this gives error instead of -1 this is difference b/w find method & index
print(x)'''

#rindex(sub,start,end)
'''s = 'hello how are you'
x = s.rindex('o',5,9)
print(x)'''

#count(sub,start,end)
'''s = 'hello how are you'
#x = s.count('o')
x = s.count('h',4,7)
print(x)'''

#Alignment & padding methods

#ljust means left justify string
#ljust(width,fillChar)
'''s = 'hello'
x = s.ljust(6,'o')
print(x)'''

#rjust means right justify string
#rjust(width,fillChar)
'''s = 'hello'
x = s.rjust(6,'*')
print(x)'''

#center - center alignment
#center(width,fillChar)
'''s = 'hello'
x = s.center(7,'*')
print(x)'''

#zfill- zero fill on left
#zfill(width)
'''s = 'hello'
x = s.zfill(6)
print(x)'''

#Strip Methods - string methods
#lstrip(chars)
#s = '    hello'
'''s = '**hello'
x= s.lstrip('*')
print(x)'''

#rstrip(chars)
'''s = 'hello**'
x = s.rstrip('*')
print(x)'''

#strip(chars)
'''s = '**hello**'
x = s.strip('*')
print(x)'''

'''s = '#%$hello753'
x = s.strip('#$%o735')
print(x)'''