# WRITE YOUR SOLUTION HERE:
import pygame
from pygame.constants import WINDOWHIDDEN

pygame.init()

window=pygame.display.set_mode((640,480))

robot1=pygame.image.load("robot.png")
robot2=pygame.image.load("robot.png")


x=0
y=120
a=640-robot2.get_width()
b=240

velocity1=1
velocity2=2
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(robot1,(x,y))
    window.blit(robot2,(a,b))
    pygame.display.flip()

    x += velocity1
    if velocity1 > 0 and x+robot1.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x <= 0:
        velocity1 = -velocity1

    a += velocity2
    if velocity2 > 0 and a+robot2.get_width() >= 640:
        velocity2 = -velocity2
    if velocity2 < 0 and a <= 0:
        velocity2 = -velocity2


    clock.tick(100)

    

    