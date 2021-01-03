import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
display = pygame.Surface((300, 300))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5


grass_img = pygame.image.load('grass.png').convert()
grass_img.set_colorkey((0, 0, 0))


run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN]:
        y += vel
    
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    #win.blit(grass_img, x, y)
    pygame.display.update() 
    
pygame.quit()
