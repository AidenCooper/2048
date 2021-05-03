import random

class Box:
	def __init__(self, number, position):
		self.number = number
		self.position = position

class Board:
	def __init__(self):
		self.boxList = [Box(-1, 0), Box(-1, 1), Box(-1, 2), Box(-1, 3),
					    Box(-1, 4), Box(-1, 5), Box(-1, 6), Box(-1, 7),
					    Box(-1, 8), Box(-1, 9), Box(-1, 10), Box(-1, 11),
					    Box(-1, 12), Box(-1, 13), Box(-1, 14), Box(-1, 15)]

	def getEmptyPositions(self):
		positions = []

		for box in self.boxList:
			if box.number == -1:
				positions.append(box.position)
		return positions

	def createRandom(self):
		positionsAvailable = self.getEmptyPositions()
		position = positionsAvailable[random.randint(0, len(positionsAvailable) - 1)]

def main():
	board = Board()
	board.createRandom()

main()