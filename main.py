import pygame
from settings import *

class Game:
	def __init__(self):
		# Initialize Game Window
		pygame.init()
		pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True

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
		pass

	def draw(self):
		# Game loop - Draw
		self.screen.fill(BLACK)

		
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