import os
import sys, pygame

ball = pygame.image.load("claudius.png")
ball = pygame.transform.scale(ball, (228, 322))
ballrect = ball.get_rect()

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)


class Player:
    def __init__(xSpeed, ySpeed):
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
    def 


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    speed[1] += gravity
    
    rounerKey = pygame.key.get_pressed()

    if rounerKey[pygame.K_RIGHT]:   #Keymap
        speed[0] = 5
    if rounerKey[pygame.K_LEFT]:
        speed[0] = -5
    if rounerKey[pygame.K_UP] and ballrect.bottom == height:
        speed[1] = -10
    if rounerKey[pygame.K_DOWN]:
        speed[1] = 5

    ballrect = ballrect.move(speed)

    """if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    """
    if ballrect.right > width:
        ballrect.right = width
    if ballrect.left < 0:
        ballrect.left = 0
    if ballrect.bottom > height:
        ballrect.bottom = height
    if ballrect.top < 0:
        ballrect.top = 0
    #keep in window; fix when self == sidescroller

    ballrect.left = clip(ballrect.left, 0, width)
    ballrect.right = clip(ballrect.right, 0, width)        
    ballrect.top = clip(ballrect.top, 0, height)
    ballrect.bottom = clip(ballrect.bottom, 0, height) 

    if ballrect.bottom == height:
        speed[0] = 0

    screen.fill(black)
    screen.blit(backdrop, backRect)
    screen.blit(ball, ballrect)
    pygame.display.flip()