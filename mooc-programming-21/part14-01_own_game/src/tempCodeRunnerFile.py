# Complete your game here
 
import pygame
from datetime import datetime
from random import randint

class Robotosaur:
    def __init__(self):
        pygame.init()
 
        self.coins=0
        self.chances=0
        self.robot=pygame.image.load("robot.png")
        self.coin=pygame.image.load("coin.png")
        self.monster=pygame.image.load("monster.png")
        self.window=pygame.display.set_mode((640,480))
        self.x=0
        self.y=480-self.robot.get_height()
        self.my_time=datetime.now()
        self.s=self.my_time.second
 
        self.up=False
        self.down=False
        self.right=False
        self.left=False
       
        pygame.display.set_caption("Robotosaur: Use Arrow Keys, Collect Coins To Win but Monsters to lose ")
        self.game_font = pygame.font.SysFont("Arial", 24)
        self.new_place()
        self.main_loop()
       
 
    def new_place(self):
            self.a=randint(20,600)-self.coin.get_width()
            self.b=randint(20,400)-self.coin.get_height()
            self.c=randint(20,600)-self.monster.get_width()
            self.d=randint(20,400)-self.monster.get_height()
 
    def main_loop(self):
        clock=pygame.time.Clock()
        while True:
            self.check_events()
            
            clock.tick(60)
   
    def check_events(self):
        for event in pygame.event.get():
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.left=True
                if event.key==pygame.K_RIGHT:
                    self.right=True
                if event.key==pygame.K_UP:
                    self.up=True
                if event.key==pygame.K_DOWN:
                    self.down=True   
                if event.key == pygame.K_a:
                    self.new_game()
                if event.key == pygame.K_ESCAPE:
                    exit()
       
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False
                if event.key==pygame.K_UP:
                    self.up=False
                if event.key==pygame.K_DOWN:
                    self.down=False                           
            
       
            if event.type==pygame.QUIT:
               exit()
 
        self.window.fill((0,0,255))
        self.window.blit(self.coin,(self.a,self.b))
        self.window.blit(self.monster,(self.c,self.d))
        self.window.blit(self.robot,(self.x,self.y))
        e = self.game_font.render(f"Coins: {self.coins}/10", True, (255, 0, 0))
        self.window.blit(e, (0, 10))
        f = self.game_font.render(f"Chances: {self.chances}/3", True, (255, 0, 0))
        self.window.blit(f, (0, 30))
 
        if self.right:
            if (self.x+2)<640-self.robot.get_width():
                self.x+=4
        if self.left:
            if (self.x-2)>0:
                self.x-=4
 
        if self.up:
            if (self.y-2)>0:
                self.y-=4
        if self.down:
            if (self.y+2)<480-self.robot.get_height():
                self.y+=4
        if self.a<=self.x<=self.a+self.coin.get_width() or self.b<=self.y<=self.b+self.coin.get_height():
            self.coins+=1
            if self.coins<10:
                self.new_place()
            else:
                exit()
        if self.c<=self.x<=self.c+self.monster.get_width() and self.d<=self.y<=self.d+self.monster.get_height():
            self.coins-=1
            self.chances+=1
            self.new_place()
        if self.chances==3:
            exit()
        game_text = self.game_font.render("A = new game", True, (255, 0, 0))
        self.window.blit(game_text, (200, 10))

        game_text = self.game_font.render("Esc = exit game", True, (255, 0, 0))
        self.window.blit(game_text, (400, 10))
        pygame.display.flip()
 
    def new_game(self):
        Robotosaur()
 
if __name__=="__main__":
    Robotosaur()
 
