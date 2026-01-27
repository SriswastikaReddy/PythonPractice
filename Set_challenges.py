'''words_set = {'plea','medical','listen','leap','decimal','silent','pale','enlist'}
result = set()
for x in words_set:
    for i in words_set:
        if x != i and sorted(x) == sorted(i):
           pair = tuple(sorted((x,i)))
           result.add(pair)


print(result)'''

#Plagarism check
'''import re
str1 = 'Time is the most valuable thing we have,and ones lost,it never returns'
str2 = 'we never get time back ones it"s gone-it"s truly the most valuable resource'
'''set_str1 = set(str1.lower().split())
set_str2 = set(str2.lower().split())
common_words = set_str1 & set_str2
unique_words = set_str1 ^ set_str2'''
word1 = re.findall(r'\w+', str1)
word2 = re.findall(r'\w+', str2)
wset1 = set(word1)
wset2 = set(word2)
common_words = wset1 & wset2
unique_words = wset1 | wset2
similarity = len(common_words) / len(unique_words)
if similarity >=0.5:
    print('high Potential plagarism',similarity)
else:
    print('low Potential plagarism')'''




