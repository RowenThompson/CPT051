hp = 100 #player hp, can be added to or subtracted from
dmg_queue = [12,21,31,21,31,32,41, 1] #que of dmg to be applied one at a time
print(dmg_queue)#shows all incoming damage

x = dmg_queue.pop()#removes last elementy from que assigns to x.
print(x) #print the last dmg element from the list
print(dmg_queue)#shows all incoming damage, except dmg already removed

hp = hp - x
print(hp)

#x += dmg_queue.pop() #amount of dmaage PLUS the next/last element in que

print(x) #printing last TWO units of damage summed
print(dmg_queue)#shows all incoming damage , except dmg already removed


hp = hp - dmg_queue.pop() #dmg
hp = hp + heal_queue.pop() #heal
print(hp)


hp -= dmg_queue.pop() #next unit of dmage (the 3rd element) HEALS instead

print(x) #prints total amount of dmage accumulated in variable x
print(dmg_queue)#shows all incoming damage , except dmg already removed

hp = hp - x
print(hp)

