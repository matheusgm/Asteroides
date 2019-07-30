import pygame
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np

class NAVE:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tam = 38
        self.vel = 5
        self.nave = pygame.image.load('spaceship.png')
        self.sub = self.nave.subsurface(40,0,40,30)
        self.ang = 0
        self.ad_ang = 0.1
    def draw(self,screen):
        screen.blit(pygame.transform.rotate(self.sub,180*self.ang/np.pi),(self.x+40,self.y+30))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel*np.cos(self.ang)
            self.x -= self.vel*np.sin(self.ang)
        if keys[pygame.K_DOWN]:
            self.y += self.vel*np.cos(self.ang)
            self.x += self.vel*np.sin(self.ang)
        if keys[pygame.K_LEFT]:
            self.ang += self.ad_ang
        if keys[pygame.K_RIGHT]:
            self.ang -= self.ad_ang