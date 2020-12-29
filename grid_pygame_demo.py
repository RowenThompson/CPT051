import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0,0,255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
blockSize = 20

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

        for x in range(WINDOW_WIDTH):
            draw_pix(x, x)
        pygame.display.update()

    

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
    
    SCREEN.fill(RED)
