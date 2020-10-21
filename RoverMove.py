import pygame

pygame.init()


display_width = 800
display_height = 800

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)
bright_red = (255,0,0)
bright_green = (0,255,0)
bright_blue = (0,0,255)
cyan = (0,255,255)
someColor = (128,128,128)

rockX1 = 300
rockY1 = 300
rockX2 = 400
rockY2 = 500

roverX = 375
roverY = 750
origRoverX = 375

currRockX = 0
currRockY = 0

rockList = []


goal = pygame.image.load('Goal.png')
rover = pygame.image.load('Rover.png')
rock = pygame.image.load('Rock.png')

#gameDisplay.blit(img,(x,y))

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Rover Movement')
clock = pygame.time.Clock()

def initRocks():
	rock1 = Rock()
	rock2 = Rock()

	rock1.x = 300
	rock1.y = 300
	rock2.x = 400 
	rock2.y = 500 

	rockList.append(rock1) 
	rockList.append(rock2)


class Rock:
	x = 0
	y = 0
	

class Rover:
	x = 375
	y = 750

def align(dir, rover, amt):
	roverSpeed = 5
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()

		if(dir == "L"):
			rover.x += roverSpeed
		elif(dir == "R"):
			rover.x -= roverSpeed


		amt -= roverSpeed
		#print(rover.y)
		#collisionCheck(rover)

		if((amt <= 0)):
			run = False
			
		fillBackground()
		roverBox = (rover.x,rover.y,50,50)
		pygame.draw.rect(gameDisplay, bright_red, roverBox)
		pygame.display.update()
		clock.tick(15)


def moveRight(rover):
	displacement = 0
	roverSpeed = 5
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()


		rover.x += roverSpeed
		displacement += roverSpeed
		#print(rover.y)
		#collisionCheck(rover)

		if((rover.x) > (currRockX+110)):
			run = False
			
		fillBackground()
		roverBox = (rover.x,rover.y,50,50)
		pygame.draw.rect(gameDisplay, bright_red, roverBox)
		pygame.display.update()
		clock.tick(15)
	continueForward(rover)
	align("R", rover, displacement)

def moveLeft(rover):
	displacement = 0
	roverSpeed = 5
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()


		rover.x -= roverSpeed
		displacement += roverSpeed
		#print(rover.y)
		#collisionCheck(rover)

		if((rover.x+50) < (currRockX-10)):
			run = False
			
		fillBackground()
		roverBox = (rover.x,rover.y,50,50)
		pygame.draw.rect(gameDisplay, bright_red, roverBox)
		pygame.display.update()
		clock.tick(15)
	continueForward(rover)
	align("L", rover, displacement)

def continueForward(rover):
	roverSpeed = 5
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()


		rover.y -= roverSpeed
		#print(rover.y)

		if(obstacleCleared(rover)):
			run = False
			
		fillBackground()
		roverBox = (rover.x,rover.y,50,50)
		pygame.draw.rect(gameDisplay, bright_red, roverBox)
		pygame.display.update()
		clock.tick(15)

def whichSideCloser(rover):

	if(rover.x < currRockX):
		return "L"
	else:
		return "R"

def collisionCheck(rover):
	if(willColide(rover)):
		if(whichSideCloser(rover) == "L"):
			moveLeft(rover)

		else:
			moveRight(rover)

def willColide(rover):
	#numOfRocks = rockList.size()
	for rock in rockList:
		if((rover.y -10 < rock.y + 100) and (rover.y > rock.y)):
			global currRockY 
			currRockY = rock.y
			global currRockX 
			currRockX = rock.x
			return True

	return False

def obstacleCleared(rover):
	if((rover.y + 50) < (currRockY - 10)):
		return True
	else:
		return False

def moveForward(rover):
	roverSpeed = 5
	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()


		rover.y -= roverSpeed
		#print(rover.y)
		collisionCheck(rover)

		if(rover.y < 25):
			run = False
			
		fillBackground()
		roverBox = (rover.x,rover.y,50,50)
		pygame.draw.rect(gameDisplay, bright_red, roverBox)
		pygame.display.update()
		clock.tick(15)

#creat bubble around rover 
# check for collisions on all sides
#move accordingly
def fillBackground():
	gameDisplay.fill(white)
	gameDisplay.blit(goal,(200,0))
	fillRocks()

def fillRocks():
	rect1 = (rockX1,rockY1,100,100)
	rect2 = (rockX2,rockY2,100,100)
	pygame.draw.rect(gameDisplay, someColor, rect1)
	pygame.draw.rect(gameDisplay, someColor, rect2)
	#gameDisplay.blit(rock,(rockX1,rockY1))
	#gameDisplay.blit(rock,(rockX2,rockY2))

def quitGame():
	pygame.quit()
	exit()

def main():
	roverX = 375
	roverY = 750
	
	rightOffset = 0
	leftOffset = 0 
	inFront = True
	align = True

	rover = Rover()
	initRocks()

	sim = True
	while sim:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()

		if(rover.y > 25):
			moveForward(rover)
	

def menu_screen():
	run = True
	#gameDisplay.fill(someColor)

	while run:
		clock.tick(60)
		gameDisplay.fill(white)
		font = pygame.font.SysFont("comicsans", 60)
		text = font.render("Run Simulation", 1, black)
		gameDisplay.blit(text, (100,200))
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				quitGame()

			if event.type == pygame.MOUSEBUTTONDOWN:
				run = False
				print("here")

	main()




menu_screen()




