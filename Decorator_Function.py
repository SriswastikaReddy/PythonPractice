#Decorator Function - Closure function + function as parameter


def outer(f):
    def inner():
        print('*'* 10)
        f()
        print('*' * 10)
    return inner

@outer
def new():
    print('welcome')

#r = outer(new)
#r()

#new = outer(new)
new()







