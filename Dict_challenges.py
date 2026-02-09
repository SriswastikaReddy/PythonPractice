#Login Tracker

'''users = ['john','bob','alex','alice','charlie','john','alex','alice','john','alex']
logins = {}
for username in users:
    if username in logins:
        logins[username] += 1
    else:
        logins[username] = 1

#print(logins)
for x,y in logins.items():
    print(f'{x:8} : {y} logins')'''

#Invert Dictionary

'''original = {'a':1, 'b':2, 'c':1, 'd':2, 'e':3, 'f':2}
inverted = {}
for x,y in original.items():
    if y in inverted:
        inverted[y].append(x)
    else:
        inverted[y] = [x]

for x,y in inverted.items():
    print(f'{x:2} : {y}')'''

#Isomorphic Strings
'''str1, str2 = 'paper', 'title'
flag = True
if len(str1) != len(str2):
    flag = False
else:
    map1, map2 = {}, {}
    for c1, c2 in zip(str1, str2):
        if c1 in map1:
            if map1[c1] != c2:
                flag = False
        else:
            map1[c1] = c2

        if c2 in map2:
            if map2[c2] != c1:
                flag = False
        else:
            map2[c2] = c1

if flag:
    print('Isomorphic String')
else:
    print('Not a Isomorphic String')'''

#List to Dictionaries
'''header = ['name', 'age', 'city']
data = [['James', 25, 'NY'],['Kiran', 30, 'DEL'],['Smith', 24, 'PAR'],
    ['Raj', 27, 'DEL']]
result = []
length = len(header)

for i in range(length):
    newdict = {}
    for row in data:
        if row[i] not in newdict:
            newdict[row[i]] = [row]
        else:
            newdict[row[i]].append(row)

    result.append(newdict)

print('Dictionares')
for i in range(length):
    print('\n'+header[i]+'\n')
    for key,value in result[i].items():
        print(f'{key:<10}: {value}')'''


#Dynamic Key Generation
#uuid1() - based on the current time and the computer's MAC address.
#uuid4() - generates a random UUID based on pseudo-random numbers.
#uuid3(namespace, name) - Generates a UUID by hashing a namespace identifier and a string using the MD5 algorithm.
import uuid
id = uuid.uuid1()
id1 = uuid.uuid4()
id3 = uuid.uuid3(uuid.NAMESPACE_OID, 'laptop')
print(int(id))
print(int(id1))
print(int(id3))
items = [['laptop',1200],['mouse',20],['keyboard',30],['computer',40]]
item_data = {}
for item in items:
    id = uuid.uuid5(uuid.NAMESPACE_OID, item[0])
    key = id.hex[:6]
    item_data[key] = item

print('item_data:')
for k,v in item_data.items():
    print(f'{k}: {v}')