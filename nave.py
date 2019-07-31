import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np
from bala import *

class NAVE:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 5
        self.balas=[]
        self.nave = pygame.image.load('spaceship.png')
        self.sub = self.nave.subsurface(40,0,40,30)
        self.ang = 0
        self.ad_ang = 0.1
        self.a = 0
        self.rot = 0  
        self.rot_speed = 0 
        # define a surface (RECTANGLE)  
        self.image_orig = self.nave.subsurface(40,0,40,30)
        # for making transparent background while rotating an image  
        #self.image_orig.set_colorkey(BLACK)  
        # fill the rectangle / surface with green color  
        self.image = self.image_orig.copy()  
        #self.image.set_colorkey(BLACK)  
        # define rect for placing the rectangle at the desired position  
        self.rect = self.image.get_rect()  
        self.rect.center = (WIDTH // 2 , HEIGHT // 2) 


    def draw(self,screen):
        for el in self.balas:
            el.draw(screen)

        # making a copy of the old center of the rectangle  
        old_center = self.rect.center  
        # defining angle of the self.rotation  
        self.rot = (self.rot + self.rot_speed) % 360  
        #print(self.rot)
        # self.rotating the orignal image  
        new_image = pygame.transform.rotate(self.image_orig , self.rot)  
        self.rect = new_image.get_rect()  
        # set the rotated rectangle to the old center  
        self.rect.center = old_center  
        # drawing the rotated rectangle to the screen  
        #print(self.rect)
        screen.blit(new_image , self.rect)#(self.x,self.y,self.rect[2],self.rect[3]))  #
        # flipping the display after drawing everything  
        
        

    def update(self):
        for el in self.balas:
            el.update()
            if(el.x <= 0 or el.x >= WIDTH or el.y >=HEIGHT or el.y <=0):
                self.balas.remove(el)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect[1] -= self.vel*np.cos((np.pi*self.rot)/180)
            self.rect[0] -= self.vel*np.sin((np.pi*self.rot)/180)
        if keys[pygame.K_LEFT]:
            self.rot_speed=5
        elif keys[pygame.K_RIGHT]:
            self.rot_speed=-5
        else:
            self.rot_speed = 0
        if keys[pygame.K_SPACE]:
            self.balas.append(BALA(self.rect[0],self.rect[1],(np.pi*self.rot)/180))