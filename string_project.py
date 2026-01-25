#Palindrome project ex: madam
#palindrome phrase - 'Name now one man' - 'namenowoneman'
#Making a palindrome

'''phrase = input('Enter a phrase: ')
remove = phrase.replace(" ", "")
reverse = remove[::-1]
if remove.casefold() == reverse.casefold():
    print(f'Yes its a palindrome : {reverse}')
else:
    reverse = remove.casefold() + reverse.casefold()
    print(f'its not a palindrome but changed: {reverse}')'''


'''
#Anagrams Project - two or more words are framed using same set of words called Anagrams ex - decimal -> medical
S1 = input('Enter a string: ')
S2= input('Enter another string: ')


S1 = S1.lower()
S2 = S2.lower()

for x in S1:
    if x.isalpha():
        if S1.count(x) != S2.count(x):
            print('not anagrams')
            break
else:
    print('Anagrams')'''


#Data Cleaning Project
'''data ='These+notes#reveal9Newton seeking-out an(!underlying structure to/the\\pyramid'
clean = ''
for x in data:
    if x.isalpha() or x.isspace():
        clean += x
    else:
         clean = clean + ' '

print(clean)'''

#Resetting Password project
pass1 = input('Enter your password: ')
pass2 = input('Re-enter your password: ')
if pass1 == pass2:
    print('password changed')
elif pass1.casefold() == pass2.casefold():
    print('please check cases and try again')
elif pass1 != pass2:
    print('password do not match')












