with open('Day9.txt', 'r') as data:
    data = data.read()
    data = data.split('\n')
    
for i in range(len(data)):
  data[i] = int(data[i])

############# Part 1 ############# 

#preample list
check = data[0:26]

#data list
data = data[26:]

#list of all possible pair-wise sums
sums = []
for i in range(len(check) - 1):
  for ii in range(1, len(check)-i):
    sums.append(check[i]+check[i+ii])

#create list of all non-sums
nonsums = []
for j in range(len(data)):
  if data[j] in sums:
    check = check[1:]
    check.append(data[j])
    for i in range(len(check) - 1):
      for ii in range(1, len(check)-i):
        sums.append(check[i]+check[i+ii])
  else:
    nonsums.append(data[j])
