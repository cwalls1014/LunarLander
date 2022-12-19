import pygame
import math

class Explosion():
	def __init__(self, screen, lander, ll_Settings):
		self.screen = screen
		self.lander = lander
		self.ll_Settings = ll_Settings
		
		self.image1 = pygame.transform.scale(pygame.image.load("images/explosion/explosion1.png"), (100, 100))
		self.image2 = pygame.transform.scale(pygame.image.load("images/explosion/explosion2.png"), (100, 100))
		self.image3 = pygame.transform.scale(pygame.image.load("images/explosion/explosion3.png"), (100, 100))
		self.image4 = pygame.transform.scale(pygame.image.load("images/explosion/explosion4.png"), (100, 100))
		self.image5 = pygame.transform.scale(pygame.image.load("images/explosion/explosion5.png"), (100, 100))
		self.image6 = pygame.transform.scale(pygame.image.load("images/explosion/explosion6.png"), (100, 100))
		self.image7 = pygame.transform.scale(pygame.image.load("images/explosion/explosion7.png"), (100, 100))
		self.image8 = pygame.transform.scale(pygame.image.load("images/explosion/explosion8.png"), (100, 100))
		self.image9 = pygame.transform.scale(pygame.image.load("images/explosion/explosion9.png"), (100, 100))
		self.image10 = pygame.transform.scale(pygame.image.load("images/explosion/explosion10.png"), (100, 100))
		self.image11 = pygame.transform.scale(pygame.image.load("images/explosion/explosion11.png"), (100, 100))
		self.image12 = pygame.transform.scale(pygame.image.load("images/explosion/explosion12.png"), (100, 100))
		self.image13 = pygame.transform.scale(pygame.image.load("images/explosion/explosion13.png"), (100, 100))
		self.image14 = pygame.transform.scale(pygame.image.load("images/explosion/explosion14.png"), (100, 100))
		self.image15 = pygame.transform.scale(pygame.image.load("images/explosion/explosion15.png"), (100, 100))
		self.image16 = pygame.transform.scale(pygame.image.load("images/explosion/explosion15.png"), (100, 100))
		
		self.rect1 = self.image1.get_rect()
		self.rect2 = self.image2.get_rect()
		self.rect3 = self.image3.get_rect()
		self.rect4 = self.image4.get_rect()
		self.rect5 = self.image5.get_rect()
		self.rect6 = self.image6.get_rect()
		self.rect7 = self.image7.get_rect()
		self.rect8 = self.image8.get_rect()
		self.rect9 = self.image9.get_rect()
		self.rect10 = self.image10.get_rect()
		self.rect11 = self.image11.get_rect()
		self.rect12 = self.image12.get_rect()
		self.rect13 = self.image13.get_rect()
		self.rect14 = self.image14.get_rect()
		self.rect15 = self.image15.get_rect()
		self.rect16 = self.image16.get_rect()
				
		self.screenRect = self.screen.get_rect()
		
		self.centerX1 = float(self.rect1.centerx)
		self.centerY1 = float(self.rect1.centery)
		self.centerX2 = float(self.rect2.centerx)
		self.centerY2 = float(self.rect2.centery)
		self.centerX3 = float(self.rect3.centerx)
		self.centerY3 = float(self.rect3.centery)
		self.centerX4 = float(self.rect4.centerx)
		self.centerY4 = float(self.rect4.centery)
		self.centerX5 = float(self.rect5.centerx)
		self.cetnerY5 = float(self.rect5.centery)
		self.centerX6 = float(self.rect6.centerx)
		self.centerY6 = float(self.rect6.centery)
		self.centerX7 = float(self.rect7.centerx)
		self.centerY7 = float(self.rect7.centery)
		self.centerX8 = float(self.rect8.centerx)
		self.centerY8 = float(self.rect8.centery)
		self.centerX9 = float(self.rect9.centerx)
		self.centerY9 = float(self.rect9.centery)
		self.centerX10 = float(self.rect10.centerx)
		self.cetnerY10 = float(self.rect10.centery)
		self.centerX11 = float(self.rect11.centerx)
		self.centerY11 = float(self.rect11.centery)
		self.centerX12 = float(self.rect12.centerx)
		self.centerY12 = float(self.rect12.centery)
		self.centerX13 = float(self.rect13.centerx)
		self.centerY13 = float(self.rect13.centery)
		self.centerX14 = float(self.rect14.centerx)
		self.centerY14 = float(self.rect14.centery)
		self.centerX15 = float(self.rect15.centerx)
		self.centerY15 = float(self.rect15.centery)
		self.centerX16 = float(self.rect16.centerx)
		self.centerY16 = float(self.rect16.centery)
		
		self.images = (
			self.image1, 
			self.image2, 
			self.image3, 
			self.image4, 
			self.image5, 
			self.image6,
			self.image7, 
			self.image8,
			self.image9, 
			self.image10, 
			self.image11,
			self.image12, 
			self.image13, 
			self.image14, 
			self.image15, 
			self.image16
		)
		
		self.rects = (
			self.rect1,
			self.rect2,
			self.rect3,
			self.rect4,
			self.rect5,
			self.rect6,
			self.rect7,
			self.rect8,
			self.rect9,
			self.rect10,
			self.rect11,
			self.rect12,
			self.rect13,
			self.rect14,
			self.rect15,
			self.rect16
		)
		
		self.exploded = False
		self.timer = False
		self.divisor = 2.0
		self.animationFrame = 0
		
	def update(self):
		self.centerX1 = self.lander.rect.centerx
		self.centerY1 = self.lander.rect.centery
		self.centerX2 = self.lander.rect.centerx
		self.centerY2 = self.lander.rect.centery
		self.centerX3 = self.lander.rect.centerx
		self.centerY3 = self.lander.rect.centery
		self.centerX4 = self.lander.rect.centerx
		self.centerY4 = self.lander.rect.centery
		self.centerX5 = self.lander.rect.centerx
		self.centerY5 = self.lander.rect.centery
		self.centerX6 = self.lander.rect.centerx
		self.centerY6 = self.lander.rect.centery
		self.centerX7 = self.lander.rect.centerx
		self.centerY7 = self.lander.rect.centery
		self.centerX8 = self.lander.rect.centerx
		self.centerY8 = self.lander.rect.centery
		self.centerX9 = self.lander.rect.centerx
		self.centerY9 = self.lander.rect.centery
		self.centerX10 = self.lander.rect.centerx
		self.centerY10 = self.lander.rect.centery
		self.centerX11 = self.lander.rect.centerx
		self.centerY11 = self.lander.rect.centery
		self.centerX12 = self.lander.rect.centerx
		self.centerY12 = self.lander.rect.centery
		self.centerX13 = self.lander.rect.centerx
		self.centerY13 = self.lander.rect.centery
		self.centerX14 = self.lander.rect.centerx
		self.centerY14 = self.lander.rect.centery
		self.centerX15 = self.lander.rect.centerx
		self.centerY15 = self.lander.rect.centery
		self.centerX16 = self.lander.rect.centerx
		self.centerY16 = self.lander.rect.centery
		
		self.rect1.centerx = self.centerX1
		self.rect1.centery = self.centerY1
		self.rect2.centerx = self.centerX2
		self.rect2.centery = self.centerY2
		self.rect3.centerx = self.centerX3
		self.rect3.centery = self.centerY3
		self.rect4.centerx = self.centerX4
		self.rect4.centery = self.centerY4
		self.rect5.centerx = self.centerX5
		self.rect5.centery = self.centerY5
		self.rect6.centerx = self.centerX6
		self.rect6.centery = self.centerY6
		self.rect7.centerx = self.centerX7
		self.rect7.centery = self.centerY7
		self.rect8.centerx = self.centerX8
		self.rect8.centery = self.centerY8
		self.rect9.centerx = self.centerX9
		self.rect9.centery = self.centerY9
		self.rect10.centerx = self.centerX10
		self.rect10.centery = self.centerY10
		self.rect11.centerx = self.centerX11
		self.rect11.centery = self.centerY11
		self.rect12.centerx = self.centerX12
		self.rect12.centery = self.centerY12
		self.rect13.centerx = self.centerX13
		self.rect13.centery = self.centerY13
		self.rect14.centerx = self.centerX14
		self.rect14.centery = self.centerY14
		self.rect15.centerx = self.centerX15
		self.rect15.centery = self.centerY15
		self.rect16.centerx = self.centerX16
		self.rect16.centery = self.centerY16
		
		if self.timer == True and self.animationFrame < len(self.images) * self.divisor:
			self.animationFrame += 1
			
		self.targetFrame = math.floor(self.animationFrame / self.divisor)
		
	def reset(self):
		self.animationFrame = 0
		self.timer = False
	
	def blitme(self):
		self.screen.blit(self.images[self.targetFrame], self.rects[self.targetFrame])
		
	def play_sound(self):
		self.explosionSound.play()