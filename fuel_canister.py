import pygame
import random
from pygame.sprite import Sprite

class FuelCanister(Sprite):
	def __init__(self, ll_Settings, screen, fuelCanisters):
		super(FuelCanister, self).__init__()
		self.ll_Settings = ll_Settings
		self.screen = screen
		
		self.image = pygame.image.load("images/fuel-canister.png")
		self.rect = self.image.get_rect()
		self.screenRect = self.screen.get_rect()
		
		self.placementY = random.randrange(30, self.ll_Settings.screenHeight - 100)
		
		self.rect.left = self.screenRect.right
		self.rect.bottom = self.placementY
		
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
				
	def update(self):
		self.centerX -= self.ll_Settings.fuelCanisterScrollSpeed
		self.rect.centerx = self.centerX
		self.ll_Settings.rotation += 1
		
	def blitme(self):
		self.screen.blit(pygame.transform.rotate(self.image, self.ll_Settings.rotation), self.rect)