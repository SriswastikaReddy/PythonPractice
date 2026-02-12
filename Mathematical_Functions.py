#Mathematical_Functions
#abs(x,/) - it will just give the psitive value
print(abs(-9))
print(abs(-70.25))

#pow(base,exp,mod=None,/)
print(pow(10,2))
print(pow(10,-2))
print(pow(10,2,3))

#round(number,ndigits=None)
print(round(10.4))
print(round(10.5))
print(round(5.5))    #when its .5 it takes nearest even number called Banker's rounding
print(round(3.54321))
print(round(3.56721,2))

#divmod(a,b,/)
print(divmod(61,7))

#min(iterable,*,key=None,default=None)
print(min([10,3,7,-2,6,1],key = abs))
print(min([],default= 'empty list'))

#max(iterable,*,key=None,default=None)
print(max(['apple','banana','cherry','blueberry'],key= len))

#sum(iterable,start=0,/)
print(sum([1,2,3,4]))
print(sum([1,2,3,4],start = 20))

#eval(expression,globals=None,locals=None)
global_var = {'x':5,'y':10}
local_var = {'z':3}
print(eval('10+20*4-5'))
print(eval('x+y-z',global_var,local_var))   #first it check local variable then global