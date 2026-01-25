#Tuple is same as list but immutable
'''t1 = (1,2,3)
t2 = tuple([4,5,6])
t3 = tuple('swastika')
t4 = (2,)
t5 = 1,2,3,4,5,6,7,8,9,10
t6 = tuple(range(1,11))
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(type(t5))
print(t6)'''

#Tuple Comprehensions
'''#list = (*(x for x in range(1,5)),)
list = tuple(x for x in range(1,11))
t3 = tuple(x**2 for x in range(1,11))
print(list)
print(type(list))
print(t3)'''

#Indexing & slicing
'''l1 = (1,2,3,4,5,6,7,8,9,10)
print(l1[-1])
print(l1[0:9:2])'''

#Concatination & Repetition
'''l1 = (1,2,3)
l2 = (4,5,6)
l3 = l1 + l2
l4 = l1 * 3
print(l3)
print(l4)'''

#packing & unpacking
t1 = 1,2,3,4,5,6 #when u assign multiple values to single variable python creates tuple called packing
a,b,c,d,e,f = t1 #unpacking  taken all elements from tuple and assigned to variables
x,y,*z = t1
*p,q,r = t1
s,*r,i = t1
print(a,b,c)
print(x,y,z)
print(p,q,r)
print(s,r,i)
print(t1)

'''t2 = [1,2,3]
a,b,c = t2
print(a,b,c)'''


