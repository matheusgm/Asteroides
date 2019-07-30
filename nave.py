import pygame

class NAVE:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.tam = 38
        self.vel = 15
        self.nave = pygame.image.load('spaceship.png')
        self.sub = self.nave.subsurface(40,0,40,30)
    def draw(self,screen):
        screen.blit(self.sub,(self.x,self.y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.y -= self.vel
            self.left = True
            self.right = False
        if keys[pygame.K_DOWN]:
            self.y += self.vel
            self.left = True
            self.right = False
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
            self.left = True
            self.right = False
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
            self.right = True
            self.left = False
        else:
            self.right = False
            self.left = False
