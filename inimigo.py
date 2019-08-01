import pygame
from pygame import mixer
from settings import *
from pygame.transform import flip,scale,rotate,smoothscale
import numpy as np
from random import randint

class INIMIGO:
    def __init__(self,pos=None,filho = None):
        if(pos==None):
            self.randomico()
        else:
            self.lado = 5
            self.ang = randint(0,359)
            self.vel = randint(20,40)/10
            self.x = pos[0]
            self.y = pos[1]

        #self.pedra = pygame.image.load('rock.png')
        #self.sub = self.pedra.subsurface(0,0,64,64)

        self.sheet = pygame.image.load('spaceship.png')
        self.jair = pygame.image.load('minibolso.png')
        self.carlos = pygame.image.load('minicarlos.png')
        self.dudu = pygame.image.load('minidudu.png')
        self.flavio = pygame.image.load('miniflavio.png')

        self.cla = [self.jair,self.carlos,self.dudu,self.flavio]
        #self.rocks = [self.sheet.subsurface(0,151,57,57), self.sheet.subsurface(62,169,32,33),self.sheet.subsurface(102,177,14,13) ,
            #self.sheet.subsurface(0,212,52,44),self.sheet.subsurface(79,220,19,29) ,self.sheet.subsurface(90,222,23,24)]

        self.img = self.cla[randint(0,len(self.cla)-1)]
        if(filho != None):
            self.img = self.cla[filho]

        if self.img == self.cla[0]:
            mixer.init()
            mixer.music.load('bolso1.wav')
            mixer.music.play()


        self.atualizar_pos()

    def randomico(self):
        self.lado = randint(0,3)
        self.ang = randint(0,180)
        self.vel = randint(10,100)/10
        self.x=randint(0,WIDTH)
        self.y=randint(0,HEIGHT)

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

    