import sys
import pygame
import random
import copy
import numpy

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
		if self.number == 0:
			self.number = 2
		else:
			self.number *= 2

class Board:
	def __init__(self):
		self.storage = [Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0), Box(0)]
		
		self.addRandomBox()
		self.addRandomBox()

	def getRandomPosition(self):
		emptyPositions = []

		for index in range(16):
			if self.storage[index].number == 0:
				emptyPositions.append(index + 1)

		if len(emptyPositions) == 0:
			return -1
		else:
			return emptyPositions[random.randrange(0, len(emptyPositions))]

	def addRandomBox(self):
		position = self.getRandomPosition()
		number = 0

		if random.randrange(1, 101) <= 90:
			number = 2
		else:
			number = 4

		self.storage[position - 1] = Box(number)

	def getPosition(self, number):
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

	def moveUp(self):
		storage = copy.deepcopy(self.storage)

		row1 = [storage[0], storage[4], storage[8], storage[12]]
		row2 = [storage[1], storage[5], storage[9], storage[13]]
		row3 = [storage[2], storage[6], storage[10], storage[14]]
		row4 = [storage[3], storage[7], storage[11], storage[15]]

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		row1 = self.combine(row1)
		row2 = self.combine(row2)
		row3 = self.combine(row3)
		row4 = self.combine(row4)

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		storage[0] = row1[0]
		storage[4] = row1[1]
		storage[8] = row1[2]
		storage[12] = row1[3]
		storage[1] = row2[0]
		storage[5] = row2[1]
		storage[9] = row2[2]
		storage[13] = row2[3]
		storage[2] = row3[0]
		storage[6] = row3[1]
		storage[10] = row3[2]
		storage[14] = row3[3]
		storage[3] = row4[0]
		storage[7] = row4[1]
		storage[11] = row4[2]
		storage[15] = row4[3]

		
		for index in range(16):
			if storage[index].number != self.storage[index].number:
				self.storage = storage
				return True
		return False

	def moveDown(self):
		storage = copy.deepcopy(self.storage)

		row1 = [storage[12], storage[8], storage[4], storage[0]]
		row2 = [storage[13], storage[9], storage[5], storage[1]]
		row3 = [storage[14], storage[10], storage[6], storage[2]]
		row4 = [storage[15], storage[11], storage[7], storage[3]]

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		row1 = self.combine(row1)
		row2 = self.combine(row2)
		row3 = self.combine(row3)
		row4 = self.combine(row4)

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		storage[12] = row1[0]
		storage[8] = row1[1]
		storage[4] = row1[2]
		storage[0] = row1[3]
		storage[13] = row2[0]
		storage[9] = row2[1]
		storage[5] = row2[2]
		storage[1] = row2[3]
		storage[14] = row3[0]
		storage[10] = row3[1]
		storage[6] = row3[2]
		storage[2] = row3[3]
		storage[15] = row4[0]
		storage[11] = row4[1]
		storage[7] = row4[2]
		storage[3] = row4[3]

		for index in range(16):
			if storage[index].number != self.storage[index].number:
				self.storage = storage
				return True
		return False

	def moveLeft(self):
		storage = copy.deepcopy(self.storage)

		row1 = [storage[0], storage[1], storage[2], storage[3]]
		row2 = [storage[4], storage[5], storage[6], storage[7]]
		row3 = [storage[8], storage[9], storage[10], storage[11]]
		row4 = [storage[12], storage[13], storage[14], storage[15]]

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		row1 = self.combine(row1)
		row2 = self.combine(row2)
		row3 = self.combine(row3)
		row4 = self.combine(row4)

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		storage[0] = row1[0]
		storage[1] = row1[1]
		storage[2] = row1[2]
		storage[3] = row1[3]
		storage[4] = row2[0]
		storage[5] = row2[1]
		storage[6] = row2[2]
		storage[7] = row2[3]
		storage[8] = row3[0]
		storage[9] = row3[1]
		storage[10] = row3[2]
		storage[11] = row3[3]
		storage[12] = row4[0]
		storage[13] = row4[1]
		storage[14] = row4[2]
		storage[15] = row4[3]

		for index in range(16):
			if storage[index].number != self.storage[index].number:
				self.storage = storage
				return True
		return False

	def moveRight(self):
		storage = copy.deepcopy(self.storage)

		row1 = [storage[3], storage[2], storage[1], storage[0]]
		row2 = [storage[7], storage[6], storage[5], storage[4]]
		row3 = [storage[11], storage[10], storage[9], storage[8]]
		row4 = [storage[15], storage[14], storage[13], storage[12]]

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		row1 = self.combine(row1)
		row2 = self.combine(row2)
		row3 = self.combine(row3)
		row4 = self.combine(row4)

		row1 = self.slide(row1)
		row2 = self.slide(row2)
		row3 = self.slide(row3)
		row4 = self.slide(row4)

		storage[3] = row1[0]
		storage[2] = row1[1]
		storage[1] = row1[2]
		storage[0] = row1[3]
		storage[7] = row2[0]
		storage[6] = row2[1]
		storage[5] = row2[2]
		storage[4] = row2[3]
		storage[11] = row3[0]
		storage[10] = row3[1]
		storage[9] = row3[2]
		storage[8] = row3[3]
		storage[15] = row4[0]
		storage[14] = row4[1]
		storage[13] = row4[2]
		storage[12] = row4[3]

		for index in range(16):
			if storage[index].number != self.storage[index].number:
				self.storage = storage
				return True
		return False

	def slide(self, row):
		for i in range(1, 4):
			for j in reversed(range(0, i)):
				if row[j].number == 0:
					row[j].number = row[j + 1].number
					row[j + 1].number = 0
				else:
					break
		return row

	def combine(self, row):
		for i in range(0, 3):
			if row[i].number == row[i + 1].number:
				row[i].number *= 2
				row[i + 1].number = 0
		return row

	def canMove(self):
		return True

board = Board()

while True:
	for box in board.storage:
		if box.number == 2048:
			sys.exit()

	if board.canMove() == False:
		sys.exit()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				if board.moveUp():
					board.addRandomBox()
					
					print(f"{board.storage[0].number} {board.storage[1].number} {board.storage[2].number} {board.storage[3].number}")
					print(f"{board.storage[4].number} {board.storage[5].number} {board.storage[6].number} {board.storage[7].number}")
					print(f"{board.storage[8].number} {board.storage[9].number} {board.storage[10].number} {board.storage[11].number}")
					print(f"{board.storage[12].number} {board.storage[13].number} {board.storage[14].number} {board.storage[15].number}")

					print(" ")
			elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
				if board.moveDown():
					board.addRandomBox()
					
					print(f"{board.storage[0].number} {board.storage[1].number} {board.storage[2].number} {board.storage[3].number}")
					print(f"{board.storage[4].number} {board.storage[5].number} {board.storage[6].number} {board.storage[7].number}")
					print(f"{board.storage[8].number} {board.storage[9].number} {board.storage[10].number} {board.storage[11].number}")
					print(f"{board.storage[12].number} {board.storage[13].number} {board.storage[14].number} {board.storage[15].number}")

					print(" ")
			elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
				if board.moveLeft():
					board.addRandomBox()
					
					print(f"{board.storage[0].number} {board.storage[1].number} {board.storage[2].number} {board.storage[3].number}")
					print(f"{board.storage[4].number} {board.storage[5].number} {board.storage[6].number} {board.storage[7].number}")
					print(f"{board.storage[8].number} {board.storage[9].number} {board.storage[10].number} {board.storage[11].number}")
					print(f"{board.storage[12].number} {board.storage[13].number} {board.storage[14].number} {board.storage[15].number}")

					print(" ")
			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				if board.moveRight():
					board.addRandomBox()
					
					print(f"{board.storage[0].number} {board.storage[1].number} {board.storage[2].number} {board.storage[3].number}")
					print(f"{board.storage[4].number} {board.storage[5].number} {board.storage[6].number} {board.storage[7].number}")
					print(f"{board.storage[8].number} {board.storage[9].number} {board.storage[10].number} {board.storage[11].number}")
					print(f"{board.storage[12].number} {board.storage[13].number} {board.storage[14].number} {board.storage[15].number}")

					print(" ")

	SCREEN.fill(BACKGROUND)


	SCREEN.blit(GRID, [0, SCREEN.get_height() - GRID.get_height()])
	SCREEN.blit(TITLE, [(SCREEN.get_width() / 2) - (TITLE.get_width() / 2), (SCREEN.get_height() - GRID.get_height()) - (TITLE.get_height() + (TITLE.get_height() / 2))])

	for index in range(16):
		SCREEN.blit(board.storage[index].getImage(), board.getPosition(index + 1))

	pygame.display.flip()

# C:\%HOMEPATH%\Desktop\Python\2048\Scripts
# C:\Users\s12710216\AppData\Local\Git\bin\git.exe