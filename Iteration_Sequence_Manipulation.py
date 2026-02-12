#sorted(iterable,/,*,key=None,reverse=None)
l1 = [4,6,3,4,5,2,8,-3]
print(sorted(l1))
print(sorted(l1, reverse=True))
print(sorted(l1, key=abs))

#reversed(seq,/)
l1 = [4,6,3,4,5,2,8,-3]
s = reversed(l1)   #it creates reverse iterator
print(list(s))

#slice(start,stop,step)
l1 = [4,6,3,4,5,2,8,-3]
s = slice(5)   #here s is a object of slice whose size is 5
print(l1[s])    #applying it on list

#iter(callable, sentinel)
#next(iterator,default)
l = [4,6,3,4,5,2,8,-3]
it = iter(l)
print(next(it))
print(next(it))
print(next(it))

