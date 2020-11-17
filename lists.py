supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

print(cat)

dog = ['fat', 'gray', 'loud']
size, color, disposition = dog

print(dog)




import random
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))
