import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1000, 1000),0,32)
display = pygame.Surface((300, 300))

base_screen_size = [1000,1000]



grass_img = pygame.image.load('cobble2.png').convert()
grass_img.set_colorkey((0, 0, 0))

goal_img = pygame.image.load('goal.png').convert()
goal_img.set_colorkey((0, 0, 0))

mx = 5
my = 5

game_scroll = [0, 0]

player_x = 5
player_y = 5
vel = 1


def complex_camera(camera, target_rect):
    # we want to center target_rect
    x = -player_x + WIN_WIDTH/2 
    y = -player_y + WIN_HEIGHT/2
    # move the camera. Let's use some vectors so we can easily substract/multiply
    camera.topleft += (pygame.Vector2((x, y)) - pygame.Vector2(camera.topleft)) * 0.06 # add some smoothness coolnes
    # set max/min x/y so we don't see stuff outside the world
    camera.x = max(-(camera.width-WIN_WIDTH), min(0, camera.x))
    camera.y = max(-(camera.height-WIN_HEIGHT), min(0, camera.y))
    
    return camera





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
                    display.blit(goal_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))
                

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        mx, my = pygame.mouse.get_pos()
        true_mx = mx
        true_my = my
        mx -= (screen.get_width() - base_screen_size[0]) // 2
        my -= (screen.get_height() - base_screen_size[1]) // 2
        mx /= base_screen_size[0] / display.get_width()
        my /= base_screen_size[1] / display.get_height()


        game_mx = ((mx + game_scroll[0]) + (my + game_scroll[1])) / 18 * 100
        game_my = ((-mx - game_scroll[0]) + (my + game_scroll[1])) / 18 * 100

        if (x == game_mx) and (y == game_my):
            display.blit(grass_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5 - 14))

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

    #camera = Camera(complex_camera, total_level_width, total_level_height)
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    #screen.blit(pygame.transform.scale(display, screen.get_size()), (player_x, player_y))
    pygame.display.update()
    #time.sleep(1)
