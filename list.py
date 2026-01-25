#List  - ordered collection of  Heterogenous elements which is mutable and can have duplicates
#Methods to create list
'''L1 = [1,2,3,4]
L2 = [1.2,2.56,1.2,2.56]
L3 = ['john','sri','sai','teja']
L4 = list((2,3,4,6))
L5 = list('string')
L6 = []
print(L1, L2, L3)
print(L4, L5 , L6)

#Hertrogenous
L7 = [2,2.3,'sri',True,5+6j]
print(L7)
print(L7[-2])

#Mutable - (we can Modify elements); (we can add elements using var.append()); (remove element using var.(remove))
L7[0] = 15
L7.append('car')
L7.remove('sri')
print(L7)'''

#Indexing & Slicing
#Read Indexing
'''l1 = [1,2,3,4,5,6,7,8,9]
print(l1[-3])
x = l1[-3]
print(x)'''

#slicing
'''l1 = [3,6,9,12,15,18,21]
print(l1[4:0:-1])'''

#writing Indexing
'''l1 = [1,2,3,4,5]
l1[3] = 10
l1[4] = [6,5]
print(l1)
#slicing
l1[3:3] = [5]
l1[9:9] = [6,7]

print(l1) '''

#if you are mentioning only start and stop then you can give n number of elements ; if you mention step should mention exact number of elements

#l1[start:stop] = [any number of elements]
'''l1 = [1,2,3,4,5]
l1[1:1] = [10]
print(l1)
l1[1:4]=[10]
print(l1)
l1[1:4]=[6,15,9,4,8,9]
print(l1)'''

''''#l1[start:stop:step] = [exact number of elements]
l1 = [1,2,3,4,5]
#l1[::2] = [10,11,12]
l1[::-1] = [14,13,12,11,10]
#l1[3:0:-1] = [1,2,3]
print(l1)'''

#operations on List
#concatenation(+) ; repetition(*) ; Membership(in, not in) ; List Comparison(< <= > >= == != )
'''l1 = [1,2,3,4,5]
l2 = [1,2,3,4,5]
#print(l1+[10])
l1.extend([45,25,35])  #modify the first list
l3 = l1 + l2 #this create new list
print(l3)
print(l1)'''

'''l1 = [1,2,3]
l2 = l1*2
print(l2)'''

'''l1 = [1,2,3,4,5]
l2_N = [[1,2],[3,4],5]
l3 = ['red','blue','green']
print(3 not in l1)
print([3,4] in l2_N)
for x in l3:
    print(x)'''

'''l1 = [1,2,3]
l2 = [1,2,3]
l3 = [3,2,1]
l4 = [1,2,3,4]
l5 = [1,2,1]
l6 = [2]
print(l1 == l2)
print(l1 == l3)
print(l1 != l2)
print(l1 != l3)  #comparision is done in terms of elements
print(l1 > l5)
print(l6 > l5)'''

#List Traversals - visiting all the elements of a list
'''l1 = [1,2,3,4,5]
#for x in l1:
    #print(x)
#for x in range(len(l1)):
    #print(x, l1[x])
    
i = 0
while i<len(l1):
    print(l1[i])
    i += 1'''



