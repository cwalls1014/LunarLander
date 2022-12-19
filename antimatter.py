import pygame
import os
import random
import math
from pygame.sprite import Sprite

class Antimatter(Sprite):
	def __init__(self, ll_Settings, screen, antiM):
		super(Antimatter, self).__init__()
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.screenRect = self.screen.get_rect()
		self.targetFrame = 0

		# Add antimatter images to list
		self.image1 = pygame.image.load("images/antimatter/antimatter1.png")
		self.image2 = pygame.image.load("images/antimatter/antimatter1.png")
		self.image3 = pygame.image.load("images/antimatter/antimatter2.png")
		self.image4 = pygame.image.load("images/antimatter/antimatter3.png")
		self.image5 = pygame.image.load("images/antimatter/antimatter4.png")
		self.image6 = pygame.image.load("images/antimatter/antimatter5.png")
		self.image7 = pygame.image.load("images/antimatter/antimatter6.png")
		self.image8 = pygame.image.load("images/antimatter/antimatter7.png")
		self.image9 = pygame.image.load("images/antimatter/antimatter8.png")
		self.image10 = pygame.image.load("images/antimatter/antimatter8.png")

		self.images = [
			self.image1,
			self.image2,
			self.image3,
			self.image4,
			self.image5,
			self.image6,
			self.image7,
			self.image8,
			self.image9,
			self.image10
		]

		self.rects = []

		for i in self.images:
			self.rects.append(i.get_rect())

		self.placementX = random.randrange(0, self.ll_Settings.screenWidth)
		self.placementY = random.randrange(30, self.ll_Settings.screenHeight - 100)

		for r in self.rects:
			r.centerx = self.placementX
			r.centery = self.placementY

		self.centerX1 = float(self.rects[0].centerx)
		self.centerY1 = float(self.rects[0].centery)
		self.centerX2 = float(self.rects[1].centerx)
		self.centerY2 = float(self.rects[1].centery)
		self.centerX3 = float(self.rects[2].centerx)
		self.centerY3 = float(self.rects[2].centery)
		self.centerX4 = float(self.rects[3].centerx)
		self.centerY4 = float(self.rects[3].centery)
		self.centerX5 = float(self.rects[4].centerx)
		self.centerY5 = float(self.rects[4].centery)
		self.centerX6 = float(self.rects[5].centerx)
		self.centerY6 = float(self.rects[5].centery)
		self.centerX7 = float(self.rects[6].centerx)
		self.centerY7 = float(self.rects[6].centery)
		self.centerX8 = float(self.rects[7].centerx)
		self.centerY8 = float(self.rects[7].centery)
		self.centerX9 = float(self.rects[8].centerx)
		self.centerY9 = float(self.rects[8].centery)
		self.centerX10 = float(self.rects[9].centerx)
		self.centerY10 = float(self.rects[9].centery)
		
		self.divisor = 6
		self.animationFrame = 0
		
		self.leftORright = random.randint(0, 1)
		
	def update(self):
		if self.leftORright == 0:
			self.centerX1 -= self.ll_Settings.antimatterScrollSpeed 
			self.centerX2 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX3 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX4 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX5 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX6 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX7 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX8 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX9 -= self.ll_Settings.antimatterScrollSpeed
			self.centerX10 -= self.ll_Settings.antimatterScrollSpeed
		else:
			self.centerX1 += self.ll_Settings.antimatterScrollSpeed 
			self.centerX2 += self.ll_Settings.antimatterScrollSpeed
			self.centerX3 += self.ll_Settings.antimatterScrollSpeed
			self.centerX4 += self.ll_Settings.antimatterScrollSpeed
			self.centerX5 += self.ll_Settings.antimatterScrollSpeed
			self.centerX6 += self.ll_Settings.antimatterScrollSpeed
			self.centerX7 += self.ll_Settings.antimatterScrollSpeed
			self.centerX8 += self.ll_Settings.antimatterScrollSpeed
			self.centerX9 += self.ll_Settings.antimatterScrollSpeed
			self.centerX10 += self.ll_Settings.antimatterScrollSpeed
		
		self.rects[0].centerx = self.centerX1
		self.rects[1].centerx = self.centerX2
		self.rects[2].centerx = self.centerX3
		self.rects[3].centerx = self.centerX4
		self.rects[4].centerx = self.centerX5
		self.rects[5].centerx = self.centerX6
		self.rects[6].centerx = self.centerX7
		self.rects[7].centerx = self.centerX8
		self.rects[8].centerx = self.centerX9
		self.rects[9].centerx = self.centerX10
		
		if self.animationFrame < len(self.images) * self.divisor:
			self.animationFrame += 1
			
		self.targetFrame = math.floor(self.animationFrame / self.divisor)
		
		if self.targetFrame == 9:
			self.animationFrame = 0
			self.images.reverse()
		
	def blitme(self):
		self.screen.blit(self.images[self.targetFrame], self.rects[self.targetFrame])
