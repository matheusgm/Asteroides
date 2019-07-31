import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np

class BALA:
    def __init__(self,x,y,ang):
        self.x = x
        self.y = y
        self.ang = ang
        self.vel = 15
        self.saida_bala = 40

        self.bala = pygame.image.load('fire_blue.png')
        self.sub = self.bala.subsurface(0,0,30,52)

        self.img = pygame.transform.rotate(self.sub,(self.ang*180)/np.pi)
        self.img_rect = self.img.get_rect()  
        self.img_rect.center = self.x-(self.saida_bala*np.sin(self.ang)), self.y-(self.saida_bala*np.cos(self.ang))


    def draw(self,screen):
    	screen.blit(self.img,self.img_rect)

    def update(self):
        self.x -= self.vel*np.sin(self.ang)
        self.y -= self.vel*np.cos(self.ang)
        self.img_rect.center = self.x-(self.saida_bala*np.sin(self.ang)), self.y-(self.saida_bala*np.cos(self.ang))
