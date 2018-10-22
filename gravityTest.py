import pygame
import os
import sys

pygame.font.init()
#pygame.init()

size = width, height = 1279, 742
speed = [0, 0]
speedCoeff = 5
black = 0, 0, 0
gravity = 0.2

screen = pygame.display.set_mode(size)

backdrop = pygame.image.load("background.jpg")
backdrop = pygame.transform.scale(backdrop, (width, height))
backRect = backdrop.get_rect()

ball = pygame.image.load("claudius.png")
ball = pygame.transform.scale(ball, (228, 322))
ballrect = ball.get_rect()

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    speed[1] += gravity
    
    rounerKey = pygame.key.get_pressed()

    if rounerKey[pygame.K_RIGHT]:   #Keymap
        speed[0] = speedCoeff
    if rounerKey[pygame.K_LEFT]:
        speed[0] = -speedCoeff
    if rounerKey[pygame.K_UP] and ballrect.bottom == height:
        speed[1] = -speedCoeff * 2
    if rounerKey[pygame.K_DOWN]:
        speed[1] = speedCoeff

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