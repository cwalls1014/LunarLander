import pygame
import random
import os
import math

class Flames:
	def __init__(self, ll_Settings, screen, lander):
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.lander = lander
		self.path = "images/thruster"
		self.thruster = []
		self.rects = []
		self.screenRect = self.screen.get_rect()
		self.landerRect = self.lander.rect
		self.engaged = False
		self.divisor = 2
		self.animationFrame = 0
		self.targetFrame = 0
		
		for image in os.listdir(self.path):
			if not image.startswith('.'):
				self.thruster.append(pygame.image.load(f"{self.path}/{image}"))

		for rect in self.thruster:
			self.rects.append(rect.get_rect())
			
	def update(self):
		for r in self.rects:
			r.top = self.landerRect.bottom
			r.centerx = self.landerRect.centerx
			
		if self.animationFrame < 15 * self.divisor:
			self.animationFrame += 1
			
		self.targetFrame = math.floor(self.animationFrame / self.divisor)
		
		if self.animationFrame == 15:
			self.animationFrame = 0
		
	def blitme(self):
		self.screen.blit(self.thruster[self.targetFrame], self.rects[self.targetFrame])
		