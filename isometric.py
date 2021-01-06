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
    
        if keys[pygame.K_LEFT]:
            player_x -= vel

        if keys[pygame.K_RIGHT]:
            player_x += vel

        if keys[pygame.K_UP]:
            player_y -= vel

        if keys[pygame.K_DOWN]:
            player_y += vel
            
        if keys[pygame.K_SPACE]:
            player_y = 5
            player_x = 5

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    #time.sleep(1)
