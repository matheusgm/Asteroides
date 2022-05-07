import pygame
import os
from pygame.transform import flip,scale,rotate,smoothscale
from settings import *
from nave import *
from inimigo import *
import time
import threading


class Game:
	def __init__(self):
		# Initialize Game Window
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.bg = pygame.image.load(os.path.join('imagens','background.jpg'))
		self.bg = smoothscale(self.bg,(int(WIDTH),int(HEIGHT)))

		balas = pygame.image.load(os.path.join('imagens','fire_blue.png'))
		img_bala = balas.subsurface(0,0,32,52)

		spaceship_img = pygame.image.load(os.path.join('imagens','spaceship.png'))

		self.sps = NAVE(400,400,img_bala,spaceship_img)

		self.inimigo = []
		self.start_time = time.time()
		self.temp_antigo = -1

		self.rocks = [spaceship_img.subsurface(0,151,57,57), spaceship_img.subsurface(62,169,32,33),spaceship_img.subsurface(102,177,14,13) ,
            spaceship_img.subsurface(0,212,52,44),spaceship_img.subsurface(79,220,19,29) ,spaceship_img.subsurface(90,222,23,24)]

		self.game_music = pygame.mixer.Sound('audio/game_music.wav')
		self.jair_music = pygame.mixer.Sound('audio/rock_appear.wav')
		self.jair_music.set_volume(0.1)
		self.jair_morre = pygame.mixer.Sound('audio/big_rock_explosion.wav')
		self.jair_morre.set_volume(0.1)

	def new(self):
		# Start a new game
		self.run()

	def run(self):
		# Game loop
		self.playing = True
		self.game_music.play(-1)
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

		if(temp_novo != self.temp_antigo):
			#print(temp_novo)
			self.temp_antigo = temp_novo
			if(temp_novo % 1 == 0):
				ind_img = randint(0,len(self.rocks)-1)
				self.inimigo.append(INIMIGO(randint(0,WIDTH),randint(0,HEIGHT),randint(0,3), randint(0,180),randint(10,100)/10,self.rocks[ind_img]))
				if(ind_img == 0): # Se for o Jair, toca a musica
					self.jair_music.play()

		#print(len(self.inimigo))

		for el in self.inimigo:
			el.update()
			if(el.x <= 0-200 or el.x >= WIDTH+200 or el.y >=HEIGHT+200 or el.y <=0-200):
				self.inimigo.remove(el)
			else:
				for bala in self.sps.balas:
					if(self.collision(el.quad_objeto(),bala.quad_objeto())):
						if(el.img == self.rocks[0]): # Se for o Jair, aparece os 3 filhos
							self.jair_morre.play()
							self.inimigo.append(INIMIGO(el.x,el.y,5,randint(0,359),randint(20,40)/10,self.rocks[1]))
							self.inimigo.append(INIMIGO(el.x,el.y,5,randint(0,359),randint(20,40)/10,self.rocks[2]))
							self.inimigo.append(INIMIGO(el.x,el.y,5,randint(0,359),randint(20,40)/10,self.rocks[3]))
						self.sps.balas.remove(bala)
						self.inimigo.remove(el)

		self.sps.update()

	def draw(self):
		# Game loop - Draw
		self.screen.blit(self.bg,(0,0))
		self.sps.draw(self.screen)

		#self.grid()

		for el in self.inimigo:
			el.draw(self.screen)

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

	def grid(self):
		for i in range(20):
			pygame.draw.line(self.screen,(255,0,0),(i*50,0),(i*50,HEIGHT),1)
		for i in range(20):
			pygame.draw.line(self.screen,(255,0,0),(0,i*50),(WIDTH,i*50),1)

	def detectCollisions(self,x1,y1,w1,h1,x2,y2,w2,h2):
		return x1 < x2+w2 and x2 < x1+w1 and y1 < y2+h2 and y2 < y1+h1

	def collision(self, player, objeto):
		return self.detectCollisions(player[0], player[1], player[2], player[3], objeto[0], objeto[1], objeto[2], objeto[3])

g = Game()
g.show_start_screen()
while g.running:
	g.new()
	g.show_go_screen()

pygame.quit()
