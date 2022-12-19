import pygame

class PlayButton():
	def __init__(self, ll_Settings, screen):
		self.ll_Settings = ll_Settings
		self.screen = screen
		
		self.image = pygame.transform.scale(pygame.image.load("images/play-button.png"), (200, 50))
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.center = self.screenRect.center
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)