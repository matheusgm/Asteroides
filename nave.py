import pygame
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np
from bala import *
import time

class NAVE:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vel = 5
        self.balas=[]

        self.nave = pygame.image.load('spaceship.png')

        #self.nave_parada = smoothscale(self.nave_parada,(int(39*4), int(160)))

        self.img = [self.nave.subsurface(39,0,39,40),self.nave.subsurface(38,38,43,45) ]

        self.rot = 0  
        self.rot_speed = 0 

        self.image_orig = self.img[0]
        self.image = self.image_orig.copy()   
        self.rect = self.image.get_rect()  
        self.rect.center = (self.x , self.y) 

        self.pontos_verdes=[]

        self.start_time = time.time()
        self.delta_tiro = 1/TIROS_POR_SEGUNDO

    def draw(self,screen):
        
        #pygame.draw.circle(screen, (0,255,0),(450,450),50,1)
        
        screen.blit(self.new_image , self.rect)
        #for el in self.pontos_verdes:
            #pygame.draw.circle(screen, (0,255,0),el,10)

        for el in self.balas:
            el.draw(screen)

    def update(self):
        for el in self.balas:
            el.update()
            if(el.x <= 0 or el.x >= WIDTH or el.y >=HEIGHT or el.y <=0):
                self.balas.remove(el)
        
        old_center = self.rect.center  
        self.rot = (self.rot + self.rot_speed) % 360  
        self.new_image = pygame.transform.rotate(self.image_orig , self.rot)  
        self.rect = self.new_image.get_rect()    
        self.rect.center = old_center  
        
        ang_rad = (np.pi*self.rot)/180

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.image_orig = self.img[1]
            self.x -= self.vel*np.sin(ang_rad)
            self.y -= self.vel*np.cos(ang_rad)

            self.rect.center = self.x, self.y
            self.pontos_verdes.append(self.rect.center)

            #print("Rect: {} Center {} Ang: {} Sin: {:.2f} Cos: {:.2f}".format(self.rect,self.rect.center,self.rot,np.sin(ang_rad),np.cos(ang_rad)))
        else:
            self.image_orig = self.img[0] 
        if keys[pygame.K_LEFT]:
            self.rot_speed=5
        elif keys[pygame.K_RIGHT]:
            self.rot_speed=-5
        else:
            self.rot_speed = 0

        self.colisao_nave_com_tela()
        
        if self.delta_tiro >= 1/TIROS_POR_SEGUNDO:
            if keys[pygame.K_SPACE]:
                self.delta_tiro = 0
                self.start_time = time.time()
                self.balas.append(BALA(self.rect.center[0],self.rect.center[1],ang_rad))
        else:
            end_time = time.time()
            self.delta_tiro = round(end_time - self.start_time,1)
        #print(self.delta_tiro,end=" - ")
        #print(1/TIROS_POR_SEGUNDO)
    def colisao_nave_com_tela(self):
        #print(self.rect)
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        elif self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0
        