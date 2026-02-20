#Lambda Functions - Anonymous Functions they are simple single line functions, useful for functional programming

'''def double(x):
    return x * 2

k = lambda x:x*2   #lambda function
print(double(3))
print(k(3))'''


'''k = lambda x,y: x+y
print(k(3,4))'''

'''print((lambda x:x*2)(5))'''

'''#creat a list which are multiple of 3
l1 = [1,2,3,4,5,6,7,8,9]
k = filter(lambda x: x%3 == 0,l1)
print(list(k))'''

'''l1 = [1,2,3,4]
l2 = list(map(lambda x: -x,l1))
print(l1)
print(l2)'''

'''l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(map(lambda x: x if x%2==0 else -x ,l1))
print(l1)
print(l2)'''

l1 = [[4,2,'six'],[1,1,'two'],[1,2,'three']]
#print(sorted(l1))
l2 = sorted(l1,key = lambda x:x[0]+x[1])
print(l1)
print(l2)





