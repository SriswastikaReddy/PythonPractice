#Fibonacci Series
'''def fib(n):
    a,b = 0,1
    for i in range(n+1):
        yield a
        a,b = b,a+b
num = 10
for term in fib(num):
    print(term,end=',')'''

#Flatten Nested List challenge

'''def flatten(L):
    for i in L:
        if hasattr(i,'__iter__'):
            yield from flatten(i)
        else:
            yield i


L = [1,2,[3,4,[5,6,7],8],9,[10,11]]
flat = flatten(L)
flat_list = list(flat)
print(flat_list)'''

#Months Name Generator challenge
import calendar as cal
'''print(cal.MONDAY)
print(cal.JANUARY)
print(cal.day_name[0])
print(cal.day_name[1])
print(list(cal.day_name))
print(list(cal.day_abbr))
print(list(cal.month_name))
print(cal.prmonth(2020,1))'''

def next_month():
    count = 1
    while True:
        name = cal.month_name[count]
        yield name
        count = count % 12 + 1

m = next_month()
print(next(m))
print(next(m))