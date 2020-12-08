hp = 100
dmg_queue = [12,21,31,21,31,32,41,1]
x = dmg_queue.pop
while(hp > 0):
    hp = hp - dmg_queue.pop()
    print(hp)
    
print("You have died")
