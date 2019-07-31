import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np
from random import randint

class INIMIGO:
    def __init__(self):
        self.lado = randint(0,3)
        self.ang = randint(0,180)
        self.vel = randint(10,100)/10
        self.x=randint(0,WIDTH)
        self.y=randint(0,HEIGHT)

        self.pedra = pygame.image.load('rock.png')
        self.sub = self.pedra.subsurface(0,0,64,64)

        self.atualizar_pos()

    def atualizar_pos(self):
        if(self.lado == 0):
            self.x = WIDTH+100
        elif(self.lado==1):
            self.y = 0-100
        elif(self.lado==2):
            self.x = 0-100
        else:
            self.y = HEIGHT+100

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
