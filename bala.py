import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np

class BALA:
    def __init__(self,x_centro,y_centro,ang,img):
        self.x_centro = x_centro
        self.y_centro = y_centro
        self.ang = ang
        self.vel = 15
        self.saida_bala = 40

        self.img = pygame.transform.rotate(img,(self.ang*180)/np.pi)
        self.img_rect = self.img.get_rect()  
        self.img_rect.center = self.x_centro-(self.saida_bala*np.sin(self.ang)), self.y_centro-(self.saida_bala*np.cos(self.ang))

        self.info = self.info_quadrado()


    def draw(self,screen):
        screen.blit(self.img,self.img_rect)
        #pygame.draw.rect(screen, (0,255,0),self.quad_objeto())

    def update(self):
        self.x_centro -= self.vel*np.sin(self.ang)
        self.y_centro -= self.vel*np.cos(self.ang)
        self.img_rect.center = self.x_centro-(self.saida_bala*np.sin(self.ang)), self.y_centro-(self.saida_bala*np.cos(self.ang))

        self.info = self.info_quadrado()

    def info_quadrado(self):
        return {"x":self.img_rect[0],"y":self.img_rect[1],"w":self.img_rect[2],"h":self.img_rect[3]}
        
    def quad_objeto(self):
        return pygame.Rect(self.info["x"]+self.info["w"]*0.5/2, self.info["y"]+self.info["h"]*0.5/2, self.info["w"]*0.5, self.info["h"]*0.5)