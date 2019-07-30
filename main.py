import pygame
import os
from pygame.transform import flip,scale,rotate,smoothscale
from settings import *
from nave import *
from pygame.transform import flip,scale,rotate,smoothscale

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
		self.sps = NAVE(100,100)

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
		self.sps.update()

	def draw(self):
		# Game loop - Draw
		self.screen.blit(self.bg,(0,0))
		self.sps.draw(self.screen)
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
