#Shuffle a List
import random as rd
from itertools import permutations

'''print(rd.random()*10)
print(rd.randint(1,10))
print(rd.randrange(1,10,2))
rd.seed(10)
for i in range(5):
    print(rd.randint(1,100))'''

'''l = ['a','b','c',1,2,3,4,5]
print(rd.choice(l))
print(rd.choices(l,k=4))'''

#num = input('Enter a number: ')
#number = [int(x) for x in num.split()]
#print(number)
'''number = [1,2,3,4,5]
for i in range(0,5):
    rd.shuffle(number)
    print(i)
    print(number)'''

#Generate Permutations
#function available in itertools module
#product(*iterable,repeat=1)
#combinations(iterable,r=None)

#permutations(iterable,r=None)
'''import itertools as it
list1 = ['a','b','c','d']
list2 = [1,2,3,4,5]
perms = it.permutations(list1,2)
comb = it.combinations(list1,2)
pro = it.product(list1,repeat = 2)
print(list(perms))
print(list(comb))
print(list(pro))'''

'''import itertools as it
# Given list of elements
lst = ['A', 'B', 'C', 'D']

# Generate all permutations of length 2
perms = it.permutations(lst, r=2)

# Convert iterator to list
perm_list = list(perms)

# Print header
print('Permutations')

# Print each tuple permutation
for t in perm_list:
    print(t)'''

#Mean - Median - Mode
'''import statistics as st
list = input("Enter elements separated by space: ").split()
list1 = [int(x)for x in list]
print(list1)
mean_value = st.mean(list1)
median_value = st.median(list1)
mode_value = st.mode(list1)
print(mean_value, median_value, mode_value)'''


