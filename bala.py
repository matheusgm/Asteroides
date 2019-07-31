import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np

class BALA:
    def __init__(self,x,y,ang):
        self.x = x
        self.y = y
        self.ang = ang
        self.tam = 38
        self.vel = 15
        self.bala = pygame.image.load('fire_blue.png')
        self.sub = self.bala.subsurface(0,0,30,52)



    def draw(self,screen):
    	#print("x: "+str(self.x)+" - y: "+str(self.y)+" - Ang: "+str(self.ang)+" - Ang Normalizado: "+str((self.ang*180)/np.pi))
    	screen.blit(pygame.transform.rotate(self.sub,(self.ang*180)/np.pi),(self.x+(5*np.sin(self.ang)),self.y-(0*np.cos(self.ang))))

    def update(self):
        self.y-=self.vel*np.cos(self.ang)
        self.x-=self.vel*np.sin(self.ang)