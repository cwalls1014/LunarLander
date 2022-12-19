import sys
import pygame
from fuel_canister import FuelCanister
from debris import Debris
from antimatter import Antimatter
import math
import random
import webbrowser

def check_credits_button(title, creditsButton, credits, mouseX, mouseY):
	creditsClicked = creditsButton.rect.collidepoint(mouseX, mouseY)
	if creditsClicked and title.viewed:
		credits.viewed = True
		title.viewed = False
		
def check_link(enterName, mouseX, mouseY):
	linkClicked = enterName.linkRect.collidepoint(mouseX, mouseY)
	if linkClicked and enterName.viewed:
		enterName.linkColor = (70, 29, 219)
		webbrowser.open(r"https://thingsnstuff.in/lunar_lander")

def check_ok_button(title, okButton, mouseX, mouseY, howToPlay, credits):
	okClicked = okButton.rect.collidepoint(mouseX, mouseY)
	if okClicked and howToPlay.viewed:
		howToPlay.viewed = False
		title.viewed = True
	elif okClicked and credits.viewed:
		credits.viewed = False
		title.viewed = True

def check_how_button(title, howButton, mouseX, mouseY, howToPlay):
	howClicked = howButton.rect.collidepoint(mouseX, mouseY)
	if howClicked and title.viewed:
		howToPlay.viewed = True
		title.viewed = False

def check_quit_button(title, quitButton, mouseX, mouseY):
	quitClicked = quitButton.rect.collidepoint(mouseX, mouseY)
	if quitClicked and title.viewed:
		sys.exit()

def check_start_button(stats, event, playButton, mouseX, mouseY, fuelCanisters, fuel, lander, landingPad, ll_Settings, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton):
	startClicked = startButton.rect.collidepoint(mouseX, mouseY)
	if startClicked and title.viewed:
		title.viewed = False
		pygame.mouse.set_visible(False)
		stats.gameActive = True
		stats.reset_stats()
		highScore.get_highscore()
		scoreboard.prep_score()
		scoreboard.prep_level()
		scoreboard.prep_high_score()
		scoreboard.prep_landers()
		enterName.text = ''
		fuelCanisters.empty()
		antiM.empty()
		fuel.reset_fuel()
		lander.reset_lander()
		dropship.reset_dropship()
		landingPad.reset_landingPad()
		debris.empty()
		ll_Settings.initialize_dynamic_settings()
		level.set_level()
		pygame.mixer.music.load(random.choice(ll_Settings.music))
		pygame.mixer.music.play(-1)
	else:
		pass

def check_play_button(stats, event, playButton, mouseX, mouseY, enterName, title, startButton, howToPlay, credits):
	buttonClicked = playButton.rect.collidepoint(mouseX, mouseY)
	if title.viewed:
		pass
	elif howToPlay.viewed:
		pass
	elif enterName.viewed:
		pass
	elif credits.viewed:
		pass
	elif buttonClicked and not stats.gameActive:
		pygame.mouse.set_visible(False)
		stats.gameActive = True
		pygame.mixer.music.unpause()

def check_switch(ll_Settings, lander):
	if ll_Settings.gaySwitch == 0:
		# Calculate lander speed
		ll_Settings.lastX = lander.rect.centerx
		ll_Settings.lastY = lander.rect.centery
		
		# SWITCH
		ll_Settings.gaySwitch = 1
	else:
		# Calculate lander speed
		ll_Settings.currentX = lander.rect.centerx
		ll_Settings.currentY = lander.rect.centery
		
		# SWITCH
		ll_Settings.gaySwitch = 0
		
	# Calculate lander speed
	speed = ll_Settings.currentX - ll_Settings.lastX
	
	if speed < 0:
		speed *= -1

	dx = ll_Settings.lastX - ll_Settings.currentX
	dy = ll_Settings.lastY - ll_Settings.currentY
	ll_Settings.landerSpeed = math.sqrt(dx * dx + dy * dy)
    
def lander_go_boom(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, scoreboard, enterName):
	if stats.landersLeft > 0:
		stats.landersLeft -= 1
		scoreboard.prep_landers()
		fuelCanisters.empty()
		debris.empty()
		antiM.empty()
		fuel.reset_fuel()
		lander.reset_lander()
		landingPad.reset_landingPad()
		dropship.reset_dropship()
		level.reset_level()
		stats.antimatter = 0
		scoreboard.prep_antimatter()
		ll_Settings.tractorBeamOn = False
		ll_Settings.canisterTimeStart = ll_Settings.defaultCanisterTimeStart
		ll_Settings.debrisTimeStart = ll_Settings.defaultDebrisTimeStart
		ll_Settings.antimatterTimeStart = ll_Settings.defaultAntimatterTimeStart
	else:
		pygame.mouse.set_visible(True)
		stats.gameActive = False
		pygame.mixer.music.stop()
		ll_Settings.ch7.play(ll_Settings.gameOver)
		enterName.viewed = True
		
def start_new_level(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, tractorBeam, scoreboard):
	stats.landingPadPoints = 0
	stats.score += ll_Settings.levelCompletePoints
	scoreboard.prep_score()
	ll_Settings.increase_difficulty()
	level.set_level()
	stats.currentLevel += 1
	scoreboard.prep_level()
	fuelCanisters.empty()
	debris.empty()
	antiM.empty()
	fuel.reset_fuel()
	lander.reset_lander()
	landingPad.reset_landingPad()
	dropship.reset_dropship()
	stats.antimatter = 0
	scoreboard.prep_antimatter()
	ll_Settings.canisterTimeStart = ll_Settings.defaultCanisterTimeStart
	ll_Settings.debrisTimeStart = ll_Settings.defaultDebrisTimeStart
	ll_Settings.antimatterTimeStart = ll_Settings.defaultAntimatterTimeStart
	pygame.mixer.music.load(random.choice(ll_Settings.music))
	pygame.mixer.music.play(-1)
	
def check_bonus_points(stats, scoreboard, ll_Settings):
	if stats.antimatter == stats.bonus:
		stats.score += ll_Settings.bonusPoints
		scoreboard.prep_score()
		stats.antimatter = 0
		scoreboard.prep_antimatter()
		ll_Settings.ch6.play(ll_Settings.bonusPointsSound)

def check_lives(stats, scoreboard, ll_Settings):
	if math.floor(stats.score / stats.getLife) == 1:
		stats.landersLeft += 1
		scoreboard.prep_landers()
		ll_Settings.ch4.play(ll_Settings.extraLifeSound)
		stats.getLife *= 2

def check_evac(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, tractorBeam, scoreboard, enterName):
	
	lander.evac(dropship, tractorBeam)
	
	if dropship.rect.left >= dropship.screenRect.right:
		if ll_Settings.tractorBeamTimer == 0 and not dropship.evac:
			stats.landersLeft = 0
			lander_go_boom(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, scoreboard, enterName)
		elif ll_Settings.tractorBeamTimer == 0 and dropship.evac:
			start_new_level(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, tractorBeam, scoreboard)
		
def check_lander_crash(ll_Settings, lander, explosion, landingPad, stats, scoreboard):
	
	if lander.rect.bottom >= lander.screenRect.bottom - 50.0:
		if not explosion.timer:
			ll_Settings.ch4.play(ll_Settings.explosionSound)
		explosion.exploded = True
		explosion.timer = True
		ll_Settings.verticalSpeed = 0.0
	if landingPad.rect.contains(lander):
		if ll_Settings.landerSpeed > 4:
			if not explosion.timer:
				ll_Settings.pointsSound.stop()
				ll_Settings.ch4.play(ll_Settings.explosionSound)
			explosion.exploded = True
			explosion.timer = True
			ll_Settings.verticalSpeed = 0.0
		else:
			stats.antimatter = 0
			scoreboard.prep_antimatter()
			ll_Settings.verticalSpeed = -(ll_Settings.gravity)
			ll_Settings.horizontalSpeed = 0.0
			ll_Settings.horizontalSpeed -= ll_Settings.landingPadScrollSpeed
			if not explosion.exploded:
				if stats.landingPadPoints < ll_Settings.maxLandingPadPoints:
					stats.score += ll_Settings.landingPadPoints
					stats.landingPadPoints += ll_Settings.landingPadPoints
					ll_Settings.pointsSound.play()
					if stats.landingPadPoints == ll_Settings.maxLandingPadPoints:
						ll_Settings.pointsSound.stop()
					scoreboard.prep_score()
	else:
		ll_Settings.pointsSound.stop()
	if lander.rect.right <= lander.screenRect.left:
		if not explosion.timer:
			ll_Settings.ch4.play(ll_Settings.explosionSound)
			explosion.exploded = True
			explosion.timer = True
			ll_Settings.verticalSpeed = 0.0
			
def start_timer(ll_Settings):
	ll_Settings.canisterTimeStart -= 1
	ll_Settings.debrisTimeStart -= 1
	ll_Settings.antimatterTimeStart -= 1
	
def update_antimatter(ll_Settings, screen, lander, antiM, stats, scoreboard):
	antiM.update()
	collected = False
	
	for matter in antiM.copy():
		for r in matter.rects:
			if r.right <= 0 or r.left >= 1024:
				matter.remove(antiM)
			if r.colliderect(lander):
				ll_Settings.ch2.play(ll_Settings.getAntimatterSound)
				matter.remove(antiM)
				collected = True	
	
	if collected:
		stats.score += ll_Settings.antimatterPoints
		scoreboard.prep_score()
		stats.antimatter += 1
		scoreboard.prep_antimatter()
		collected = False
	
def generate_antimatter(ll_Settings, screen, antiM):
	if ll_Settings.antimatterTimeStart == 0:
		newAntimatter = Antimatter(ll_Settings, screen, antiM)
		antiM.add(newAntimatter)
		ll_Settings.antimatterTimeStart = 60
	
def update_debris(debris, lander, ll_Settings, explosion):
	debris.update()
	
	for deb in debris.copy():
		if deb.currentImage[1].right <= 0 or deb.currentImage[1].top >= 768 or deb.currentImage[1].left >= 1024:
			debris.remove(deb)
		if not lander.docked and not lander.invincible:
			if deb.currentImage[1].colliderect(lander):
				if not explosion.timer:
					ll_Settings.ch4.play(ll_Settings.explosionSound)
				debris.remove(debris)
				explosion.exploded = True
				explosion.timer = True
				ll_Settings.verticalSpeed = 0.0
	
def generate_debris(ll_Settings, screen, lander, debris):
	if ll_Settings.debrisTimeStart <= 0:
		newDebris = Debris(ll_Settings, screen, debris, lander)
		debris.add(newDebris)
		ll_Settings.debrisTimeStart = 100
	
def update_canisters(fuelCanisters, lander, fuel, ll_Settings, stats, scoreboard):
	fuelCanisters.update()
	
	for canister in fuelCanisters.copy():
		if canister.rect.right <= 0:
			fuelCanisters.remove(canister)
		if canister.rect.colliderect(lander):
			stats.antimatter = 0
			scoreboard.prep_antimatter()
			fuelCanisters.remove(canister)
			fuel.reset_fuel()
			ll_Settings.ch3.play(ll_Settings.fuelSound)
	
def generate_canister(ll_Settings, screen, fuelCanisters):
	if ll_Settings.canisterTimeStart <= 0:
		newFuelCanister = FuelCanister(ll_Settings, screen, fuelCanisters)
		fuelCanisters.add(newFuelCanister)
		ll_Settings.canisterTimeStart = ll_Settings.defaultCanisterTimeStart

def check_keydown_events(event, lander, flames, ll_Settings, stats, enterName, highScore, title, howToPlay):
	"""Resond to key presses"""
	if enterName.viewed:
		if event.key == pygame.K_BACKSPACE:
			enterName.name = enterName.name[:-1]
		elif event.key == pygame.K_RETURN:
			highScore.post_highscore()
			enterName.viewed = False
			title.viewed = True
		else:
			enterName.name += event.unicode
	else:
		if event.key == pygame.K_d:
			lander.movingRight = True
		elif event.key == pygame.K_a:
			lander.movingLeft = True
		elif event.key == pygame.K_w:
			if ll_Settings.landerFuel > 0 and stats.gameActive and not lander.docked:
				ll_Settings.ch1.play(ll_Settings.rocketSound)
				lander.movingUp = True
				flames.engaged = True
			if ll_Settings.landerFuel <= 0:
				ll_Settings.ch1.stop()
		elif event.key == pygame.K_ESCAPE:
			lander.checkLLinv.clear()
			lander.checkLLful.clear()
			if stats.gameActive:
				pygame.mixer.music.pause()
				stats.gameActive = False
				pygame.mouse.set_visible(True)
			else:
				pygame.mixer.music.unpause()
				stats.gameActive = True
				pygame.mouse.set_visible(False)
	
	if not stats.gameActive and not enterName.viewed and not title.viewed and not howToPlay.viewed and event.key is not pygame.K_ESCAPE:
		lander.checkLLinv.append(event.key)
		lander.checkLLful.append(event.key)
	
	if lander.checkLLinv == lander.invincibleCode:
		if lander.invincible:
			lander.invincible = False
			ll_Settings.ch2.play(ll_Settings.codeSound)
			lander.checkLLinv.clear()
		else:
			lander.invincible = True
			ll_Settings.ch2.play(ll_Settings.codeSound)
			lander.checkLLinv.clear()
	elif lander.checkLLful == lander.unlimitedFuelCode:
		if lander.unlimitedFuel:
			lander.unlimitedFuel = False
			ll_Settings.ch2.play(ll_Settings.codeSound)
			lander.checkLLful.clear()
		else:
			lander.unlimitedFuel = True
			ll_Settings.ch2.play(ll_Settings.codeSound)
			lander.checkLLful.clear()

def check_keyup_events(event, lander, flames, ll_Settings):
	"""Respond to key releases"""
	if event.key == pygame.K_d:
		lander.movingRight = False
	elif event.key == pygame.K_a:
		lander.movingLeft = False
	elif event.key == pygame.K_w:
		ll_Settings.ch1.stop()
		lander.movingUp = False
		flames.engaged = False
		
def check_mousedown_events(stats, event, playButton, fuelCanisters, fuel, lander, landingPad, ll_Settings, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton, quitButton, howButton, howToPlay, okButton, credits, creditsButton):
	mouseX, mouseY = pygame.mouse.get_pos()
	
	check_start_button(stats, event, playButton, mouseX, mouseY, fuelCanisters, fuel, lander, landingPad, ll_Settings, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton)
	
	check_play_button(stats, event, playButton, mouseX, mouseY, enterName, title, startButton, howToPlay, credits)
	
	check_quit_button(title, quitButton, mouseX, mouseY)
	
	check_how_button(title, howButton, mouseX, mouseY, howToPlay)
	
	check_ok_button(title, okButton, mouseX, mouseY, howToPlay, credits)
	
	check_link(enterName, mouseX, mouseY)
	
	check_credits_button(title, creditsButton, credits, mouseX, mouseY)
	
def check_events(lander, flames, fuel, ll_Settings, playButton, stats, fuelCanisters, landingPad, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton, quitButton, howButton, howToPlay, okButton, credits, creditsButton):
	"""Respond to keypresses and mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, lander, flames, ll_Settings, stats, enterName, highScore, title, howToPlay)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, lander, flames, ll_Settings)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			check_mousedown_events(stats, event, playButton, fuelCanisters, fuel, lander, landingPad, ll_Settings, level, debris, dropship, antiM, scoreboard, enterName, highScore, title, startButton, quitButton, howButton, howToPlay, okButton, credits, creditsButton)
				
def update_screen(ll_Settings, screen, level, lander, flames, fuel, fuelCanisters, landingPad, explosion, stats, playButton, debris, dropship, antiM, tractorBeam, scoreboard, enterName, title, startButton, howButton, quitButton, howToPlay, okButton, credits, creditsButton):
	"""Update images on the screen and flip the new screen"""
	screen.fill(ll_Settings.bgColor)
	
	if not stats.gameActive:
		if title.viewed:
			title.blitme()
			startButton.blitme()
			howButton.blitme()
			creditsButton.blitme()
			quitButton.blitme()
		elif enterName.viewed:
			enterName.blitme()
		elif howToPlay.viewed:
			howToPlay.blitme()
			okButton.blitme()
		elif credits.viewed:
			credits.blitme()
			okButton.blitme()
		else:
			playButton.blitme()
	else:
		level.blitme()
		fuel.blitme()
		landingPad.blitme()
	
		if not lander.docked:
			if not explosion.exploded:
				lander.blitme()
		
		if ll_Settings.tractorBeamOn:
			tractorBeam.blitme()
	
		if dropship.rect.left < dropship.screenRect.right:
			dropship.blitme()
	
		if explosion.exploded == True:
			explosion.blitme()
			lander.movingUp = False
			flames.engaged = False
			if explosion.targetFrame == 14:
				lander_go_boom(ll_Settings, stats, lander, fuelCanisters, fuel, explosion, debris, landingPad, level, dropship, antiM, scoreboard, enterName)
				explosion.exploded = False
				explosion.timer = False
				explosion.animationFrame = 0
			
		for matter in antiM.sprites():
			matter.blitme()
			
		for deb in debris.sprites():
			deb.blitme()
			
		for canister in fuelCanisters.sprites():
			canister.blitme()
	
		if flames.engaged and ll_Settings.landerFuel > 0:
			flames.blitme()
	
		scoreboard.show_score()
	
	# Make the most recently drawn screen visible
	pygame.display.flip()