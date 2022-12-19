import pygame.font
from pygame.sprite import Group
from lander import Lander

class Scoreboard():
	def __init__(self, ll_Settings, screen, stats):
		self.ll_Settings = ll_Settings
		self.screen = screen
		self.stats = stats
		self.screenRect = self.screen.get_rect()
		self.highscore = 0
		self.textColor = (255, 255, 255)
		self.antiTextColor = (24, 240, 223)
		self.font = pygame.font.SysFont(None, 48)
		self.matterFont = pygame.font.SysFont(None, 36)
		
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_landers()
		self.prep_antimatter()
		
	def prep_score(self):
		roundedScore = int(round(self.stats.score, -1))
		scoreStr = "{:,}".format(roundedScore)
		self.scoreImage = self.font.render(scoreStr, True, self.textColor)
		self.scoreRect = self.scoreImage.get_rect()
		self.scoreRect.right = self.screenRect.right - 20
		self.scoreRect.top = 20
		
	def prep_high_score(self):
		self.highscoreImage = self.font.render(f"Highscore: {self.highscore}", True, self.textColor)
		self.highscoreRect = self.highscoreImage.get_rect()
		self.highscoreRect.top = 20
		self.highscoreRect.centerx = self.screenRect.centerx
	
	def prep_level(self):
		self.levelImage = self.font.render(f"Level: {self.stats.currentLevel}", True, self.textColor)
		self.levelRect = self.levelImage.get_rect()
		self.levelRect.right = self.scoreRect.right
		self.levelRect.top = self.scoreRect.bottom + 10
		
	def prep_landers(self):
		self.landers = Group()
		for landerNumber in range(self.stats.landersLeft):
			lander = Lander(self.ll_Settings, self.screen)
			lander.rect.x = 10 + landerNumber * lander.rect.width
			lander.rect.y = 10
			self.landers.add(lander)
			
	def prep_antimatter(self):
		self.antimatterImage = self.matterFont.render(f"Antimatter: {self.stats.antimatter}", True, self.antiTextColor)
		self.antimatterRect = self.antimatterImage.get_rect()
		self.antimatterRect.left = self.screenRect.left + 10
		self.antimatterRect.top = self.screenRect.top + 100
		
	def show_score(self):
		self.screen.blit(self.antimatterImage, self.antimatterRect)
		self.screen.blit(self.scoreImage, self.scoreRect)
		self.screen.blit(self.levelImage, self.levelRect)
		self.screen.blit(self.highscoreImage, self.highscoreRect)
		self.landers.draw(self.screen)