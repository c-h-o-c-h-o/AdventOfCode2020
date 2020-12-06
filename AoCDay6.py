with open('Day6.txt', 'r') as data:
    data_str = data.read()
    data_array = data_str.split('\n\n')

#print(data_array)

new_data = data_array
for i in range(len(data_array)):
    new_data[i]= data_array[i].replace('\n', ' ')
#print(new_data)

#Part 1

letters = 'abcdefghijklmnopqrstuvwxyz'
count = 0 

for i in new_data:
    unique = []
    for ii in i:
        if ii in letters and ii not in unique:
            unique.append(ii) 
            count +=1
print(count)

#Part 2

data2 = new_data
for i in range(len(new_data)):
    data2[i] = new_data[i].split(' ')
#print(data2)

answer = 0
for i in data2:
    unique = []
    people = len(i)
    for ii in i:
        for chars in ii:
            if chars not in unique:
                unique.append(chars)
    for unique_char in unique:
        yes = 0
        for ii in i:
            if unique_char in ii:
                yes += 1
        if yes == people:
            answer += 1
print(answer)
