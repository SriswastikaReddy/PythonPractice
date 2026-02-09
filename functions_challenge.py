#Maximum of Three challenge

'''def max3(a,b,c,/):
    m = max(a,b,c)
    return m
print(max3(10,12,5))'''

#Simple Interest challenge

'''def simple_int(*,p,t,r):
    si = (p*t*r)/(100)
    return si
print(simple_int(p=50000,t=12,r=1.5))'''

#Pangram Phrase challenge
import re

def pangram(phrase):
    letters = re.sub(r'[^a-zA-Z]','',phrase)
    letter_set = set(letters.lower())
    print(letter_set)
    if len(letter_set) == 26:
        return True
    else:
        return False

str = input('Enter a phrase: ')
print(pangram(str))
