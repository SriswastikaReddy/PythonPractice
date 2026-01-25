'''l = [1, 2, 3,4,5,6]
l[1] = 9
#l[1:1] = [10]
#l[1:len(l)] = [11,12,13,14,15]
#l[1:len(l):2] = [11,12,13]
print(l)'''

'''l = [11,12,13]
l2 = l+[14]
print(l,l2)'''


#Weekly Wages
'''hours= input('Enter your 7 days working hours: ')
wage = int(input('Enter your hourly wage: '))
hours = hours.split()
week_hours = [int(x)for x in hours]  #list comprension
print(week_hours)
tot_hours = sum(week_hours)'''
'''tot_hours = 0
for x in week_hours:
    tot_hours += x'''
'''print(tot_hours)
extra_hours = tot_hours - 40
if tot_hours <= 40:
    final_wages = tot_hours * wage
    print('final_wages: ',final_wages)
else:
    final_wages = (40*wage)+(extra_hours*(wage*1.5))
    print('final_wages with extra hours: ',final_wages)'''


#2 table
'''table = int(input('Enter the table number: '))
s = 0
for i in range(1,11):
    s = table*i
    print(f'{table} x {i} = {s}')'''


#Remove duplicates

'''#l1 = [3,5,7,9,3,6,5,2,3,7]
l = input('Enter few duplicate numbers: ')
l = l.split()
l1 = [int(x)for x in l]
result = []
for i in l1:
    if i not in result:
        result.append(i)

print(result)'''

#Rotate a List challenge

'''l = input('Enter 1 to 6: ')
l1 = [int(x)for x in l.split()]
x= int(input('Enter the number of rotations: '))

l1 = l1[x:]+l1[:x]

print(l1)'''

#Palindrome list
'''l1 = input('Enter a list of elements: ')
first = [int(x) for x in l1.split()]
print(first)
rev = list(reversed(first))
#rev = first[::-1]
#rev = first.reverse()
print(rev)
if rev == first:
    print('palindrome')
else:
    print('not palindrome')'''


