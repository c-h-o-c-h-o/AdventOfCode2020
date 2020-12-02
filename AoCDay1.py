import csv
with open('Day1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ')
    data1 = []
    for row in reader:
        data1.append(row) 

data = []
for i in data1:
    for ii in i:
        data.append(int(ii))

print(data)

for i in range(len(data)-1):
    for ii in range(len(data)-1-i):
        if data[i] + data[i+ii] == 2020:
            print(data[i], data[i+ii])
            print(data[i]*data[i+ii])

#Part 2

for i in range(len(data)-1):
    for ii in range(len(data)-1-i):
        for iii in range(len(data)-1-i-ii):
            if data[i] + data[i+ii] + data[i+ii+iii]== 2020:
                print(data[i], data[i+ii], data[i+ii+iii])
                print(data[i]*data[i+ii]*data[i+ii+iii])
        

    

        