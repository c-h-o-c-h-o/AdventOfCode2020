with open('Day4.txt', 'r') as data:
    data_str = data.read()
    data_array = data_str.split('\n\n')

#print(data_array)

new_data = data_array
for i in range(len(data_array)):
    new_data[i]= data_array[i].replace('\n', ' ')

#print(new_data)

#byr (Birth Year)
#iyr (Issue Year)
#eyr (Expiration Year)
#hgt (Height)
#hcl (Hair Color)
#ecl (Eye Color)
#pid (Passport ID)
#cid (Country ID)

valid = 0
validPass = []
invalid = 0
for i in new_data:
    if 'byr:' in i and 'iyr:' in i and 'eyr:' in i and 'hgt:' in i and 'hcl:' in i and 'ecl:' in i and 'pid:' in i:
        valid += 1
        validPass.append(i)
    else:
        invalid += 1

print('There are', valid, 'valid passports')


#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

revised = validPass

for i in range(len(validPass)):
    revised[i] = validPass[i].split(' ')
#print(revised)

revised_again = revised

for i in range(len(revised)):
    for ii in range(len(revised[i])):
        revised_again[i][ii] = revised[i][ii].split(':')
#print(revised_again)

hcl_num = '0123456789'
hcl_char = 'abcdef'
ecl_lst = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


valid1 = 0
invalid1 = 0
for i in range(len(revised_again)):
    validentry = 0
    for ii in range(len(revised_again[i])):
        if revised_again[i][ii][0] == 'byr' and int(revised_again[i][ii][1]) >= 1920 and int(revised_again[i][ii][1]) <= 2002:
            validentry += 1
        if revised_again[i][ii][0] == 'iyr' and int(revised_again[i][ii][1]) >= 2010 and int(revised_again[i][ii][1]) <= 2020:
            validentry += 1
        if revised_again[i][ii][0] == 'eyr' and int(revised_again[i][ii][1]) >= 2020 and int(revised_again[i][ii][1]) <= 2030:
            validentry += 1
        if revised_again[i][ii][0] == 'hgt' and 'cm' in revised_again[i][ii][1] and int(revised_again[i][ii][1].replace('cm', '')) >= 150 and int(revised_again[i][ii][1].replace('cm', '')) <= 193:
            validentry += 1
        if revised_again[i][ii][0] == 'hgt' and 'in' in revised_again[i][ii][1] and int(revised_again[i][ii][1].replace('in', '')) >= 59 and int(revised_again[i][ii][1].replace('in', '')) <= 76:
            validentry += 1
        if revised_again[i][ii][0] == 'hcl' and '#' in revised_again[i][ii][1] and len(revised_again[i][ii][1].replace('#', '')) == 6:
            validhcl = 0
            for thing in revised_again[i][ii][1].replace('#', ''):
                if thing in hcl_num or thing in hcl_char:
                    validhcl += 1 
            if validhcl == 6:
                validentry += 1
        if revised_again[i][ii][0] == 'ecl' and revised_again[i][ii][1] in ecl_lst:
            validentry += 1
        if revised_again[i][ii][0] == 'pid' and len(revised_again[i][ii][1]) == 9:
            validentry += 1
                    
            
    if validentry == 7:
        valid1 += 1
    else:
        invalid1 += 1
    
print(valid1, invalid1)

#print('There are', valid, 'passports')