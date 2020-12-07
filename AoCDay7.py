with open('Day7.txt', 'r') as data:
    data = data.read()
    data = data.replace('.', '')
    data = data.split('\n')
    
#print(data)

for i in range(len(data)):
    data[i] = data[i].split(' contain ')

#print(data)

names = []
bags = []
counter = 0
for i in data:
    if 'shiny gold' in i[1]:
        counter +=1
        bags.append(i[0].replace(' bags ', ''))
        names.append(i[0].replace(' bags ', ''))

baggy_bags = []
for i in data:
    for ii in bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            baggy_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

baggier_bags = []
for i in data:
    for ii in baggy_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            baggier_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

how_many_bags = []
for i in data:
    for ii in baggier_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            how_many_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

too_many_bags = []
for i in data:
    for ii in how_many_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            too_many_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

so_many_bags = []
for i in data:
    for ii in too_many_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            so_many_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

many_bags = []
for i in data:
    for ii in so_many_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            many_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

manyyy_bags = []
for i in data:
    for ii in many_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            manyyy_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

much_bags = []
for i in data:
    for ii in manyyy_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            much_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

mucho_bags = []
for i in data:
    for ii in much_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            mucho_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

muchoo_bags = []
for i in data:
    for ii in mucho_bags:
        if ii in i[1] and i[0].replace(' bags ', '') not in names:
            muchoo_bags.append(i[0].replace(' bags ', ''))
            names.append(i[0].replace(' bags ', ''))
            counter +=1
#print(counter)

#Part 2


for i in data:
    i[1] = i[1].split(', ')
#print(data)

gold = []
for i in data:
    if 'shiny gold' in i[0]:
        gold.append(i[1]) 
#print(gold)
#2 dark brown, 2 mirrored coral, 1 faded olive, 1 posh bronze
#for i in gold:
#    for ii in i:
        #print(ii[2:])

dark_brown = []
for i in data:
    if 'dark brown' in i[0]:
        dark_brown.append(i[1]) 
#print(dark_brown)
#2 shiny olive, 1 dull aqua

shiny_olive = []
for i in data:
    if 'shiny olive' in i[0]:
        shiny_olive.append(i[1]) 
#print(shiny_olive)
#no other bags

dull_aqua = []
for i in data:
    if 'dull aqua' in i[0]:
        dull_aqua.append(i[1]) 
#print(dull_aqua)
#no other bags

########################
dark_brown_total = 2*3
########################

#2 mirrored coral

mirrored_coral = []
for i in data:
    if 'mirrored coral' in i[0]:
        mirrored_coral.append(i[1]) 
#print(mirrored_coral)
#3 pale aqua bags

pale_aqua = []
for i in data:
    if 'pale aqua' in i[0]:
        pale_aqua.append(i[1]) 
#print(pale_aqua)
#1 dim red bag

dim_red = []
for i in data:
    if 'dim red' in i[0]:
        dim_red.append(i[1]) 
#print(dim_red)
#2 light violet, 4 clear coral

light_violet = []
for i in data:
    if 'light violet' in i[0]:
        light_violet.append(i[1]) 
#print(light_violet)
#2 dark crimson, 3 dark gray, 5 muted gold

dark_crimson = []
for i in data:
    if 'dark crimson' in i[0]:
        dark_crimson.append(i[1]) 
#print(dark_crimson)
#no other bags

dark_gray = []
for i in data:
    if 'dark gray' in i[0]:
        dark_gray.append(i[1]) 
#print(dark_gray)
#no other bags

muted_gold = []
for i in data:
    if 'muted gold' in i[0]:
        muted_gold.append(i[1]) 
#print(muted_gold)
#no other bags

clear_coral = []
for i in data:
    if 'clear coral' in i[0]:
        clear_coral.append(i[1]) 
#print(clear_coral)
#1 muted gold, 5 drab magenta, 5 bright tomato

drab_magenta = []
for i in data:
    if 'drab magenta' in i[0]:
        drab_magenta.append(i[1]) 
#print(drab_magenta)
#3 dark crimson, 1 muted gold, 3 posh silver, 2 dull aqua

posh_silver = []
for i in data:
    if 'posh silver' in i[0]:
        posh_silver.append(i[1]) 
#print(posh_silver)
#no other bags

bright_tomato = []
for i in data:
    if 'bright tomato' in i[0]:
        bright_tomato.append(i[1]) 
#print(bright_tomato)
#no other bags

mirrored_coral_total = 2*3 + 3*1 + 1*6 + 2*10 + 4*11 + 5*9 + 5*1
#print(mirrored_coral_total)

######1 faded olive, 1 posh bronze

faded_olive = []
for i in data:
    if 'faded olive' in i[0]:
        faded_olive.append(i[1]) 
#print(faded_olive)
#no other bags
#1 bag total

################################

posh_bronze = []
for i in data:
    if 'posh bronze' in i[0]:
        posh_bronze.append(i[1]) 
#print(posh_bronze)
#5 clear coral, 1 dotted lime, 5 faded olive, 3 dim red

#5 clear coral has 1 muted gold, 5 drab magenta, 5 bright tomato
#dim red has 2 light violet, 4 clear coral

#clear_coral = 1 muted gold, 5 drab magenta, 5 bright tomato

dotted_lime = []
for i in data:
    if 'dotted lime' in i[0]:
        dotted_lime.append(i[1]) 
#print(dotted_lime)
#4 drab magenta, 1 dark black, 2 posh purple

#drab magenta has 3 dark crimson, 1 muted gold, 3 posh silver, 2 dull aqua

dark_black = []
for i in data:
    if 'dark black' in i[0]:
        dark_black.append(i[1]) 
#print(dark_black)
#1 vibrant indigo, 5 muted gold bags, 4 bright tomato, 3 dull tan

vibrant_indigo = []
for i in data:
    if 'vibrant indigo' in i[0]:
        vibrant_indigo.append(i[1]) 
#print(vibrant_indigo)
#5 faded silver bags, 2 striped white, 5 shiny magenta

faded_silver = []
for i in data:
    if 'faded silver' in i[0]:
        faded_silver.append(i[1]) 
#print(faded_silver)
#1 striped white

striped_white = []
for i in data:
    if 'striped white' in i[0]:
        striped_white.append(i[1]) 
#print(striped_white)
#no other bags

shiny_magenta = []
for i in data:
    if 'shiny magenta' in i[0]:
        shiny_magenta.append(i[1]) 
#print(shiny_magenta)
#4 clear turquoise, 2 posh silver contains no bags

clear_turquoise = []
for i in data:
    if 'clear turquoise' in i[0]:
        clear_turquoise.append(i[1]) 
#print(clear_turquoise)
#no other bags

dull_tan = []
for i in data:
    if 'dull tan' in i[0]:
        dull_tan.append(i[1]) 
#print(dull_tan)
#1 posh purple

posh_purple = []
for i in data:
    if 'posh purple' in i[0]:
        posh_purple.append(i[1]) 
#print(posh_purple)
#2 bright tomato, 5 dark gray, 5 clear coral, 5 clear turquoise

##############
#posh_bronze has 5 clear coral, 1 dotted lime, 5 faded olive, 3 dim red
#################

#clear coral has 1 muted gold, 5 drab magenta, 5 bright tomato

#drab magenta has 3 dark crimson, 1 muted gold, 3 posh silver, 2 dull aqua

#dotted_lime has 4 drab magenta, 1 dark black, 2 posh purple

#dark black has 1 vibrant indigo, 5 muted gold bags, 4 bright tomato, 3 dull tan

#vibrant indigo has 5 faded silver bags, 2 striped white, 5 shiny magenta

#faded silver has 1 striped white (no other bags in striped white)

#shiny magenta has 4 clear turquoise, 2 posh silver contains no bags

#dull_tan has 1 posh purple

#posh_purple has 2 bright tomato, 5 dark gray, 5 clear coral, 5 clear turquoise

posh_bronze_total = 1*14 + 5*11 + 5*9 + 1*7 + 4*9 + 1*13 + 1*12 + 5*1

#We gave up cause we don't know recursion :(