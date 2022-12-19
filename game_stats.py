class GameStats():
	def __init__(self, ll_Settings):
		self.ll_Settings = ll_Settings
		self.reset_stats()
		self.gameActive = False
		self.callDropship = False
		
		self.score = 0
		self.antimatter = 0
		self.bonus = 5
		self.currentLevel = 1
		self.landingPadPoints = 0
		self.smallLandingPadPoints = 0
		self.landersLeft = self.ll_Settings.landerLimit
		self.getLife = 1000000
		
	def reset_stats(self):
		self.landersLeft = self.ll_Settings.landerLimit
		self.score = 0
		self.antimatter = 0
		self.landingPadPoints = 0
		self.currentLevel = 1