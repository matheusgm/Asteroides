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
        self.sub = self.nave.subsurface(39,0,39,40)
        self.sub = smoothscale(self.sub,(int(39*4), int(160)))
        self.rot = 0  
        self.rot_speed = 0 

        # define a surface (RECTANGLE)  
        self.image_orig = self.sub
        self.image = self.image_orig.copy()   
        # define rect for placing the rectangle at the desired position  
        self.rect = self.image.get_rect()  
        self.rect.center = (self.x , self.y) 

        self.pontos_verdes=[]

    def draw(self,screen):
        for el in self.balas:
            el.draw(screen)
        #pygame.draw.circle(screen, (0,255,0),(450,450),50,1)
        
        screen.blit(self.new_image , self.rect)
        for el in self.pontos_verdes:
            pygame.draw.circle(screen, (0,255,0),el,10)

    def update(self):
        for el in self.balas:
            el.update()
            if(el.x <= 0 or el.x >= WIDTH or el.y >=HEIGHT or el.y <=0):
                self.balas.remove(el)
        # making a copy of the old center of the rectangle  
        old_center = self.rect.center  
        # defining angle of the self.rotation  
        self.rot = (self.rot + self.rot_speed) % 360  
        # self.rotating the orignal image  
        self.new_image = pygame.transform.rotate(self.image_orig , self.rot)  
        self.rect = self.new_image.get_rect()  
        # set the rotated rectangle to the old center  
        self.rect.center = old_center  
        # drawing the rotated rectangle to the screen 
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            #self.rect[0] -= self.vel*np.sin(ang_rad)
            #self.rect[1] -= self.vel*np.cos(ang_rad)
            #print("X: {} Y: {} Rot: {} Rot_speed: {} Angulo: {}".format(self.rect[0],self.rect[1],self.rot,self.rot_speed,ang_rad))

            ang_rad = (np.pi*self.rot)/180

            self.x -= self.vel*np.sin(ang_rad)
            self.y -= self.vel*np.cos(ang_rad)

            self.rect.center = self.x, self.y
            self.pontos_verdes.append(self.rect.center)

            print("Rect: {} Center {} Ang: {} Sin: {:.2f} Cos: {:.2f}".format(self.rect,self.rect.center,self.rot,np.sin(ang_rad),np.cos(ang_rad)))
           
        if keys[pygame.K_LEFT]:
            self.rot_speed=5
        elif keys[pygame.K_RIGHT]:
            self.rot_speed=-5
        else:
            self.rot_speed = 0
        if keys[pygame.K_SPACE]:
            self.balas.append(BALA(self.rect[0],self.rect[1],ang_rad))
        
        