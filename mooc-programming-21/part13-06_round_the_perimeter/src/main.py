# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window=pygame.display.set_mode((640,480))

robot=pygame.image.load("robot.png")

x=0
y=0
velocity=1

clock=pygame.time.Clock()
key=1
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    window.fill((0,0,0))
    window.blit(robot,(x,y))
    pygame.display.flip()

    if key==1:
        x+=velocity
    else:
        y+=velocity

    if velocity>0 and y+robot.get_height()<=480 and x+robot.get_width()>=640:
        key=2
    elif velocity>0 and y+robot.get_height()>=480 and x+robot.get_width()>=640:
        key=1
        velocity=-velocity
    elif velocity<0 and x<=0 and y>=0:
        key=2
    elif velocity<0 and y<=0 and x<=0:
        key=1
        velocity=-velocity
    
    

    clock.tick(100)