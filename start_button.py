import pygame

class StartButton():
	def __init__(self, ll_Settings, screen):
		self.screen = screen
		
		self.image = pygame.image.load("images/start-button.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.center = self.screenRect.center
		self.rect.top = self.screenRect.top + 400
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)