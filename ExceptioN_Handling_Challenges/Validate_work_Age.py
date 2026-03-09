#Validate work Age challenge

class ageexception(Exception):
        pass

def ageF(age):
    if age >= 18 and age <= 60:
        return True
    else:
        raise ageexception('age should be between 18 and 60')


try:
    age = int(input("Enter age: "))
    print(ageF(age))
except ageexception as e:
    print(e)
