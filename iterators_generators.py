#iterators & generators
#iter(iterable) gives an iterator on iterable
#next(iterator) gives element and move next

'''#L1 = [5,6,7,8,9]
#L1 = (5,6,7,8,9)
#L1 = {5,6,7,5,9}
#L1 = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
L1 = range(10)
it = iter(L1)
print(next(it))
print(next(it))
print(next(it))'''

#Generators
'''r = range(10)
print(r)'''

'''def myrange(n):
    i = 0
    while i < n:
        yield i
        i = i+1

my_ran = myrange(5)
print(next(my_ran))
print(next(my_ran))
print(next(my_ran))'''

'''def week():
    d = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    i = 0
    while True:
        yield d[i]
        i = (i+1) % len(d)
week = week()
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))
print(next(week))'''