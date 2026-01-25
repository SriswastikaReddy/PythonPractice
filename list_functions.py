#Adding elements
#append(element)
'''l = [1,2,3,4,5]
l.append(6)   #we can only add 1 element at a time
l.append(7)

print(l)
l.append('python')
print(l)'''

#extend(iterable)
'''l = [11,12,13]
l.extend([14,15])
l.extend('python')
l.extend(range(16,20))
print(l)'''

#insert(index,element)
'''l = [11,12,13]
l.insert(2,14)
print(l)'''

#copy()
'''l = [11,12,13]
l2 = l.copy()
l2.append(14)
print(l)
print(l2)'''

#Removing elements
#pop(index)
'''l = [11,12,13]
l.pop() #if you wont give any index it will delete default last element
print(l)'''

#remove(element)
'''l = [11,12,13,11]
l.remove(11)
print(l)'''

#clear()
'''l = [11,12,13]
l.clear()
print(l)'''

#del() - delete based on the index
'''l = [11,12,13]
#del l[0]
#del l[0:2]
del l
print(l)'''

#Index & Sorting
#index(element,start,end)
#count(element)
'''l = [1,2,3,4,5,2,3]
print(l.index(2,2,6))
print(l.count(3))

#reverse()
#l.reverse()
l2 = list(reversed(l))
print(l2)'''

#sort(*,key = None,reverse=false)
l = [1,2,3,4,5,2,3]
l2 = ['Black','cat','Coat','python']
l3 = ['apple', 'cat','Bat','Dog']
#l.sort() #by default create a list in increase order
l.sort(reverse = True) # key word argument
#l2.sort()
l2.sort(key = len)
l3.sort(key =str.lower)
print(l)
print(l2)
print(l3)

