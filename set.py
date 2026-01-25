#unordered collection of distinct elements which are heterogenious and mutable
'''a = {1,2,3,4,5,6}
b = set('swastika')
d = set()
e = set([1,2,3,4,5,6])
f = set((1,2,3,4,5,6))
g = {}   # empty flower bracket is not a set
print(type(a),type(b),type(d),type(e),type(f))
print(a,b,d,e,f)
print(type(g))'''

#unordered
'''a = {20,10,5,30,40,60}
b = set('python')
print(a)
print(b)'''


#mutable
'''s1 = {10,20,30,40,50}
s1.add(100)
s1.add('hi')
s1.add((1,2,3))
#s1.add([4,5,6]) - list is not allowed only immutable values are allowed
print(s1)'''

'''s1 = {1,2,3,4,5,6}
for x in s1:
    print(x)
    
s1.remove(2)
s1.pop()
print(s1)'''

'''s = {10,20,30,40,50}
s.add(12)
print(s)'''

#Set Operations in Mathematics
'''#union - compileing the elemnts of two sets all together without any duplicates
a = {1,2,3,5,7}
b = {5,7,9,10,11}
aUb = {1,2,3,9,10,11}
# Intersection - common elements in two sets
a b = {5,7}
#Difference - take elements which are only present in one set
a-b = {1,2,3}

#Symmetric Difference - exclusive elements which are present in both
{1,2,3,9,10,11}'''

#Set Operations
#union(iterable)
s1 = {1,2,3,5,7}
s2 = {5,7,9,10,11}
s3 = s1.union(s2)
print(s3)
#intersection(iterable)
s4 = s1.intersection(s2)
print(s4)
#intersection_update(iterable)
#s5 = s1.intersection_update(s2)
#print(s1)

#difference(iterable)
s6 = s2.difference(s1)
print(s6)
#difference_update(iterable)
#s7 = s2.difference_update(s1)
#print(s2)
#symmetric_difference(iterable)
s8 = s1.symmetric_difference(s2)
print(s8)

#symmetric_difference_update(iterable)
s9 = s1.symmetric_difference_update(s2)
print(s1)