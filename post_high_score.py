import mysql.connector

class PostHighScore:
	def __init__(self, scoreboard, stats, enterName):
		self.scoreboard = scoreboard
		self.stats = stats
		self.enterName = enterName
		self.getQuery = "SELECT MAX(score) FROM HighScores"
		self.postQuery = "INSERT INTO HighScores (name, score, level) VALUES (%s, %s, %s)"
		self.host = "localhost"
		self.user = "user"
		self.password = "password"
		self.database = "database"
		
	def get_highscore(self):
		self.lunarBase = mysql.connector.connect(
			host = self.host,
			user = self.user,
			password = self.password,
			database = self.database
		)
		
		self.cursor = self.lunarBase.cursor()
		
		self.cursor.execute(self.getQuery)
		highscore = self.cursor.fetchall()
		self.scoreboard.highscore = "{:,}".format(highscore[0][0])
		self.cursor.close()
		self.lunarBase.close()
		
	def post_highscore(self):
		self.lunarBase = mysql.connector.connect(
			host = self.host,
			user = self.user,
			password = self.password,
			database = self.database
		)
		
		self.score = self.stats.score
		self.level = self.stats.currentLevel
		self.cursor = self.lunarBase.cursor()
		self.cursor.execute(self.postQuery, (self.enterName.name, self.score, self.level))
		self.lunarBase.commit()
		self.cursor.close()
		self.lunarBase.close()
