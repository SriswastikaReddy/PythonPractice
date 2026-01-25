'''n = 5
while(n>0):
    print(n)
    n = n-1'''

#Simple table program

'''n = 5
i = 0
while (i<10):
    i = i+1
    print(n,'X', i, '=' , i*n)'''

#Digit of a number
'''n = int(input('Enter a number: '))
while n>0:
    r = n % 10
    print(r)
    n = n // 10
print(n)'''

#Count Digits of a Number

'''n = int(input('Enter a number: '))
count = 0
while(n>0):
    n = n // 10
    count = count + 1

print("number of digits:", count)'''

#Sum of digits of a Number

'''n = int(input('Enter a number: '))
sum = 0
while n>0:
    sum = sum + n % 10
    n = n // 10
   

print("sum of a given digit", sum)'''

#Reverse a number

'''n1 = int(input('Enter a number: '))
reverse = 0
n2 = n1
while n2>0:
    reverse = reverse * 10 + (n2 % 10)
    n2 = n2 // 10
print("Reverse of a number", reverse)

if reverse == n1:
    print(" yes number is palindrome ")
else:
    print(" no its not palindrome")'''

#Summation Logic
'''n = int(input('Enter a number: '))
i = 0
sum = 0
while i<n:
    i = i + 1
    sum = sum + i
print("sum of a given number is : ", sum)'''

#Sum of n Numbers
'''n = 5
i = 0
sum = 0
print('enter', n ,'numbers')
while (i<n):
    i = i + 1
    x = int(input('Enter a number: '))
    sum = sum + x

print("sum of a given number is : ", sum)'''

#Find Maximum element

'''n = 5
x = int(input('Enter a number: '))
max = float('-inf')
min = float('inf')
i = 0
while i<n:
   x = int(input('Enter a number: '))
   i = i + 1
   if x>max:
       max = x
   if x<min:
       min = x

print(f'The largest number is: {max} \n The smallest number is: {min}')'''

#infinite break
'''i = 0
while True:
    i = i + 1

    if i >10:
        break

    print(i)'''

#Continue Statement

'''i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)'''

#else suite with while Loop
'''i = 0
while i < 10:
    i = i + 1
    if i == 10:
        break
    print(i)
else:
    print("end of loop")

print("end of program")'''


