#ASCII Codes - American standard code for information Interchange(0-127)
#characters are also represented in numeric form which is called as ASCII code. ex: A(65), B(66)..Z(90)
#a(97)...z(122), for every character in keyboard we have codes, 0(48)..9(57)

'''print(ord('A')) #GIVES ASCII VALUE
print(ord(' '))
print(chr(97)) #gives character for a given ASCII
print(chr(123))
print(chr(127))
print(chr(55))
print(ord('7'))'''

#Unicode - for every language there is a separate codes combined together called unique codes
'''s = '\u03b1\u03b2\u03b3\u03b4\u03b5'
print(s)
a = '\u0C38\u0C4D\u0C35\u0C38\u0C4D\u0C24\u0C3F\u0C15'
print(a)'''

#escape Sequences
''''# - new line- print coming word in line
print('hello\nworld')'''

#\r - carriage return- move curser to the beginning and overwrite.
'''print('valid\rso')'''

#\f - line feed - move to the next line but to the same column
'''print('step1\fstep2')'''

#\t - tab
'''print('hello\tworld')'''

#\v - vertical tab
'''print('hello\vworld')'''

#\b - backslash
'''print('hello\b')'''

#\a - alert
'''print('completed\a')'''

#\ - ignore  newline
'''print('line1\
line2')'''

#\\ back slash- for printing backslash
'''print('C:\\')'''

#\'quote
'''print('sri\'s')'''

#o octal value
'''print('\101\102')'''

#\xhh
'''print('\x41\x42')'''
#\uxxxx - 4 Digit hexa - to mention unicode
'''print('\x41')
print('\u0041')
print('\u00000041')'''

#\N{name} - name in unicode database
'''print('\N{dollar sign}')
print('\N{registered sign}')
print('\N{grinning face}')'''

#print Function
#separator
'''print('hi',13,45.6)
#Signature of print Method - The name of a function and  the parameters it takes
#print(object,sep='',end = '\t', file = sys.stdout, flush = False) - object(positional argument), sep(keyword argument)we give name f the arugument and value of the argument
print('hi',45,8, sep = '-')
print('hi',8,9.2, sep = '*')'''

'''#end of line
print('hello',end = ' \t')
print('world')'''

#C Style Printing
#srting(%s string), float(% float, %F Float, %g General Float, %e Scientific, %E Exponent ) integer(%d Decimal, %i integer, %o octal, %x Hexadecimal)
'''item = 'Memory'
size = 32
price = 11.75
print('Cost of %dGB %s is $%f'%(size,item,price))'''

'''data = 200
data1 = 45
print('%d %i %o'% (data,data1,data))'''

'''data = 23.45
print('%f %F %g %e %E'% (data,data,data,data,data))
print('%2.5f %2F %5d'%(data,data,data))'''

#Python's Formatted printing
'''name = 'sri'
roll = 10
avg = 78.5
print('name - {} roll - {} avg - {}'.format(name,roll,avg))'''
#in place holders{} you can also add width & precision, flag:< :^ :> :+ :- , conversion d b o x f F g e E , - %
item = 'memory'
size = 32
price = 11.75
#print('{1}GB {2} in ${0}'.format(price,size,item))
#width & precision
'''print('start {0:15} end'.format(size))
print('start{0:<15} end'.format(size))
print('start{0:^15} end'.format(size))'''

#conversions
'''size = 1234568977
print('start{0:^15,} end'.format(size))
print('start{0:^15_} end'.format(size))
print('start{0:^15o} end'.format(size))
print('start{0:^15E} end'.format(size))'''

#simple way
print(f'{size}Gb {item:^10} in ${price:o}')