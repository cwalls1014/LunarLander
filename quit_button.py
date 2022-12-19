import pygame

class QuitButton():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load("images/quit-button.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.center = self.screenRect.center
		self.rect.bottom = self.screenRect.bottom - 120
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)