import pygame
import os
import sys

pygame.font.init()
#pygame.init()

size = width, height = 1280, 720
speed = [0, 0]
black = 0, 0, 0

thrust = 5
lift = 10
gravity = 0.5
friction = 0.5

backdrop = pygame.image.load("background.jpg")
backdrop = pygame.transform.smoothscale(backdrop, (width, height))
backRect = backdrop.get_rect()

ball = pygame.image.load("claudius.png")
ball = pygame.transform.scale(ball, (171, 242))
ballrect = ball.get_rect()

def clip(val, minval, maxval):
    return min(max(val, minval), maxval)

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

    speed[1] += gravity
    
    rounerKey = pygame.key.get_pressed()

    if rounerKey[pygame.K_RIGHT]:   #Keymap
        speed[0] = thrust
    if rounerKey[pygame.K_LEFT]:
        speed[0] = -thrust
    if rounerKey[pygame.K_UP] and ballrect.bottom == height:
        speed[1] = -lift * 2
    if rounerKey[pygame.K_DOWN]:
        speed[1] = lift
        
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

    if ballrect.bottom == height and speed[0] != 0: #friction mechanic
        if speed[0] >= 0:
            speed[0] -= friction
        elif speed[0] <= 0:
            speed[0] += friction
    
    screen.fill(black)
    screen.blit(backdrop, backRect)
    screen.blit(ball, ballrect)
    pygame.display.flip()