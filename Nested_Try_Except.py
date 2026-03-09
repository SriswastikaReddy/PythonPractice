'''l = [10,20,30,40,50]

try:
    index = int(input('Enter a number: '))
    print(l[index])
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)'''

#NestedTryExcept

l = [10,20,30,40,50]

try:
    try:
        index = int(input('Enter a number: '))
    except ValueError as e:
        print(e)

    print(l[index])

except IndexError as e:
    print(e)
except NameError as e:
    print(e)


