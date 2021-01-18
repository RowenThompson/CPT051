class Actor:
    def __init__(self, name, hp, x , y):
        self.name = name
        self.hp = hp + 10

    def get_hp(self):
        return self.hp

class Fighter(Actor):
    def __init__(self, name,  hp, x, y, attack):
        super().__init__(name,  hp, x, y)
        self.attack = attack


class Player(Fighter):
    def __init__(self, name,  hp, x, y, attack, quest_points):
        super().__init__(name,  hp, x, y, attack)
        self.quest_points = quest_points

    def get_name(self):
        print(self.name)

class Caster:
    def __init__(self, mana):
        self.mana = mana

    def spell(self):
        print("You cast a spell")


class Player_Caster(Player,Caster):
    def __init__(self, name,  hp, x, y, attack, quest_points, mana):
        super().__init__(name,  hp, x, y, attack, quest_points)
        self.mana = mana

def basic_attack(actor1, actor2):
    actor1.hp -= actor2.attack


class Tile():
    pass

class Magic_Tile(Tile, Caster):
    def __init__(self, mana):
        super().__init__(mana)



def my_function(my_actor):
    print(my_actor.hp)
    
    

x = Actor('Rabbit', 100, 0, 0)
print(x.hp)

b = Fighter('wolf', 200, 0,1,50)
print(b.attack)

basic_attack(x, b)
print(x.hp)


p = Player("Rowen", 300, 2, 2, 60, 0)

print("my_func")
my_function(p)

n = Player_Caster("Rowen", 300, 2, 2, 60, 0, 100)
print("P_C spell")
n.spell()

n.get_name()

print("tiles")
u = Magic_Tile(50)
u.spell()


#item: name, get_name
#Caster: use/cast
#Healing: amount_healed
#Equipment: Equip

