#Dictionary - is a collection of key value pair
'''d1 = {1:'one', 2:'two', 3:'three'}
d2 = {1:3.5, 2:'four', 2.5: True}
d3 = {4:[4,5], 5:(6,7), 9:{4,9,11}}
d4 = {(5,6):'hi'}
d1[3] = 'tres'
d1[5] = 'five'
print(d1[1])
print(d1)
for x in d1:
    print(x,d1[x])'''

#Dictionary create methods
#iterable pairs
#Zip function
#enumerate function

'''d1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
d = [(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]
z1 = [1,2,3,4,5]
z2 = ['one','two','three','four','five']
print(dict(zip(z1,z2)))
print(dict(enumerate(z2,2)))
print(d1)
print(dict(d))'''

#Dictionary Comprehension
'''d1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
l1 = [(1,'one'),(2,'two'),(3,'three'),(4,'four'),(5,'five')]
z1 = [1,2,3,4,5]
z2 = ['one','two','three','four','five']
#d2  = {x:y for x,y in l1}
#d2 = {x:y for x,y in zip(z1,z2)}
d2 = {x:y for x,y in enumerate(z2,1)}
print(d2)'''


#Methods available in Dictionary Loop over

'''#keys()  - give all the keys of a dictionary
d1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
print(d1.keys())
for x in d1.keys():
    print(x,d1[x])

#values()
print(d1.values())
for x in d1.values():
    print(x)

#items()
print(d1.items())
for x,y in d1.items():
    print(x,y)

#get(key,alt_value)
print(d1.get(4))
print(d1.get(6,'missing'))

#setdefault(key,alt_value)
#print(d1.setdefault(6))
print(d1.setdefault(6,'unknown'))
print(d1)'''


d1 = {1:'one', 2:'two', 3:'three', 4:'four'}
d2 = {5:'five'}

#update(dictionary)
d1.update(d2)
print(d1)

#fromkeys(sequence,default)
l1 = [1,2,3,4,5]
d3 = dict.fromkeys(l1,'sri')
print(d3)

#copy()
d4 = d1.copy()
print(d4)

#pop(key,alt_value)
d1.pop(1)
d1.pop(7,'not available')
print(d1)

#popitem()-recent entry will be removed
x = {1:'one', 2:'two', 3:'three', 4:'four'}
x.popitem()
print(x)

#clear()
x.clear()
print(x)
