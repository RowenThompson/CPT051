hp = 100
dmg_queue = [12,21,31,21,31,32,41,1]

if (hp > 0):
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    hp = hp - dmg_queue.pop()
    
print(hp)

if (hp < 0):
    print("You are dead")
