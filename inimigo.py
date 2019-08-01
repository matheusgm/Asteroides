import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np
from random import randint

class INIMIGO:
    def __init__(self,x,y,lado,ang,vel,img):

        self.lado = lado
        self.ang = ang
        self.vel = vel
        self.x = x
        self.y = y
        self.img = img

        self.atualizar_pos()


    def atualizar_pos(self):
        if(self.lado == 0):
            self.x = WIDTH+100
        elif(self.lado==1):
            self.y = 0-100
        elif(self.lado==2):
            self.x = 0-100
        elif(self.lado==3):
            self.y = HEIGHT+100

    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        #pygame.draw.rect(screen, (255,0,0),self.quad_objeto())
        

    def update(self):
        if(self.lado == 0): # DIREITO
            self.y+=self.vel*np.sin(self.ang)
            self.x-=self.vel
        elif (self.lado == 1): # TOPO
            self.x-=self.vel*np.sin(self.ang)
            self.y+=self.vel
        elif (self.lado == 2): # ESQUERDO
            self.y+=self.vel*np.sin(self.ang)
            self.x+=self.vel
        elif (self.lado == 3): # BAIXO
            self.x-=self.vel*np.sin(self.ang)
            self.y-=self.vel
        elif (self.lado == 5):
            self.x+=self.vel*np.sin(self.ang)
            self.y+=self.vel*np.cos(self.ang)


    def quad_objeto(self):
        return pygame.Rect(self.x+self.img.get_width()*0.25/2, self.y+self.img.get_height()*0.25/2, self.img.get_width()*0.75, self.img.get_height()*0.75)

    