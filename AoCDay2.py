import csv
with open('Day2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ')
    data1 = []
    for row in reader:
        data1.append(row) 

#print(data1)

for lists in data1:
    lists[0] = lists[0].split('-')
    lists[1] = lists[1].replace(':', '')

#print(data1)

isValid = 0
notValid = 0
for lists in data1:
    if lists[2].count(lists[1]) >= int(lists[0][0]) and lists[2].count(lists[1]) <= int(lists[0][1]):
        isValid += 1
    else:
        notValid +=1
print('There are ' + str(isValid) + ' valid passwords.')
print('There are ' + str(notValid) + ' invalid passwords.')

#Part 2


for lists in data1:
    lists[0][0] = int(lists[0][0])-1
    lists[0][1] = int(lists[0][1])-1
#print(data1)

isValid = 0
notValid = 0

for lists in data1:
    cond_1 = int(lists[0][0])
    cond_2 = int(lists[0][1])
    if lists[2][cond_1] == lists[1] and lists[2][cond_2] != lists[1] or lists[2][cond_1] != lists[1] and lists[2][cond_2] == lists[1] :
        isValid += 1
    else:
        notValid +=1
print('There are ' + str(isValid) + ' valid passwords.')
print('There are ' + str(notValid) + ' invalid passwords.')
