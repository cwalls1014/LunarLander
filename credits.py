import pygame

class Credits:
	def __init__(self, screen):
		self.screen = screen
		self.viewed = False
		self.font = pygame.font.SysFont(None, 42)
		self.textColor = (255, 255, 255)
		self.headerColor = (24, 240, 223)
		self.background = pygame.image.load("images/nolines.png")
		self.screenRect = self.screen.get_rect()
		self.backgroundRect = self.background.get_rect()
		self.musicText = "MUSIC"
		self.sadSong = "Darkman007 - Sad Song"
		self.promises = "Darkman007 - Promises"
		self.threeDgalax = "Dubmood - 3D Galax"
		self.grassNearTheHouse = "Darkman007 - Grass Near the House"
		self.mrDroichen = "Darkman007 - Mr. Droichen"
		self.iWantSleep = "Karloz - I Want Sleep"
		self.dancing = "Fearofdark - Dancing on the M%n"
		self.boner = "Marx Marvelous - Boner"
		self.spaceTheme = "Charlie Axl Tebbutt - A Theme for Space"
		self.uiGraphicsText = "UI GRAPHICS"
		self.jEverettText = "Joseph Everett"
		self.programmerText = "PROGRAMMER"
		self.mWallsText = "Matthew Walls"
		self.madeWithText = "MADE WITH:"
		self.pygameLogo = pygame.image.load("images/pygame-logo.png")
		
		self.musicTextImage = self.font.render(self.musicText, True, self.headerColor)
		self.musicTextImageRect = self.musicTextImage.get_rect()
		
		self.uiGraphicsTextImage = self.font.render(self.uiGraphicsText, True, self.headerColor)
		self.uiGraphicsTextImageRect = self.uiGraphicsTextImage.get_rect()
		
		self.sadSongImage = self.font.render(self.sadSong, True, self.textColor)
		self.sadSongImageRect = self.sadSongImage.get_rect()
		
		self.promisesImage = self.font.render(self.promises, True, self.textColor)
		self.promisesImageRect = self.promisesImage.get_rect()
		
		self.threeDgalaxImage = self.font.render(self.threeDgalax, True, self.textColor)
		self.threeDgalaxImageRect = self.threeDgalaxImage.get_rect()
		
		self.grassNearTheHouseImage = self.font.render(self.grassNearTheHouse, True, self.textColor)
		self.grassNearTheHouseImageRect = self.grassNearTheHouseImage.get_rect()
		
		self.mrDroichenImage = self.font.render(self.mrDroichen, True, self.textColor)
		self.mrDroichenImageRect = self.mrDroichenImage.get_rect()
		
		self.iWantSleepImage = self.font.render(self.iWantSleep, True, self.textColor)
		self.iWantSleepImageRect = self.iWantSleepImage.get_rect()
		
		self.dancingImage = self.font.render(self.dancing, True, self.textColor)
		self.dancingImageRect = self.dancingImage.get_rect()
		
		self.bonerImage = self.font.render(self.boner, True, self.textColor)
		self.bonerImageRect = self.bonerImage.get_rect()
		
		self.spaceThemeImage = self.font.render(self.spaceTheme, True, self.textColor)
		self.spaceThemeImageRect = self.spaceThemeImage.get_rect()
		
		self.jEverettTextImage = self.font.render(self.jEverettText, True, self.textColor)
		self.jEverettTextImageRect = self.jEverettTextImage.get_rect()
		
		self.programmerTextImage = self.font.render(self.programmerText, True, self.headerColor)
		self.programmerTextImageRect = self.programmerTextImage.get_rect()
		
		self.mWallsTextImage = self.font.render(self.mWallsText, True, self.textColor)
		self.mWallsTextImageRect = self.mWallsTextImage.get_rect()
		
		self.madeWithTextImage = self.font.render(self.madeWithText, True, self.headerColor)
		self.madeWithTextImageRect = self.madeWithTextImage.get_rect()
		
		self.pygameLogoRect = self.pygameLogo.get_rect()
		
		
		self.backgroundRect.center = self.screenRect.center
		self.musicTextImageRect.centerx = self.screenRect.centerx
		self.musicTextImageRect.top = self.screenRect.bottom
		
		self.sadSongImageRect.centerx = self.screenRect.centerx
		self.sadSongImageRect.top = self.musicTextImageRect.bottom + 80
		
		self.promisesImageRect.centerx = self.screenRect.centerx
		self.promisesImageRect.top = self.sadSongImageRect.bottom + 10
		
		self.threeDgalaxImageRect.centerx = self.screenRect.centerx
		self.threeDgalaxImageRect.top = self.promisesImageRect.bottom + 10
		
		self.grassNearTheHouseImageRect.centerx = self.screenRect.centerx
		self.grassNearTheHouseImageRect.top = self.threeDgalaxImageRect.bottom + 10
		
		self.mrDroichenImageRect.centerx = self.screenRect.centerx
		self.mrDroichenImageRect.top = self.grassNearTheHouseImageRect.bottom + 10
		
		self.iWantSleepImageRect.centerx = self.screenRect.centerx
		self.iWantSleepImageRect.top = self.mrDroichenImageRect.bottom + 10
		
		self.dancingImageRect.centerx = self.screenRect.centerx
		self.dancingImageRect.top = self.iWantSleepImageRect.bottom + 10
		
		self.bonerImageRect.centerx = self.screenRect.centerx
		self.bonerImageRect.top = self.dancingImageRect.bottom + 10
		
		self.spaceThemeImageRect.centerx = self.screenRect.centerx
		self.spaceThemeImageRect.top = self.bonerImageRect.bottom + 10
		
		self.uiGraphicsTextImageRect.centerx = self.screenRect.centerx
		self.uiGraphicsTextImageRect.top = self.spaceThemeImageRect.bottom + 160
		
		self.jEverettTextImageRect.centerx = self.screenRect.centerx
		self.jEverettTextImageRect.top = self.uiGraphicsTextImageRect.bottom + 80
		
		self.programmerTextImageRect.centerx = self.screenRect.centerx
		self.programmerTextImageRect.top = self.jEverettTextImageRect.bottom + 160
		
		self.mWallsTextImageRect.centerx = self.screenRect.centerx
		self.mWallsTextImageRect.top = self.programmerTextImageRect.bottom + 80
		
		self.madeWithTextImageRect.centerx = self.screenRect.centerx
		self.madeWithTextImageRect.top = self.mWallsTextImageRect.bottom + 160
		
		self.pygameLogoRect.centerx = self.screenRect.centerx
		self.pygameLogoRect.top = self.madeWithTextImageRect.bottom + 80
		
		self.centerY = self.musicTextImageRect.centery
		
	def update(self):
		if self.pygameLogoRect.bottom > self.screenRect.top:
			self.musicTextImageRect.centery -= 2
			self.sadSongImageRect.centery -= 2
			self.promisesImageRect.centery -= 2
			self.threeDgalaxImageRect.centery -= 2
			self.grassNearTheHouseImageRect.centery -= 2
			self.mrDroichenImageRect.centery -= 2
			self.iWantSleepImageRect.centery -= 2
			self.dancingImageRect.centery -= 2
			self.bonerImageRect.centery -= 2
			self.spaceThemeImageRect.centery -= 2
			self.uiGraphicsTextImageRect.centery -= 2
			self.jEverettTextImageRect.centery -= 2
			self.programmerTextImageRect.centery -= 2
			self.mWallsTextImageRect.centery -= 2
			self.madeWithTextImageRect.centery -= 2
			self.pygameLogoRect.centery -= 2
		elif self.pygameLogoRect.bottom < self.screenRect.top:
			self.musicTextImageRect.centery += 2300
			self.sadSongImageRect.centery += 2300
			self.promisesImageRect.centery += 2300
			self.threeDgalaxImageRect.centery += 2300
			self.grassNearTheHouseImageRect.centery += 2300
			self.mrDroichenImageRect.centery += 2300
			self.iWantSleepImageRect.centery += 2300
			self.dancingImageRect.centery += 2300
			self.bonerImageRect.centery += 2300
			self.spaceThemeImageRect.centery += 2300
			self.uiGraphicsTextImageRect.centery += 2300
			self.jEverettTextImageRect.centery += 2300
			self.programmerTextImageRect.centery += 2300
			self.mWallsTextImageRect.centery += 2300
			self.madeWithTextImageRect.centery += 2300
			self.pygameLogoRect.centery += 2300
		
	def blitme(self):
		self.screen.blit(self.background, self.backgroundRect)
		self.screen.blit(self.musicTextImage, self.musicTextImageRect)
		self.screen.blit(self.sadSongImage, self.sadSongImageRect)
		self.screen.blit(self.promisesImage, self.promisesImageRect)
		self.screen.blit(self.threeDgalaxImage, self.threeDgalaxImageRect)
		self.screen.blit(self.grassNearTheHouseImage, self.grassNearTheHouseImageRect)
		self.screen.blit(self.mrDroichenImage, self.mrDroichenImageRect)
		self.screen.blit(self.iWantSleepImage, self.iWantSleepImageRect)
		self.screen.blit(self.dancingImage, self.dancingImageRect)
		self.screen.blit(self.bonerImage, self.bonerImageRect)
		self.screen.blit(self.spaceThemeImage, self.spaceThemeImageRect)
		self.screen.blit(self.uiGraphicsTextImage, self.uiGraphicsTextImageRect)
		self.screen.blit(self.jEverettTextImage, self.jEverettTextImageRect)
		self.screen.blit(self.programmerTextImage, self.programmerTextImageRect)
		self.screen.blit(self.mWallsTextImage, self.mWallsTextImageRect)
		self.screen.blit(self.madeWithTextImage, self.madeWithTextImageRect)
		self.screen.blit(self.pygameLogo, self.pygameLogoRect)
		