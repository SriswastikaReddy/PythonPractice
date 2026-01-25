#print("hello world")
'''length = int(input("enter length of a rectangle: "))
width = int(input("enter width of a rectangle: "))
area = length * width
print("the area of the rectangle is ", area)'''
from xmlrpc.client import Boolean

'''#Area of a circle
import math
r = int(input("enter radius of a circle: "))
area = math.pi * r * r
print("the area of the circle is ", area)'''

#convert km to miles
'''km = int(input("enter km value: "))
miles = km * 0.621371
print("the area in miles is ", miles)'''

#Calculate Displacement
'''v = 12
u = 5
a = 6
d = (v**2- u**2)/ (2*a)
print("the displacement of the circle is ", d)'''

#Formula for roots in Python
'''import math
a = 1
b = -5
c = 6
x1 = (-b+math.sqrt(b**2 - 4*a*c))/(2*a)
x2 = (-b-math.sqrt(b**2 - 4*a*c))/(2*a)
print("square roots of a equation: ", x1, x2)'''

#Arithmetic operations
'''a = 6
b = 5
c = 5
x = 10
#x = x+(a*b-c)
x += a*b-c
print(x)'''

#String Concatenation & Repetition
'''s = "sri "
#s += "10"
#s += str(10)
s *= 10
print(s)'''

#Float
'''a = 10.5
b = 12.5
c = a // b
d = a % b
#print(c,"\n" ,d)
print(f"{c}\n{d}")'''

#Boolean

'''a = True
b = True
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a // b
i = a ** b
print(a ,b ,c ,d ,e ,f ,g  ,h )'''

#Conditional Statements

# check a number is positive or Negative

'''a = int(input("enter a number: "))

if(a >= 0):
    print(f"{a} is positive")
else:
    print(f"{a} is negative")'''

#Compound conditional Statements
'''a = 5
b = 7
c = 3
print(a>b and a>c)'''

#Challenges using conditional statements
#ODD OR EVEN
'''a = int(input("enter a number: "))
if(a %2 == 0):
    print(f"{a} is even")
else:
    print(f"{a} is odd")'''
#eligible to vote

'''a = int(input("enter your age : "))
if(a >= 18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")'''

#Age check for work

'''age = int(input("enter your age: "))
if(age > 18 and age <60):
    print(f"as your age {age} is above 18 and below 60 you are eligible to work")
else:
    print("you are not eligible to work")'''

#Valid marks
'''marks = int(input("enter your marks: "))
if(marks >= 0 and marks <= 100):
     print(f"{marks} valid marks")
else:
     print(f"{marks} invalid marks")'''

#Gender Check
'''gender = input("enter your gender: ")
if(gender == "m" or gender == "M"):
    print("Male")
else:
    print("Female")'''

# Vowel or Consonant
'''a = input("enter an lowercase Alphabet: ")
if(a == 'a' or a == 'e' or a == 'i' or a =='o' or a== 'u'):
    print("vowel")
else:
    print("consonant")'''

#Exam Result
'''math = float(input("enter your math score: "))
physics = float(input("enter your physics score: "))
chemistry = float(input("enter your chemistry score: "))
if(math >=45 and physics >= 45 and chemistry >= 45):
    print("you are passed")
else:
    print("you are not passed")'''

#Nested if and elif
#Temperature check

'''temp = float(input("enter your temperature: "))
if(temp == 25):
    print("Normal")
elif(temp < 25):
    print("cold")
else:
    print("hot")'''

#if elif Ladder
#Generate Discounted Bill
'''Bill = float(input("enter your bill: "))
if(Bill < 1000):
    discount = Bill * 0.1
    fin_bill = Bill - discount
    #print("your final amount after discount is ", fin_bill)
elif(Bill >=1000 and Bill <5000):
    discount = Bill * 0.15
    fin_bill = Bill - discount
    #print("your final amount after discount is ", fin_bill)
elif(Bill >=5000 and Bill <10000):
    fin_bill = Bill - (Bill * 0.2)
    #print("your final amount after discount is ", fin_bill)
else:
    discount = Bill * 0.25
    fin_bill = Bill - discount
print("your final amount after discount is ", fin_bill)'''

#Day number to day name

'''day_no = int(input("enter day number: "))
if(day_no == 0):
    print("monday")
elif(day_no == 1):
    print("tuesday")
elif(day_no == 2):
    print("wednesday")
elif(day_no == 3):
    print("thursday")
elif(day_no == 4):
    print("friday")
elif(day_no == 5):
    print("saturday")
elif(day_no == 6):
    print("sunday")
else:
    print("please enter a valid day number")'''





