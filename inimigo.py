import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np

class INIMIGO:
    def __init__(self,x,y,lado,ang,vel):
        self.lado = lado
        self.ang = ang
        self.tam = 38
        self.vel = vel
        self.x=x
        self.y=y
        self.pedra = pygame.image.load('rock.png')
        self.sub = self.pedra.subsurface(0,0,64,64)



    def draw(self,screen):
    	screen.blit(self.sub,(self.x,self.y))

    def update(self):
        if(self.lado == 0): # DIREITO
            if(self.ang > np.pi/2):
                self.y+=self.vel*np.sin(self.ang)
            else:
                self.y-=self.vel*np.sin(self.ang)
            self.x-=self.vel
        elif (self.lado == 1): # TOPO
            if(self.ang > np.pi/2):
                self.x-=self.vel*np.sin(self.ang)
            else:
                self.x+=self.vel*np.sin(self.ang)
            self.y+=self.vel
        elif (self.lado == 2): # ESQUERDO
            if(self.ang > np.pi/2):
                self.y+=self.vel*np.sin(self.ang)
            else:
                self.y-=self.vel*np.sin(self.ang)
            self.x+=self.vel
        elif (self.lado == 3): # BAIXO
            if(self.ang > np.pi/2):
                self.x-=self.vel*np.sin(self.ang)
            else:
                self.x+=self.vel*np.sin(self.ang)
            self.y-=self.vel
