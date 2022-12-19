import pygame
from settings import Settings
from level import Level
from lander import Lander
from flames import Flames
from fuel import Fuel
from landing_pad import LandingPad
from explosion import Explosion
from game_stats import GameStats
from how_button import HowButton
from play_button import PlayButton
from quit_button import QuitButton
from credits_button import CreditsButton
from dropship import Dropship
from tractor_beam import TractorBeam
from scoreboard import Scoreboard
from post_high_score import PostHighScore
from enter_name import EnterName
from title import Title
from start_button import StartButton
from ok_button import OKButton
from how_to_play import HowToPlay
from credits import Credits
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# Initialize pygame, settings, and screen object
	pygame.mixer.pre_init(44100, -16, 2, 512)
	pygame.init()
	pygame.mixer.init()
	ll_Settings = Settings()
	screen = pygame.display.set_mode((ll_Settings.screenWidth, ll_Settings.screenHeight))
	pygame.display.set_caption("Lunar Lander")
	clock = pygame.time.Clock()
	fps = 30
	antiM = Group()
	lander = Lander(ll_Settings, screen)
	flames = Flames(ll_Settings, screen, lander)
	stats = GameStats(ll_Settings)
	scoreboard = Scoreboard(ll_Settings, screen, stats)
	title = Title(screen)
	enterName = EnterName(screen)
	credits = Credits(screen)
	highScore = PostHighScore(scoreboard, stats, enterName)
	level = Level(ll_Settings, screen)
	fuel = Fuel(ll_Settings, screen, lander, stats)
	landingPad = LandingPad(ll_Settings, screen)
	howToPlay = HowToPlay(screen)
	playButton = PlayButton(ll_Settings, screen)
	quitButton = QuitButton(screen)
	creditsButton = CreditsButton(screen)
	okButton = OKButton(screen)
	howButton = HowButton(screen)
	startButton = StartButton(ll_Settings, screen)
	explosion = Explosion(screen, lander, ll_Settings)
	debris = Group()
	fuelCanisters = Group()
	dropship = Dropship(screen, lander, stats, ll_Settings)
	tractorBeam = TractorBeam(screen, ll_Settings, lander)
	# Start the main loop for the game
	while True:
		clock.tick(fps)
		# Watch for keyboard and mouse events
		gf.check_events(lander, flames, fuel, ll_Settings, playButton, stats, fuelCanisters, landingPad, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton, quitButton, howButton, howToPlay, okButton, credits, creditsButton)
		
		if enterName.viewed:
			enterName.update()
		if credits.viewed:
			credits.update()
		elif stats.gameActive:
			level.update()
			landingPad.update()
			if ll_Settings.callDropship:
				dropship.call_dropship()
				gf.check_evac(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, tractorBeam, scoreboard, enterName)
			else:
				dropship.update()
			if not lander.docked:
				lander.update()
			flames.update()
			tractorBeam.update()
			if not lander.unlimitedFuel:
				fuel.update()
			explosion.update()
			gf.check_switch(ll_Settings, lander)
			gf.start_timer(ll_Settings)
			gf.generate_antimatter(ll_Settings, screen, antiM)
			gf.update_antimatter(ll_Settings, screen, lander, antiM, stats, scoreboard)
			gf.generate_debris(ll_Settings, screen, lander, debris)
			gf.update_debris(debris, lander, ll_Settings, explosion)
			gf.generate_canister(ll_Settings, screen, fuelCanisters)
			gf.update_canisters(fuelCanisters, lander, fuel, ll_Settings, stats, scoreboard)
			if not lander.invincible:
				gf.check_lander_crash(ll_Settings, lander, explosion, landingPad, stats, scoreboard)
			gf.check_lives(stats, scoreboard, ll_Settings)
			gf.check_bonus_points(stats, scoreboard, ll_Settings)
			
		gf.update_screen(ll_Settings, screen, level, lander, flames, fuel, fuelCanisters, landingPad, explosion, stats, playButton, debris, dropship, antiM, tractorBeam, scoreboard, enterName, title, startButton, howButton, quitButton, howToPlay, okButton, credits, creditsButton)
		
run_game()
