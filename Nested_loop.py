'''for i in range(1,4):
    for j in range(1,4):
        print(i,',',j,end=" ")
    print(" ")'''

#primes from 1 - 100
'''n = 100
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
    if count == 2:
       print(i)'''
#Patterns challenges
'''n = 5
for i in range (1,n+1):
    for j in range(1,n+1):
        print('*', ' ', end='')
    print(' ')'''

'''n = 5

for i in range(1,n+1):

    for j in range(1,i+1):
        print('*', ' ', end='')

    print(' ')'''

'''n = 6
for i in range(1,n):

    for j in range(1,n - (i-1)):

       print('*', ' ', end='')


    print(' ')'''

'''n = 5
for i in range(1,n+1):
    for s in range(1, i):
        print(' ', end=' ')

    for j in range(i,n+1):
        print('*',end=' ')

    print(' ')'''

'''n = 5
p = 5
for i in range(1,n+1):
    for s in range(n-i):
        print(' ', end=' ')

    for j in range(i):
        print('*',end=' ')

    print(' ')'''




