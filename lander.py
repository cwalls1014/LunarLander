import pygame
from pygame.sprite import Sprite

class Lander(Sprite):
	def __init__(self, ll_Settings, screen):
		"""Initialize the lander and set it's starting position"""
		super(Lander, self).__init__()
		self.screen = screen
		self.ll_Settings = ll_Settings
		self.invincibleCode = [pygame.K_l, pygame.K_l, pygame.K_i, pygame.K_n, pygame.K_v]
		self.unlimitedFuelCode = [pygame.K_l, pygame.K_l, pygame.K_f, pygame.K_u, pygame.K_l]
		self.checkLLinv = []
		self.checkLLful = []
		self.invincible = False
		self.unlimitedFuel = False
		self.docked = True
		self.released = True
		self.startingX = 300
		self.startingY = 150
		self.beamed = False
		
		# Load the lander image and get it's rect
		self.image = pygame.image.load("images/lander.png")
		self.rect = self.image.get_rect()
		self.screenRect = screen.get_rect()
		
		# Start the lander at the dropship release bay
		self.rect.centerx = 340
		self.rect.centery = 150
		
		# Store a decimal value for the lander's center
		self.centerX = float(self.rect.centerx)
		self.centerY = float(self.rect.centery)
		
		# Movement flags
		self.movingUp = False
		self.movingRight = False
		self.movingLeft = False
		
	def update(self):
		"""Update the lander's position based on the movement flag"""
		# Update the lander's speed
		if self.movingUp == True and self.ll_Settings.landerFuel > 0:
			self.ll_Settings.verticalSpeed -= 0.2
		else:
			self.ll_Settings.verticalSpeed += self.ll_Settings.gravity
		if self.movingRight == True:
			self.ll_Settings.horizontalSpeed += .2
		if self.movingLeft == True:
			self.ll_Settings.horizontalSpeed -= .2
			
		# Lander undocking
		if self.released:
			self.centerY += 10
			if self.rect.bottom >= 250:
				self.released = False
			
		# Update lander's center value, not rect
		self.centerX += self.ll_Settings.horizontalSpeed
		self.centerY += self.ll_Settings.verticalSpeed
		
		# Restrict lander movement
		if self.rect.left <= self.screenRect.left:
			self.ll_Settings.horizontalSpeed = 5.0
		if self.rect.right >= self.screenRect.right:
			self.ll_Settings.horizontalSpeed = -5.0
		if self.rect.top <= self.screenRect.top:
			self.ll_Settings.verticalSpeed = self.ll_Settings.gravity + 5.0			
		
		# Update rect object from self.center
		self.rect.centerx = self.centerX
		self.rect.centery = self.centerY
		
	def blitme(self):
		"""Draw the ship at it's current location"""
		self.screen.blit(self.image, self.rect)

	def reset_lander(self):
		self.docked = True
		self.released = True
		self.ll_Settings.horizontalSpeed = 0.0
		self.ll_Settings.verticalSpeed = 0.0
		self.centerX = self.startingX
		self.centerY = self.startingY
		self.rect.centerx = self.centerX
		self.rect.centery = self.centerY
		self.beamed = False
		
	def evac(self, dropship, tractorBeam):
		if self.ll_Settings.tractorBeamOn:
			for r in tractorBeam.rects:
				if r.contains(self.rect):
					self.beamed = True
					self.ll_Settings.verticalSpeed -= 0.1
					if self.centerX > 305:
						self.centerX -= 1.0
					else:
						self.centerX += 1.0
					self.ll_Settings.horizontalSpeed = 0.0
					if self.centerY <= self.startingY:
						self.ll_Settings.verticalSpeed = 0.0
				if self.rect.bottom <= 200 and self.beamed:
					self.docked = True
