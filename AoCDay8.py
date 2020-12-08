with open('Day7.txt', 'r') as data:
    data = data.read()
    data = data.split('\n')

#Part 1

accum = 0

i = 0 
while data[i] != 'fin':
    if data[i][:3] == 'acc':
        accum += int(data[i][4:])
        data[i] = 'fin'
        i += 1
    if data[i][:3] == 'nop':
        data[i] = 'fin'
        i += 1        
    if data[i][:3] == 'jmp':
        add = int(data[i][4:])
        data[i] = 'fin'
        i += add
    print(accum)

print(accum)
