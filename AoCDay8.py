with open('Day8.txt', 'r') as data:
    data = data.read()
    data = data.split('\n')
#print(data)

accumulator = 0
i = 0
while data[i] != 'fin':
    if data[i][0:3] == 'acc':
        accumulator += int(data[i][4:])
        data[i] = 'fin'
        i += 1 
    if data[i][0:3] == 'nop':
        accumulator += 0
        data[i] = 'fin'
        i += 1
    if data[i][0:3] == 'jmp':
        add = int(data[i][4:])
        data[i] = 'fin'
        i += add

print(accumulator)

