import pygame

class HowToPlay:
	def __init__(self, screen):
		self.viewed = False
		self.font = pygame.font.SysFont(None, 42)
		self.textColor = (255, 255, 255)
		self.screen = screen
		self.background = pygame.image.load("images/how-to-play.png")
		self.lander = pygame.image.load("images/how-lander.png")
		self.fuelCanister = pygame.image.load("images/how-fuel.png")
		self.landingPad = pygame.image.load("images/how-pad.png")
		self.antimatter = pygame.image.load("images/how-matter.png")
		
		self.backgroundRect = self.background.get_rect()
		self.screenRect = self.screen.get_rect()
		self.landerRect = self.lander.get_rect()
		self.fuelCanisterRect = self.fuelCanister.get_rect()
		self.landingPadRect = self.landingPad.get_rect()
		self.antimatterRect = self.antimatter.get_rect()
		
		self.landerText = " Your lander: 'A' is left, 'D' is right, 'W' is up. Press ESC to pause"
		self.fuelCanisterText = " Collect a fuel barrel to refuel your thrusters"
		self.landingPadText = " Land safely on a landing pad for extra points"
		self.antimatterText = " Collect 5 in a row without landing or refueling for bonus points"
		
		self.landerTextImage = self.font.render(self.landerText, True, self.textColor)
		self.landerTextImageRect = self.landerTextImage.get_rect()
		self.fuelCanisterTextImage = self.font.render(self.fuelCanisterText, True, self.textColor)
		self.fuelCanisterTextImageRect = self.fuelCanisterTextImage.get_rect()
		self.landingPadTextImage = self.font.render(self.landingPadText, True, self.textColor)
		self.landingPadTextImageRect = self.landingPadTextImage.get_rect()
		self.antimatterTextImage = self.font.render(self.antimatterText, True, self.textColor)
		self.antimatterTextImageRect = self.antimatterTextImage.get_rect()
		
		self.backgroundRect.center = self.screenRect.center
		
		self.landerRect.left = self.screenRect.left + 10
		self.landerRect.top = self.screenRect.top + 135
		self.landerTextImageRect.left = self.landerRect.right
		self.landerTextImageRect.centery = self.landerRect.centery
		
		self.fuelCanisterRect.centerx = self.landerRect.centerx
		self.fuelCanisterRect.top = self.landerRect.bottom + 10
		self.fuelCanisterTextImageRect.left = self.fuelCanisterRect.right
		self.fuelCanisterTextImageRect.centery = self.fuelCanisterRect.centery
		
		self.landingPadRect.left = self.screenRect.left + 10
		self.landingPadRect.top = self.fuelCanisterRect.bottom + 10
		self.landingPadTextImageRect.left = self.landingPadRect.right
		self.landingPadTextImageRect.centery = self.landingPadRect.centery
		
		self.antimatterRect.left = self.screenRect.left + 10
		self.antimatterRect.top = self.landingPadRect.bottom + 10
		self.antimatterTextImageRect.left = self.antimatterRect.right
		self.antimatterTextImageRect.centery = self.antimatterRect.centery
		
	def blitme(self):
		self.screen.blit(self.background, self.backgroundRect)
		
		self.screen.blit(self.lander, self.landerRect)
		self.screen.blit(self.landerTextImage, self.landerTextImageRect)
		
		self.screen.blit(self.fuelCanister, self.fuelCanisterRect)
		self.screen.blit(self.fuelCanisterTextImage, self.fuelCanisterTextImageRect)
		
		self.screen.blit(self.landingPad, self.landingPadRect)
		self.screen.blit(self.landingPadTextImage, self.landingPadTextImageRect)
		
		self.screen.blit(self.antimatter, self.antimatterRect)
		self.screen.blit(self.antimatterTextImage, self.antimatterTextImageRect)
		