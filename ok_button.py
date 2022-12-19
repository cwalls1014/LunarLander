import pygame

class OKButton():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load("images/ok-button.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.center = self.screenRect.center
		self.rect.bottom = self.screenRect.bottom - 10
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)