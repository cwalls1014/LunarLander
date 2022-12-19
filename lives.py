import pygame

class Lives:
	def __init__(self, screen):
		self.screen = screen
		self.image1 = pygame.transform.scale(pygame.image.load("images/lander.png"), (60, 45))
		self.image2 = pygame.transform.scale(pygame.image.load("images/lander.png"), (60, 45))
		self.image3 = pygame.transform.scale(pygame.image.load("images/lander.png"), (60, 45))
		self.screenRect = self.screen.get_rect()
		self.rect1 = self.image1.get_rect()
		self.rect2 = self.image2.get_rect()
		self.rect3 = self.image3.get_rect()
		
		self.rect1.top = self.screenRect.top
		self.rect1.left = self.screenRect.left
		self.rect2.top = self.screenRect.top
		self.rect2.left = self.rect1.right
		self.rect3.top = self.screenRect.top
		self.rect3.left = self.rect2.right
		
	def blitme1(self):
		self.screen.blit(self.image1, self.rect1)
		self.screen.blit(self.image2, self.rect2)
		self.screen.blit(self.image3, self.rect3)
		
	def blitme2(self):
		self.screen.blit(self.image1, self.rect1)
		self.screen.blit(self.image2, self.rect2)
		
	def blitme3(self):
		self.screen.blit(self.image1, self.rect1)