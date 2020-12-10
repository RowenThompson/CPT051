hp = 100
#dmg_queue = [12,21,31,21,31,32,41,1]
dmg_queue = [99,12,21,12,5,4,3,2,1,4]

x = dmg_queue.pop
print(x)
print(dmg_queue)
while(hp > 0):
    hp = hp - dmg_queue.pop()
    print(hp)
    
print("You have died")
