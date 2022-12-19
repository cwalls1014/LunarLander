import pygame

class CreditsButton:
	def __init__(self, screen):
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.image = pygame.image.load("images/credits-button.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = self.screenRect.centerx
		self.rect.bottom = self.screenRect.bottom - 185
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
	