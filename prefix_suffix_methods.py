#prefix & suffix - string methods
#startswith(prefix,start,end)
'''s1 = 'python is very easy'
#print(s1.startswith('python'))
print(s1.startswith('is',7))'''

#endswith(suffix,start,end)
'''s1 = 'python is very easy'
#print(s1.endswith('easy'))
print(s1.endswith('easy'))'''

#removeprefix(prefix)
'''s1 = 'python programming'
s2 = s1.removeprefix('python')
print(s2)'''

#removesuffix(suffix)
'''s1 = 'python programming'
s2 = s1.removesuffix("ming")
print(s2)'''

#partition(sep)
'''s1 = 'python is easy is'
s2 = s1.partition('is ')
print(s2)'''

#rpartition(sep)
'''s1 = 'python is very easy'
s2 = s1.rpartition('e')
print(s2)'''