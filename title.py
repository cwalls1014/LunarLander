import pygame

class Title:
	def __init__(self, screen):
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.titleScreen = pygame.image.load("images/title-screen.png")
		self.titleText = pygame.image.load("images/title.png")
		self.titleTextRect = self.titleText.get_rect()
		self.titleRect = self.titleScreen.get_rect()
		self.viewed = True
		
		self.titleRect.center = self.screenRect.center
		self.titleTextRect.top = self.screenRect.top + 160
		self.titleTextRect.centerx = self.screenRect.centerx
		
	def blitme(self):
		self.screen.blit(self.titleScreen, self.titleRect)
		self.screen.blit(self.titleText, self.titleTextRect)