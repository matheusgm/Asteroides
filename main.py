import pygame
import os
from pygame.transform import flip,scale,rotate,smoothscale
from settings import *
from nave import *
from inimigo import *
from random import randint
import time

class Game:
	def __init__(self):
		# Initialize Game Window
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.bg = pygame.image.load('background.jpg')
		self.bg = smoothscale(self.bg,(int(WIDTH),int(HEIGHT)))
		self.sps = NAVE(400,400)
		self.inimigo = [] 
		self.start_time = time.time()
		self.temp_antigo = -1

	def new(self):
		# Start a new game
		self.run()

	def run(self):
		# Game loop
		self.playing = True
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		# Game loop - Update

		end_time = time.time()
		temp_novo = int(end_time) - int(self.start_time)
		#print(temp_novo)
		'''
		if(temp_novo != self.temp_antigo):
			#print(temp_novo)
			self.temp_antigo = temp_novo
			if(temp_novo % 1 == 0):
				lado = randint(0,3)
				posx = randint(0,WIDTH)
				posy = randint(0,HEIGHT)
				if(lado == 0):
					posx = WIDTH+100
				elif(lado==1):
					posy = 0-100
				elif(lado==2):
					posx = 0-100
				else:
					posy = HEIGHT+100
				ang = randint(0,180)
				vel = randint(10,100)/10
				self.inimigo.append(INIMIGO(posx,posy,lado,ang,vel))
		#print(len(self.inimigo))
		
		for el in self.inimigo:
			el.update()
			if(el.x <= 0-200 or el.x >= WIDTH+200 or el.y >=HEIGHT+200 or el.y <=0-200):
				self.inimigo.remove(el)
		'''
		self.sps.update()

	def draw(self):
		# Game loop - Draw
		self.screen.blit(self.bg,(0,0))
		self.sps.draw(self.screen)
		for i in range(20):
			pygame.draw.line(self.screen,(255,0,0),(i*50,0),(i*50,HEIGHT),1)
		for i in range(20):
			pygame.draw.line(self.screen,(255,0,0),(0,i*50),(WIDTH,i*50),1)
		
		'''
		for el in self.inimigo:
			el.draw(self.screen)
		'''
		# after drawing everything, flip the display
		pygame.display.flip()

	def events(self):
		# Game loop - Events
		for event in pygame.event.get():
			# check for closing window
			if event.type == pygame.QUIT:
				if self.playing:
					self.playing = False
				self.running = False

	def show_start_screen(self):
		# Game splash/start screen
		pass

	def show_go_screen(self):
		# Game Over/continue
		pass

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pygame.quit()
