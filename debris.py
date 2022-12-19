import pygame
from pygame.sprite import Sprite
import math
import random
import os

class Debris(Sprite):
	def __init__(self, ll_Settings, screen, debris, lander):
		super(Debris, self).__init__()
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.lander = lander
		self.debrisTravel = 0
		self.speed = random.randint(1, 10)
		self.images = []
		self.rects = []
		self.imageRects = []
		self.path = "images/debris"
		self.screenRect = self.screen.get_rect()
		
		# Add debris images to list
		for image in os.listdir(self.path):
			if not image.startswith('.'):
				self.images.append(pygame.image.load(f"{self.path}/{image}"))
		
		# Get rects of images and add to rects list
		for image in self.images:
			self.rects.append(image.get_rect())
		
		# Place rects on the screen
		for rect in self.rects:
			self.leftRight = random.randint(0, 1)
			if self.leftRight == 0:
				rect.left = self.screenRect.right
				rect.bottom = self.screenRect.top
			elif self.leftRight == 1:
				rect.right = self.screenRect.left
				rect.bottom  = self.screenRect.top
			
			
		# Populate imageRects list
		for i in range(len(self.images)):
			self.imageRects.append((self.images[i], self.rects[i]))
			
		# Choose random imageRect
		self.currentImage = random.choice(self.imageRects)
		# Assign centerX and centerY to image rect.centerx and rect.centery
		self.centerX = self.currentImage[1].centerx
		self.centerY = self.currentImage[1].centery

		# Calculate angle
		self.distanceX = lander.rect.centerx - self.centerX
		self.distanceY = lander.rect.centery - self.centerY
		self.theta = math.atan2(self.distanceX, self.distanceY)
		
	def update(self):
		self.debrisTravel += self.speed
		self.currentImage[1].centerx = self.centerX + math.sin(self.theta) * self.debrisTravel
		self.currentImage[1].centery = self.centerY + math.cos(self.theta) * self.debrisTravel
	
	def blitme(self):
		self.screen.blit(pygame.transform.rotate(self.currentImage[0], self.ll_Settings.rotation), self.currentImage[1])
