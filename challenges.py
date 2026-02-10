#Unique List challenge

'''def unique_nums(*nums):
    return tuple(set(nums))
print(unique_nums(5,7,8,9,5,4,8,9,6,3))'''

'''def unique_nums(*args):
    numbs = set(args)
    return list(numbs)


nums = input('enter numbers seperated by spaces:')

numbers = [int(n) for n in nums.split()]
unique = unique_nums(*numbers)
print(unique)'''

#Strong password checker challenge
def is_strong(password):
    msg = 'paaword must contain atleast'
    if len(password) < 8:
        return False, msg+'8 characters'
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    special_chars = set('!@#$%^&*+-')
    has_special = any(c in special_chars for c in password)

    if not has_upper:
        return False, msg+'one upper case letter'
    if not has_lower:
        return False, msg+'one lower case letter'
    if not has_digit:
        return False, msg+'one digit letter'
    if not has_special:
        return False, msg+'special characters'

    return True, 'password is strong'

password = input('enter password: ')
message = is_strong(password)
print(message)
