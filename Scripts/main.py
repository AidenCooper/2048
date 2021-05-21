import sys
import pygame

pygame.init()

BACKGROUND = 250, 248, 239
SPEED = [2, 2]
FPS = 30
SIZE = WIDTH, HEIGHT = 480, 668

SCREEN = pygame.display.set_mode(SIZE)

GRID = pygame.image.load("../Images/grid.png")
TITLE = pygame.image.load("../Images/title.png")

SCORE = 0

class Box:
	def __init__(self, number):
		self.number = number

	def getNumber(self):
		return self.number

	def getImage(self):
		return pygame.image.load(f"../Images/{self.number}.png")

	def duplicate(self):
		self.number *= 2

class Board:
	def getPosition(number):
		if number == 1:
			return [13, 201]
		elif number == 2:
			return [130, 201]
		elif number == 3:
			return [247, 201]
		elif number == 4:
			return [364, 201]
		elif number == 5:
			return [13, 318]
		elif number == 6:
			return [130, 318]
		elif number == 7:
			return [247, 318]
		elif number == 8:
			return [364, 318]
		elif number == 9:
			return [13, 435]
		elif number == 10:
			return [130, 435]
		elif number == 11:
			return [247, 435]
		elif number == 12:
			return [364, 435]
		elif number == 13:
			return [13, 552]
		elif number == 14:
			return [130, 552]
		elif number == 15:
			return [247, 552]
		else:
			return [364, 552]
	
	storage = []

box = Box(2)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			box.duplicate()

	SCREEN.fill(BACKGROUND)


	SCREEN.blit(GRID, [0, SCREEN.get_height() - GRID.get_height()])
	SCREEN.blit(TITLE, [(SCREEN.get_width() / 2) - (TITLE.get_width() / 2), (SCREEN.get_height() - GRID.get_height()) - (TITLE.get_height() + (TITLE.get_height() / 2))])

	SCREEN.blit(box.getImage(), [13, 201])
	pygame.display.flip()


# C:\%HOMEPATH%\Desktop\Python\2048\Scripts
# C:\Users\s12710216\AppData\Local\Git\bin\git.exe

# 1 = 13, 201
# 2 = 130, 201
# 3 = 247, 201
# 4 = 364, 201
# 5 = 13, 318
# 6 = 130, 318
# 7 = 247, 318
# 8 = 364, 318
# 9 = 13, 435
# 10 = 130, 435
# 11 = 247, 435
# 12 = 364, 435
# 13 = 13, 552
# 14 = 130, 552
# 15 = 247, 552
# 16 = 364, 552