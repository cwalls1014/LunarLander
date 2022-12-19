import pygame
import pygame.font

class EnterName:
	def __init__(self, screen):
		self.screen = screen
		self.ui = pygame.image.load("images/enter-name-ui.png")
		self.uiRect = self.ui.get_rect()
		self.screenRect = screen.get_rect()
		self.viewed = False
		self.uiRect.top = self.screenRect.top
		self.uiRect.left = self.screenRect.left
		self.linkColor = (255, 255, 255)
		
		self.text = f"Click here to see high scores!"
		self.font = pygame.font.SysFont(None, 32)
		self.textColor = pygame.Color(255, 255, 255)
		self.name = ''
		self.textImage = self.font.render(self.name, True, (self.textColor))
		self.linkImage = self.font.render(self.text, True, (self.linkColor))
		self.linkRect = self.linkImage.get_rect()
		self.inputRect = pygame.Rect(self.screenRect.centerx - 80, self.screenRect.centery, 140, 32)
		self.bgColor = pygame.Color(68, 237, 248)
		
		self.linkRect.centerx = self.uiRect.centerx
		self.linkRect.centery = self.uiRect.bottom - 50
	
	def update(self):
		self.textImage = self.font.render(self.name, True, (self.textColor))
		self.inputRect.width = max(210, self.textImage.get_width() + 10)
		
	def blitme(self):
		self.screen.blit(self.ui, self.uiRect)
		pygame.draw.rect(self.screen, self.bgColor, self.inputRect)
		self.screen.blit(self.textImage, (self.inputRect.x + 5, self.inputRect.y + 5))
		self.screen.blit(self.linkImage, self.linkRect)