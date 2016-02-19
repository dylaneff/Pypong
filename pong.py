import pygame, sys
from pygame.locals import *

# Set the frames per second
FPS = 160

# The dimensions of the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

def main():
    pygame.init()

    global DISPLAYSURF  # The main display surface
    fpsclock = pygame.time.Clock()  # Creates a clock object used to track FPS

    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    pygame.display.set_caption('PyPong')

    while True:     # main loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    fpsclock.tick(FPS)

if __name__ == '__main__':
    main()
