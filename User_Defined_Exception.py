#User_Defined Exception

class NegativeException(Exception):


    def area(l,b):
        if l>0 and b>0:
            a = l*b
            return a
        else:
            raise NegativeException
    try:
        c = area(-3,4)
        print(c)
    except:
         print('NegativeDimensionexception')


