#List_comprehansions
'''#L = [exp for item in iterable]
item = 'swastika'
#l = [x for x in item]
#l = [x for x in range(1,10)]
#l = [x**2 for x in range(1,5)]
#l = [x.lower() for x in 'PYThoN']
#l = [int(x) for x in '12345']
l = [x for x in 'ab*cd7e'if x.isalpha()]
print(l)'''

#Nested List
'''l = [1,2,[3,4]]
l1 = [[1,2,3],[4,5,6],[7,8,9]]
l3 = [[1,2,[3,4]],[5,6]]
print(l[2])
print(l1[2])
print(l3[0])
print(l3[0][2])'''

#Matrix
'''l1 = [[1,2,3],[4,5,6],[7,8,9]]
print(l1[2][2])'''

#print([[1,2,3],[4,5,6],[7,8,9]])


#split Odd & even
'''num = input('enter a list of numbers: ')
numbers = [int(x) for x in num.split()]
even = ([i for i in numbers if i%2 ==0])
odd = ([i for i in numbers if i%2 !=0])
print(even)
print(odd)'''

#Find Longest List challenge
'''nested_list = [[1,2,3],[4,5,6],[7,8,9],[10,12],[14,2]]

print(max(nested_list ,key = len))'''

