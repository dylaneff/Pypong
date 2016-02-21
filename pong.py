import pygame, sys
from pygame.locals import *

# Set the frames per second
FPS = 160

# The dimensions of the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

LINETHICKNESS = 10
PADDLELENGTH = 50
PADDLEOFFSET = 20

BLACK = (0, 0, 0)
WHITE = (255,255,255)

def main():
    pygame.init()

    global DISPLAYSURF  # The main display surface
    fpsclock = pygame.time.Clock()  # Creates a clock object used to track FPS

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('PyPong')

    # Initialize the starting positions
    ballX = (WINDOWWIDTH - LINETHICKNESS) / 2
    ballY = (WINDOWHEIGHT - LINETHICKNESS) / 2
    p1Pos = (WINDOWHEIGHT - PADDLELENGTH) / 2
    p2Pos = (WINDOWHEIGHT - PADDLELENGTH) / 2
    
    # Draw the rectangles
    paddle1 = pygame.Rect(PADDLEOFFSET, p1Pos, LINETHICKNESS, PADDLELENGTH)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, p2Pos, LINETHICKNESS, PADDLELENGTH)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)
    while True:     # main loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    fpsclock.tick(FPS)

if __name__ == '__main__':
    main()
