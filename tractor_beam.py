import pygame
import math

class TractorBeam:
	def __init__(self, screen, ll_Settings, lander):
		self.screen = screen
		self.ll_Settings = ll_Settings
		self.lander = lander
		self.divisor = 6
		self.animationFrame = 0
		self.targetFrame = 0
		
		self.screenRect = self.screen.get_rect()
		
		self.beam1 = pygame.image.load("images/tractorbeam/beam1.png")
		self.beam2 = pygame.image.load("images/tractorbeam/beam2.png")
		self.beam3 = pygame.image.load("images/tractorbeam/beam3.png")
		self.beam4 = pygame.image.load("images/tractorbeam/beam3.png")
		
		self.images = [
			self.beam1,
			self.beam2,
			self.beam3,
			self.beam4
		]
		
		self.beam1Rect = self.beam1.get_rect()
		self.beam2Rect = self.beam2.get_rect()
		self.beam3Rect = self.beam3.get_rect()
		self.beam4Rect = self.beam4.get_rect()
		
		self.rects = [
			self.beam1Rect,
			self.beam2Rect,
			self.beam3Rect,
			self.beam4Rect
		]
		
		self.beam1Rect.centerx = 305
		self.beam1Rect.centery = 250
		self.beam2Rect.centerx = 305
		self.beam2Rect.centery = 250
		self.beam3Rect.centerx = 305
		self.beam3Rect.centery = 250
		self.beam4Rect.centerx = 305
		self.beam4Rect.centery = 250
	
	def update(self):
		
		if self.animationFrame < 3 * self.divisor:
			self.animationFrame += 1
			
		self.targetFrame = math.floor(self.animationFrame / self.divisor)
		
		if self.targetFrame == 3:
			self.animationFrame = 0
		
	def blitme(self):
		self.screen.blit(self.images[self.targetFrame], self.rects[self.targetFrame])