class Actor:
    def __init__(self, name, hp, x , y):
        self.name = name
        self.hp = hp
        
class Item():
    def __init__(name, get_name, number_of_items, use,):
        self.name = name
        
class MY_Object():
    def __init__(self, name, get_name, Object_brake):
        self.name = name
        pass

class Caster(Actor):
    def __init__(self, mana):
        super().__init__(mana)
        self.mana = mana

    def spell(self):
            print("You cast a spell")

t = MY_Object("name" , "get_name", "obj")

self = ("john, mama, lol")
