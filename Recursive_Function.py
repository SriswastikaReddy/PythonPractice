#Recursive function is a function which calls itself

'''def fun(n):     #Recursive function
    if n > 0:     #Base Condition
        print(n)
        fun(n-1)
fun(5)  #Recursive call'''

#Factorial of a Numbers
#n! = 1*2*3....*(n-1)*n
#n! = n*(n-1)!
#fact(n) = if n>0 then n*fact(n-1) ; if n<=0 then 1

'''def fun(n):
    if n <=0:
        return 1
    else:
        return n*fun(n-1)

print(fun(5))'''

