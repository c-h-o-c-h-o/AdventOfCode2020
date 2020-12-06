import csv
with open('Day5.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ')
    data = []
    for row in reader:
        data.append(row) 

#Start by considering the whole range, rows 0 through 127.
#F means to take the lower half, keeping rows 0 through 63.
#B means to take the upper half, keeping rows 32 through 63.
#F means to take the lower half, keeping rows 32 through 47.
#B means to take the upper half, keeping rows 40 through 47.
#B keeps rows 44 through 47.
#F keeps rows 44 through 45.
#The final F keeps the lower of the two, row 44.


#Start by considering the whole range, columns 0 through 7.
#R means to take the upper half, keeping columns 4 through 7.
#L means to take the lower half, keeping columns 4 through 5.
#The final R keeps the upper of the two, column 5.

# Part 1.
for i in range(len(data)):
    data[i] = ''.join(data[i])

def fb(string):
    string = string[0:7]
    r = [0,127]
    cutoff = 63
    for i in string:
        if i == "F":
            r = [r[0],cutoff]
        else:
            r = [(cutoff+1),r[1]]
        cutoff = r[0] + (r[1] - r[0] - 1)/2 
    return r[0]

#print(fb("FBFBBFF"))

def rl(string):
    string = string[7:]
    r = [0,7]
    cutoff = 3
    for i in string:
        if i == "L":
            r = [r[0],cutoff]
        else:
            r = [(cutoff+1),r[1]]
        cutoff = r[0] + (r[1] - r[0] - 1)/2 
    return r[0]

#print(rl("FBFBBFFRLR"))

ID = []
for i in range(len(data)):
    ID.append(fb(data[i])*8 + rl(data[i]))
#print(ID)

sorted_IDs = sorted(ID)
print(sorted_IDs[-1])

#Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

seats = 0
for i in range(len(sorted_IDs)-1):
    if sorted_IDs[i+1] - sorted_IDs[i] > 1:
        seats = sorted_IDs[i]
        
print(int(seats) + 1)