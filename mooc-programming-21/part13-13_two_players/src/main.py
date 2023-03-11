# WRITE YOUR SOLUTION HERE:
import pygame
from pygame.constants import K_s, K_w

pygame.init()
window=pygame.display.set_mode((640,480))

robot1=pygame.image.load("robot.png")
x=320-robot1.get_width()
y=240-robot1.get_height()

robot2=pygame.image.load("robot.png")
m=0
n=0

to_right1=False
to_left1=False
to_up1=False
to_down1=False

to_right2=False
to_left2=False
to_up2=False
to_down2=False

clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                to_left1=True
            if event.key==pygame.K_RIGHT:
                to_right1=True
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                to_left1=False
            if event.key==pygame.K_RIGHT:
                to_right1=False
        
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    to_up1=True
                if event.key==pygame.K_DOWN:
                    to_down1=True

        if event.type==pygame.KEYUP:
                if event.key==pygame.K_UP:
                    to_up1=False
                if event.key==pygame.K_DOWN:
                    to_down1=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                to_left2=True
            if event.key==pygame.K_d:
                to_right2=True
        
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_a:
                to_left2=False
            if event.key==pygame.K_d:
                to_right2=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                to_up2=True
            if event.key==pygame.K_s:
                to_down2=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                to_up2=False
            if event.key==pygame.K_s:
                to_down2=False

        if event.type==pygame.QUIT:
            exit()
    
    if to_right1:
        if (x+2)<640-robot1.get_width():
            x+=2
    if to_left1:
        if (x-2)>0:
            x-=2

    if to_up1:
        if (y-2)>0:
            y-=2
    if to_down1:
        if (y+2)<480-robot1.get_height():
            y+=2
    
    if to_right2:
        if (m+2)<640-robot2.get_width():
            m+=2
    if to_left2:
        if (m-2)>0:
            m-=2

    if to_up2:
        if (n-2)>0:
            n-=2
    if to_down2:
        if (n+2)<480-robot2.get_height():
            n+=2


    
    

    window.fill((0,0,0))
    window.blit(robot1,(x,y))
    window.blit(robot2,(m,n))
    pygame.display.flip()

    clock.tick(60)