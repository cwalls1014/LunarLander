import pygame
import random

class LandingPad():
	def __init__(self, ll_Settings, screen):
		self.ll_Settings = ll_Settings
		self.screen = screen
		
		self.image = pygame.image.load("images/landing-pad.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect.bottom = random.randint(100, (self.screenRect.bottom - 100))
		self.rect.left = self.screenRect.right + 150
		
		self.centerX = self.rect.centerx
		self.centerY = self.rect.centery
		
	def update(self):
		self.centerX -= self.ll_Settings.landingPadScrollSpeed
		
		if self.rect.right <= self.screenRect.left:
			self.reset_landingPad()
		
		self.rect.centerx = self.centerX
	
	def reset_landingPad(self):
		self.centerX = self.screenRect.right + 150
		self.centerY = random.randint(100, (self.screenRect.bottom - 100))
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
