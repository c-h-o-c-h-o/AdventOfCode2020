import csv
with open('Day3.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ')
    data = []
    for row in reader:
        data.append(row) 
#print(data)

for i in range(len(data)):
    data[i] =  data[i]*(i+1)
    data[i] = ''.join(data[i])
#print(data[5:7])

#Right 3, down 1.

tree = 0
for i in range(len(data)-1):
    if data[i+1][3*(i+1)] == '#':
        tree += 1

print('There are', tree, 'trees.')

#Right 1, down 1.

tree1 = 0
for i in range(len(data)-1):
    if data[i+1][1*(i+1)] == '#':
        tree1 += 1

print('There are', tree1, 'trees.')

#Right 5, down 1.
tree2 = 0
for i in range(len(data)-1):
    if data[i+1][5*(i+1)] == '#':
        tree2 += 1

print('There are', tree2, 'trees.')

#Right 7, down 1.
tree3 = 0
for i in range(len(data)-1):
    if data[i+1][7*(i+1)] == '#':
        tree3 += 1

print('There are', tree3, 'trees.')

#Right 1, down 2.
tree4 = 0
for i in range(2,len(data),2):
    if data[i][int(i/2)] == '#':
        tree4 += 1

print('There are', tree4, 'trees.')

print(tree*tree1*tree2*tree3*tree4)