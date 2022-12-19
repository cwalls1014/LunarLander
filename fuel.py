import pygame
import math

class Fuel:
	def __init__(self, ll_Settings, screen, lander, stats):
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.lander = lander
		self.stats = stats
		
		self.image1 = pygame.image.load("images/fuel.png")
		self.image2 = pygame.image.load("images/fuel-border.png")
		self.rect1 = self.image1.get_rect()
		self.rect2 = self.image2.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.rect1.top = self.screenRect.top + 74
		self.rect1.left = self.screenRect.left + 2
		self.rect2.top = self.screenRect.top + 72
		self.rect2.left = self.screenRect.left
		
	def update(self):
		if self.lander.movingUp and not self.lander.docked and self.ll_Settings.landerFuel >= 0:
			self.image1 = pygame.transform.scale(pygame.image.load("images/fuel.png"), (self.ll_Settings.landerFuel, 16))
			self.rect1 = self.image1.get_rect()
			self.rect1.top = self.screenRect.top + 74
			self.rect1.left = self.screenRect.left + 2
			self.ll_Settings.landerFuel -= 1
			
	def blitme(self):
		self.screen.blit(self.image2, self.rect2)
		self.screen.blit(self.image1, self.rect1)
		
	def reset_fuel(self):
		self.ll_Settings.landerFuel = 200
		self.image1 = pygame.transform.scale(pygame.image.load("images/fuel.png"), (self.ll_Settings.landerFuel, 16))
	