#isdigit()- for subscript& superscript it prints true
'''print('3456'.isdigit())
s2 = '7\u20823\u2075'
print(s2)
print(s2.isdigit())'''

#isdecimal() - decimal number system
'''s1 = '48962'
s2 = '\u0969\u096A\u096B'
print(s1.isdecimal())
print('4.56'.isdecimal())
print(s2.isdecimal())
print(s2)'''

#isnumeric()
'''s1 = '-3.75ab'
s2 = '\u0969\u096A\u096B'
print(s1.isnumeric())
print(s2.isnumeric())'''

#isascii()
s1 = '456'
print(s1.isascii())


#isalnum()
s1 = 'abcd_'
print(s1.isalnum())