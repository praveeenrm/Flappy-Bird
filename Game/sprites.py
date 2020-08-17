import pygame
from settings import *


class Floor(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.img = pygame.image.load(floor_image)
		self.image = pygame.transform.scale(self.img, (WIDTH*2, 100))
		self.rect = self.image.get_rect()
		self.rect.bottom = HEIGHT
		self.rect.x = 0

	def update(self):
		self.rect.x -= 2
		if self.rect.x < -400:
			self.rect.x = 0

class Bird(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.images.append(pygame.image.load(bird_image_1))
		self.images.append(pygame.image.load(bird_image_1))
		self.images.append(pygame.image.load(bird_image_1))
		self.images.append(pygame.image.load(bird_image_2))
		self.images.append(pygame.image.load(bird_image_2))
		self.images.append(pygame.image.load(bird_image_2))
		self.images.append(pygame.image.load(bird_image_3))
		self.images.append(pygame.image.load(bird_image_3))
		self.images.append(pygame.image.load(bird_image_3))
		self.index = 0
		self.image = self.images[self.index]
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (100, HEIGHT/3)
		self.bird_movement = 0
		self.gravity = 0.5

	def update(self):
		self.index += 1
		if self.index >= len(self.images):
			self.index = 0
		self.image = self.images[self.index]
		self.bird_movement += self.gravity
		self.image = pygame.transform.rotozoom(self.image, self.bird_movement*2, 1)
		self.rect.bottom += self.bird_movement

		if self.rect.top < 0:
			self.rect.top = 0

	def jump(self):
		self.bird_movement = -7

class PipeTop(pygame.sprite.Sprite):
	def __init__(self, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(pipe_image).convert()
		self.image = pygame.transform.flip(self.image, False, True)
		self.image = pygame.transform.scale(self.image, (52, h))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.top = 0
		self.rect.left = WIDTH

	def update(self):
		self.rect.x -= 2
		if self.rect.right < -10:
			self.kill()

class PipeDown(pygame.sprite.Sprite):
	def __init__(self, h):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(pipe_image).convert()
		self.image = pygame.transform.scale(self.image, (52, h))
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.bottom = HEIGHT - 100
		self.rect.left = WIDTH

	def update(self):
		self.rect.x -= 2
		if self.rect.right < -10:
			self.kill()
		

