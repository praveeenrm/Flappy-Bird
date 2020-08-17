import pygame
import random
from settings import *
from sprites import *



class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
		# pygame.mixer.init()
		self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		pygame.display.set_icon(pygame.image.load(icon_image))
		self.clock = pygame.time.Clock()
		self.font_name = '04B_19.ttf'
		self.flap_sound = pygame.mixer.Sound(flap_music)
		self.death_sound = pygame.mixer.Sound(death_music)
		self.score_sound = pygame.mixer.Sound(score_music)
		self.bg_sound = pygame.mixer.Sound(bg_music)
		# self.dayOrNight = day_or_night
		self.running = True


	def new(self):
		self.score = 0
		self.n = 0
		self.bg_sound.play(loops=-1)

		self.all_sprites = pygame.sprite.Group()
		self.all_pipes = pygame.sprite.Group()

		self.bird = Bird()
		self.all_sprites.add(self.bird)
		self.bird_rect = self.bird.rect

		self.floor = Floor()
		self.all_sprites.add(self.floor)
		self.floor_rect = self.floor.rect

		self.pipe_top = PipeTop(X[0])
		self.all_sprites.add(self.pipe_top)
		self.all_pipes.add(self.pipe_top)

		self.pipe_down = PipeDown(Y[0])
		self.all_sprites.add(self.pipe_down)
		self.all_pipes.add(self.pipe_down)
		self.run()

	def run(self):
		self.playing = True
		self.ADDSCORE = pygame.USEREVENT
		pygame.time.set_timer(self.ADDSCORE, 2500)
		self.ADDPIPE = pygame.USEREVENT
		pygame.time.set_timer(self.ADDPIPE, 2500)
		while self.playing:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update()

	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
				self.running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					self.bird.jump()
					self.flap_sound.play()

			if event.type == self.ADDSCORE:
				self.score_sound.play()
				self.score += 1

			if event.type == self.ADDPIPE:
				n = random.randrange(0, len(X))
				self.new_pipe_top = PipeTop(X[n])
				self.new_pipe_down = PipeDown(Y[n])
				self.pipe_top_rect = self.new_pipe_top.rect
				self.pipe_down_rect = self.new_pipe_down.rect
				self.all_pipes.add(self.new_pipe_top)
				self.all_pipes.add(self.new_pipe_down)
				self.all_sprites.add(self.new_pipe_top)
				self.all_sprites.add(self.new_pipe_down)


			# Collision
			# if bird hits the floor
			if self.bird.rect.y >= HEIGHT-100 or self.bird_rect.colliderect(self.floor_rect):
				self.death_sound.play()
				self.playing = False

			# if bird hits the pipe
			self.hits = pygame.sprite.spritecollide(self.bird, self.all_pipes, False)
			if self.hits:
				self.death_sound.play()
				self.playing = False


	def draw(self):
		# if self.dayOrNight == "AM":
		# 	self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_day).convert(), (WIDTH, HEIGHT)), (0, 0))
		# else:
		# 	self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_night).convert(), (WIDTH, HEIGHT)), (0, 0))

		if (self.score%10) >= 5:
			self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_night).convert(), (WIDTH, HEIGHT)), (0, 0))
		elif(self.score%10) < 5:
			self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_day).convert(), (WIDTH, HEIGHT)), (0, 0))
		self.draw_text(f'Score: {self.score}', 22, WHITE, 320, 10)
		self.all_sprites.draw(self.screen)
		pygame.display.flip()

	def game_start_screen(self):
		self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_day).convert(), (WIDTH, HEIGHT)), (0, 0))
		img = pygame.image.load(message_image).convert_alpha()
		img = pygame.transform.scale(img, (250, 350))
		img_rect = img.get_rect(center=(200, 300))
		self.screen.blit(img, img_rect)
		self.draw_text('Press "p" to play', 30, WHITE, WIDTH/2, 50)
		self.draw_text('Press "SPACE" to Jump', 25, WHITE, WIDTH/2, HEIGHT-100)
		pygame.display.flip()
		self.wait_for_key()

	def game_over_screen(self):
		self.bg_sound.stop()
		self.screen.blit(pygame.transform.scale(pygame.image.load(bg_image_day).convert(), (WIDTH, HEIGHT)), (0, 0))
		img = pygame.image.load(game_over_image).convert_alpha()
		self.screen.blit(img, (100, HEIGHT/4))
		self.draw_text(f'Your Score: {self.score}', 25, WHITE, WIDTH/2, HEIGHT/3 + 50)
		self.draw_text('Press "p" to play again', 25, WHITE, WIDTH/2, HEIGHT/2)
		pygame.display.flip()
		self.wait_for_key()


	def wait_for_key(self):
		waiting = True
		while waiting:
			self.clock.tick(FPS)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					waiting = False
					self.running = False
				if event.type ==  pygame.KEYDOWN:
					if event.key == pygame.K_p:
						waiting = False


	def draw_text(self, text, size, color, x, y):
		font = pygame.font.Font(self.font_name, size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		self.screen.blit(text_surface, text_rect)

g = Game()
g.game_start_screen()
while g.running:
	g.new()
	g.game_over_screen()

pygame.quit()
