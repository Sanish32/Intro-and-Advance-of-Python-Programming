# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))
width=robot.get_width()
height=robot.get_height()
window.blit(robot, (40,150-height/2))
window.blit(robot, (90,150-height/2))
window.blit(robot, (140,150-height/2))
window.blit(robot, (190,150-height/2))
window.blit(robot, (240,150-height/2))
window.blit(robot, (290,150-height/2))
window.blit(robot, (340,150-height/2))
window.blit(robot, (390,150-height/2))
window.blit(robot, (440,150-height/2))
window.blit(robot, (490,150-height/2))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
