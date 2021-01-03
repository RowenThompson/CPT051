import pygame
import time
import random
import sys

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0,0,255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
blockSize = 20
memo = {}

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#action zone
        grid_trav(10,10)

 #end of action zone           
        pygame.display.update()



def grid_trav(m,n):
    key = (str(m) + ',' + str(n))

    if(key in memo):
        return memo[key]
    if(m == 1 and n == 1):
        return 1
    if(m == 0 or n == 0):
        return 0

    time.sleep(0.5)
    draw_pix(m, n)
    pygame.event.pump()
    pygame.display.update()

    memo[key] = grid_trav(m - 1, n) + grid_trav(m, n - 1)

    
    
    return memo[key]


def draw_pix(x, y):
    rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
    pygame.draw.rect(SCREEN, RED, rect, 0)

def draw_person(x, y):
    rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
    pygame.draw.rect(SCREEN, BLUE, rect, 0)

def drawGrid():
     #Set the size of the grid block
    for x in range(WINDOW_WIDTH):
        for y in range(WINDOW_HEIGHT):
            rect = pygame.Rect(x*blockSize, y*blockSize,
                               blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

if __name__ == "__main__":
    main()
    

