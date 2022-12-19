import pygame
import os
import random

class Level:
	def __init__(self, ll_Settings, screen):
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.level = []
		self.complete = False
		self.scrollSpeed = self.ll_Settings.defaultLevelScrollSpeed
		self.backgroundPath = "images/level/background"
		self.middlegroundPath = "images/level/middleground"
		self.foregroundPath = "images/level/foreground"
		self.backgroundImages = []
		self.middlegroundImages = []
		self.foregroundImages = []
		self.backgroundRects = []
		self.middlegroundRects = []
		self.foregroundRects = []
		
		# Background images
		for backgroundImage in os.listdir(self.backgroundPath):
			if not backgroundImage.startswith('.'):
				self.backgroundImages.append(pygame.image.load(f"{self.backgroundPath}/{backgroundImage}"))
		
		# Middleground images
		for middlegroundImage in os.listdir(self.middlegroundPath):
			if not middlegroundImage.startswith('.'):
				self.middlegroundImages.append(pygame.image.load(f"{self.middlegroundPath}/{middlegroundImage}"))
		
		# Foreground images
		for foregroundImage in os.listdir(self.foregroundPath):
			if not foregroundImage.startswith('.'):
				self.foregroundImages.append(pygame.image.load(f"{self.foregroundPath}/{foregroundImage}"))
		
		# Background rects
		for backgroundRect in self.backgroundImages:
			self.backgroundRects.append(backgroundRect.get_rect())
			
		# Middleground rects
		for middlegroundRect in self.middlegroundImages:
			self.middlegroundRects.append(middlegroundRect.get_rect())
			
		# Foreground rects
		for foregroundRect in self.foregroundImages:
			self.foregroundRects.append(foregroundRect.get_rect())

	def update(self):
		self.backgroundCenterX -= (self.scrollSpeed * 0.6)
		self.middlegroundCenterX -= (self.scrollSpeed * 0.3)
		self.foregroundCenterX -= self.scrollSpeed
		
		self.level[0][1].centerx = self.backgroundCenterX
		self.level[1][1].centerx = self.middlegroundCenterX
		self.level[2][1].centerx = self.foregroundCenterX
		
		if self.level[2][1].right <= self.screenRect.right:
			self.scrollSpeed = 0.0
			self.ll_Settings.callDropship = True

	def set_level(self):
		self.level = [[random.choice(self.backgroundImages), random.choice(self.backgroundRects)],[random.choice(self.middlegroundImages), random.choice(self.middlegroundRects)],[random.choice(self.foregroundImages), random.choice(self.foregroundRects)]]
		
		self.reset_level()
	
	def reset_level(self):
		self.level[0][1].left = self.screenRect.left
		self.level[0][1].top = self.screenRect.top
		self.level[1][1].left = self.screenRect.right + 50
		self.level[1][1].top = self.screenRect.top + 100
		self.level[2][1].left = self.screenRect.left
		self.level[2][1].bottom = self.screenRect.bottom
		
		self.backgroundCenterX = float(self.level[0][1].centerx)
		self.middlegroundCenterX = float(self.level[1][1].centerx)
		self.foregroundCenterX = float(self.level[2][1].centerx)
		
		self.scrollSpeed = self.ll_Settings.defaultLevelScrollSpeed
			
	def blitme(self):
		self.screen.blit(self.level[0][0], self.level[0][1])
		self.screen.blit(self.level[1][0], self.level[1][1])
		self.screen.blit(self.level[2][0], self.level[2][1])
