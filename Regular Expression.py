#Regular Expression pattern matching
#module/library - collections of predefined functions , classes or objects
#functions
#from tarfile import ExtractError

#compile(pattern,flag =0)
#validtion

import re  #to use all the functions that are there in regular expression module
'''print(re.match('abc','abcdef') ) #match(pattern, string, flag = 0)
print(re.fullmatch('python','python').group())  #fullmatch(pattern, string, flag =0)'''

#Search and Extract
'''print(re.search('very','python is very easy').span())  #search(pattern, string, flag = 0)
print(re.findall('can','can you can a can as a canner'))  #findall(pattern, string, flag = 0)
                                 #split(pattern, string,maxlip =0, flag = 0)'''


#Text Processing - search and replace text
#Data Validation - check data is in proper format
#Extracting information - extracting info from large texts


#quantifiers - how much quantity is allowed or how much quantity is used for patterns
#(+) - 1 or more ; (*)- o or more ; (?) - o or 1 ; ({m})- exactly m ; ({m,n}) -- from m to n

'''print(re.fullmatch('(ab)+','ab'))
print(re.fullmatch('(ab)?',''))
print(re.fullmatch('(ab)*','ab'))
print(re.findall('[abc]+','123 abc 987 bbcc@cbacaaaccc'))'''

#Special Characters
#[...] set of possible characters
'''print(re.match('[A-Z][a-z]+ [A-Z][a-z]+ ','Swastika Reddy Sai Kishore '))
print(re.match('[A-Za-z_][A-Za-z0-9_]*','item1'))
print(re.match('[01][0-9]:[0-5][0-9]','12:00'))
print(re.match('[a-zA-Z0-9]+\.(com|org|net)$','final.com'))'''
#[^...] all characters except in bracket
# . any character except new line
#^ beginning of a string
#$ end of a string
#r|S - should match pattern R or S

#Escape Sequences
#\d - Digits[0-9] : \D non-digits(a-zA-Z+-{..} ; \w Alphanumeric[a-zA-Z0-9] ; \W Non-alphanumeric ; \s White space \t \f \r \n : \S - Non whitespace ; \A Starting of a string^ ; \Z End of a string$

print(re.match('\d{2}/\d{2}/\d+','01/14/2026'))
print(re.match('[\w_]{8,}','abc_12345'))
print(re.match('\w+\.?\w+\@\w+\.(com|org)\Z','my.id1@gmail.com'))