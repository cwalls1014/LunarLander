import pygame
import os

class Settings():
	"""A class to store all settings for Lunar Lander"""
	def __init__(self):
		"""Initialize static settings"""
		# screen settings
		self.screenWidth = 1024
		self.screenHeight = 768
		self.bgColor = (0, 0, 0)
		self.musicPath = "sounds/music"
		self.music = []
		
		# Music and sounds
		self.ch1 = pygame.mixer.Channel(1) # Rocket sound
		self.ch2 = pygame.mixer.Channel(2) # Antimatter sound, Code sound
		self.ch3 = pygame.mixer.Channel(3) # Fuel sound
		self.ch4 = pygame.mixer.Channel(4) # Explosion sound
		self.ch5 = pygame.mixer.Channel(5) # Tractorbeam sound
		self.ch6 = pygame.mixer.Channel(6) # Dropship sound, bonusPointsSound
		self.ch7 = pygame.mixer.Channel(7) # Gameover sound, points sound
		
		self.rocketSound = pygame.mixer.Sound("sounds/rocket.mp3") # Channel 1
		self.getAntimatterSound = pygame.mixer.Sound("sounds/get-antimatter.mp3") # Channel 2
		self.codeSound = pygame.mixer.Sound("sounds/code.mp3") # Channel 2
		self.fuelSound = pygame.mixer.Sound("sounds/fuel.mp3") # Channel 3
		self.explosionSound = pygame.mixer.Sound("sounds/explosion.mp3") # Channel 4
		self.extraLifeSound = pygame.mixer.Sound("sounds/extralife.mp3") # Channel 4
		self.tractorbeamSound = pygame.mixer.Sound("sounds/tractorbeam.mp3") # Channel 5
		self.dropshipSound = pygame.mixer.Sound("sounds/dropship.mp3") # Channel 6
		self.bonusPointsSound = pygame.mixer.Sound("sounds/bonus.mp3") # Channel 6
		self.gameOver = pygame.mixer.Sound("sounds/game-over.mp3") # Channel 7
		self.pointsSound = pygame.mixer.Sound("sounds/points.mp3") # Channel 7
 		
		for music in os.listdir(self.musicPath):
			if not music.startswith('.'):
				self.music.append(f"{self.musicPath}/{music}")
				
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.Sound.set_volume(self.getAntimatterSound, 0.2)
		pygame.mixer.Sound.set_volume(self.bonusPointsSound, 0.2)
		pygame.mixer.Sound.set_volume(self.fuelSound, 0.5)
		pygame.mixer.Sound.set_volume(self.explosionSound, 0.9)
		pygame.mixer.Sound.set_volume(self.pointsSound, 1.0)

		# Lander settings
		self.verticalSpeed = 0
		self.horizontalSpeed = 0
		self.landerLimit = 3
		self.lastX = 0
		self.lastY = 0
		self.currentX = 0
		self.currentY = 0
		self.landerSpeed = 0
		self.landerFuel = 200
		
		# Droship
		self.callDropship = False
		
		# Tractorbeam
		self.defaultTractorBeamTimer = 300
		self.tractorBeamOn = False
		self.tractorBeamTimer = 300
		
		# Level
		self.levelComplete = False
		
		# Antimatter
		self.antimatterScrollSpeed = 2
		self.antimatterTimeStart = 60
		self.defaultAntimatterTimeStart = 60
		
		# FuelCanister
		self.defaultCanisterTimeStart = 250
		self.rotation = 5
		self.canisterTimeStart = 250
		
		# Debris
		self.defaultDebrisTimeStart = 100
		self.debrisTimeStart = self.defaultDebrisTimeStart
		
		# gaySwitch
		self.gaySwitch = 0
		
		# Difficulty scale factor
		self.difficulty = 1.05
		self.scoreScale = 1.5
		self.levelSpeedScale = 0.1
		
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		# Gravity
		self.gravity = 0.1
		
		# Level
		self.levelCompletePoints = 10000
		self.defaultLevelScrollSpeed = 1
	
		# Antimatter
		self.antimatterPoints = 50
		self.bonusPoints = 5000
	
		# Fuel Canister
		self.fuelCanisterScrollSpeed = 2
	
		# Landing pad
		self.landingPadScrollSpeed = 1.5
		self.maxLandingPadPoints = 100000
		self.landingPadPoints = 1000
	
	def increase_difficulty(self):
		self.gravity *= self.difficulty
		self.antimatterScrollSpeed *= self.difficulty
		self.fuelCanisterScrollSpeed *= self.difficulty
		self.landingPadScrollSpeed *= self.difficulty
		self.defaultLevelScrollSpeed -= self.levelSpeedScale
		self.defaultDebrisTimeStart -= 2
		self.antimatterPoints = int(self.antimatterPoints * self.scoreScale)
		self.bonusPoints = int(self.bonusPoints * self.scoreScale)
		self.maxLandingPadPoints = int(self.maxLandingPadPoints * self.scoreScale)
		self.landingPadPoints = int(self.landingPadPoints * self.scoreScale)
		self.levelCompletePoints = int(self.levelCompletePoints * self.scoreScale)
		
	