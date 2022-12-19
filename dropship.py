import pygame

class Dropship:
	def __init__(self, screen, lander, stats, ll_Settings):
		self.screen = screen
		self.lander = lander
		self.stats = stats
		self.ll_Settings = ll_Settings
		self.screenRect = self.screen.get_rect()
		self.speed = 0
		self.called = True
		self.evac = False
		
		self.image = pygame.image.load("images/dropship.png")
		self.rect = self.image.get_rect()
		
		self.rect.right = self.screenRect.left - 100
		self.rect.top = self.screenRect.top
		
		self.centerX = float(self.rect.centerx)
		
		self.timer = 3
		
	def call_dropship(self):
		if self.called:
			self.reset_dropship()
			self.called = False
		
		if not self.lander.docked and self.rect.centerx <= self.screenRect.left:
			self.speed += 1
			
		if self.rect.centerx >= self.screenRect.left and self.speed > 0:
			self.speed -= 1
			
		if self.speed == 0.0:
			if self.ll_Settings.tractorBeamTimer == self.ll_Settings.defaultTractorBeamTimer:
				self.ll_Settings.ch5.play(self.ll_Settings.tractorbeamSound)
			else:
				self.ll_Settings.tractorBeamOn = True
				
			self.ll_Settings.tractorBeamTimer -= 1
				
		if self.ll_Settings.tractorBeamTimer <= 0:
			self.ll_Settings.tractorBeamOn = False
			self.speed += 2.0
				
		self.centerX += self.speed
		self.rect.centerx = self.centerX
		
		if self.rect.left >= self.screenRect.right:
			if not self.lander.docked:
				self.evac = False
			else:
				self.evac = True
				
		if self.called:
			self.ll_Settings.ch5.stop()
		
	def update(self):
		if self.lander.docked and self.stats.gameActive:
			self.ll_Settings.ch6.play(self.ll_Settings.dropshipSound)
			
		if self.lander.docked and self.rect.centerx <= self.screenRect.left:
			self.speed += 1

		if self.rect.centerx >= self.screenRect.left and self.speed > 1:
			self.speed -= 1
			
		if self.speed <= 1.5:
			self.timer -= 1
			if self.timer == 0:
				self.lander.docked = False
				
		if not self.lander.docked:
			self.speed += 2.0
			
		if self.rect.left >= self.screenRect.right:
			self.speed = 0.0

		self.centerX += self.speed
		self.rect.centerx = self.centerX
		
	def reset_dropship(self):
		self.timer = 3
		self.called = True
		self.speed = 0
		self.rect.right = self.screenRect.left - 100
		self.rect.top = self.screenRect.top
		self.centerX = self.rect.centerx
		self.evac = False
		self.ll_Settings.callDropship = False
		self.ll_Settings.tractorBeamOn = False
		self.ll_Settings.tractorBeamTimer = self.ll_Settings.defaultTractorBeamTimer
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		