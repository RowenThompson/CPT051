import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((300, 300))

grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))

player_x = 5
player_y = 5
vel = 1

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
    my_actor.hp += 50
    print(my_actor.hp)

x = Actor('Rabbit', 100, 0, 0)
print(x.hp)

b = Fighter('wolf', 200, 0, 1, 50)
print(b.attack)

basic_attack(x, b)
print(x.hp)

p = Player("Rowen", 300, 2, 2, 60, 0)

print("my_func")

print(p)

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0,0,0))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
                if (x == player_x) and (y == player_y):
                    display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_a]:
            player_x -= vel

        if keys[pygame.K_d]:
            player_x += vel

        if keys[pygame.K_w]:
            player_y -= vel

        if keys[pygame.K_s]:
            player_y += vel
            
        if keys[pygame.K_f]:
            player_y = 5
            player_x = 5
            
        if keys[pygame.K_KP1]:
            my_function
            print(my_actor.hp)

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    #time.sleep(1)

print(my_actor.hp)
