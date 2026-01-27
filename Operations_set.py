# | union
# & Intersection
# &= Intersection update
# - Difference
# -= Difference update
# ^ symmetric difference
# ^= symmetric difference update

a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}
'''print(a|b)
print(a&b)'''
'''a &= b
print(a)'''
'''b &= a
print(b)'''
'''print(a-b)
print(b-a)'''
'''a -= b
print(a)'''
print(a^b)
b^=a
print(b)


#Adding & Deleting
#add(element)
a = {1,2,3,4,5,6}
a.add(7)
print(a)

#update(iterable)
a.update((8,9))
a.update('sri')
print(a)

#copy()
b = a.copy()
print(b)

#pop()
a.pop()
print(a)

#discard(element)
a.discard(8)
print(a)
#remove(element)
a.remove(7)
print(a)

#clear()
a.clear()
print(a)

#Set Comprehensions
#s = {exp for item in iterable}
a = 'swastika'
s = {x for x in a}
print(s)