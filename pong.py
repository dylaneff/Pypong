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
WHITE = (255, 255, 255)


# Draws the game arena
def drawArena():
    DISPLAYSURF.fill(BLACK)
    # Outline of arena
    pygame.draw.rect(DISPLAYSURF, WHITE, ((0, 0), (WINDOWWIDTH, WINDOWHEIGHT)), LINETHICKNESS*2)
    # Center line
    pygame.draw.line(DISPLAYSURF, WHITE, ((WINDOWWIDTH/2), 0), ((WINDOWWIDTH/2), WINDOWHEIGHT), (LINETHICKNESS/4))


# Draws a paddle
def drawPaddle(paddle):

    # Prevent the paddle from moving below the playing area
    if paddle.bottom > WINDOWHEIGHT - LINETHICKNESS:
        paddle.bottom = WINDOWHEIGHT - LINETHICKNESS
    # Prevent the paddle from moving above the playing area
    if paddle.top < LINETHICKNESS:
        paddle.top = LINETHICKNESS

    # Draw the paddle
    pygame.draw.rect(DISPLAYSURF, WHITE, paddle)


# Draw the ball
def drawBall(ball):
    pygame.draw.rect(DISPLAYSURF, WHITE, ball)


def moveBall(ball, x, y):
    ball.x += x
    ball.y += y
    return ball


# Handle the collision of the ball and an edge
def checkEdgeCollision(ball, x, y):
    if ball.left == LINETHICKNESS or ball.right == (WINDOWWIDTH - LINETHICKNESS):
        x *= -1
    if ball.top == LINETHICKNESS or ball.bottom == (WINDOWHEIGHT - LINETHICKNESS):
        y *= -1
    return x, y


# Handle the collision of the ball and paddle
def checkPaddleCollision(paddle1, paddle2, ball, direction):
    if (direction < 0 and ball.left == paddle1.right and
       ball.bottom > paddle1.top and ball.top < paddle1.bottom) \
       or (direction > 0 and ball.right == paddle2.left and
       ball.bottom > paddle2.top and ball.top < paddle2.bottom):
        direction *= -1
    return direction


# Makes the enemy move
def enemyMove(paddle, ball, x):
    if x == -1:
        if paddle.centery > (WINDOWHEIGHT / 2):
            paddle.centery -= 1
        elif paddle.centery < (WINDOWHEIGHT / 2):
            paddle.centery += 1
    else:
        if ball.centery > paddle.centery:
            paddle.centery += 1
        elif ball.centery < paddle.centery:
            paddle.centery -= 1
    return paddle


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

    # Direction the ball is moving
    ballDirX = -1  # -1 = left; +1 = right
    ballDirY = -1  # -1 = up; +1 = down
    # Create the rectangles
    paddle1 = pygame.Rect(PADDLEOFFSET, p1Pos, LINETHICKNESS, PADDLELENGTH)
    paddle2 = pygame.Rect(WINDOWWIDTH - PADDLEOFFSET - LINETHICKNESS, p2Pos, LINETHICKNESS, PADDLELENGTH)
    ball = pygame.Rect(ballX, ballY, LINETHICKNESS, LINETHICKNESS)

    # Draw the game objects
    drawArena()
    drawPaddle(paddle1)
    drawPaddle(paddle2)
    drawBall(ball)

    pygame.mouse.set_visible(0)

    while True:     # main loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # Mouse movement
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                paddle1.y = mousey

        drawArena()
        drawPaddle(paddle1)
        drawPaddle(paddle2)
        drawBall(ball)
        ball = moveBall(ball, ballDirX, ballDirY)
        ballDirX, ballDirY = checkEdgeCollision(ball, ballDirX, ballDirY)
        ballDirX = checkPaddleCollision(paddle1, paddle2, ball, ballDirX)
        paddle2 = enemyMove(paddle2, ball, ballDirX)

        pygame.display.update()
        fpsclock.tick(FPS)


if __name__ == '__main__':
    main()
