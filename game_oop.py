class Actor:
    def __init__(self, name, hp, x , y):
        self.name = name
        self.hp = hp

    def get_hp(self):
        return self.hp

class Fighter(Actor):
    def __init__(self, name,  hp, x, y, attack):
        super().__init__(name,  hp, x, y)
        self.attack = attack

def basic_attack(actor1, actor2):
    actor1.hp -= actor2.attack

class Player(Fighter):
    def __init__(self, name,  hp, x, y, attack, quest_points):
        super().__init__(name,  hp, x, y, attack)
        self.quest_points = quest_points
        






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
