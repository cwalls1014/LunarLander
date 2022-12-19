import pygame

class HowButton():
	def __init__(self, screen):
		self.screen = screen
		
		self.image = pygame.image.load("images/how-to-play-button.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.center = self.screenRect.center
		self.rect.top = (768 / 2) + 85
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)