import random

class Box:
	def __init__(self, number, position):
		self.number = number
		self.position = position

class Board:
	def __init__(self):
		self.boxList = [Box(-1, i) for i in range(16)]
		self.display = [[' ' for i in range(17)] for j in range(41)]

		# Display Board
		numberList = []
		for box in self.boxList:
			numberList.append(box.number)

		self.display = [[' ' for i in range(17)] for j in range(41)]
	
		for y in range(17):
			for x in range(41):
				if y%4==0:
					if y == 0 or y == 16:
						self.display[x][y] = '-'
					else:
						if x%10==0:
							self.display[x][y] = '|'
						else:
							self.display[x][y] = '-'
				elif y%4==2:
					if x%10 == 0:
						self.display[x][y] = '|'
				elif y%4==1 or y%4==3:
					if x%10==0:
						self.display[x][y] = '|'

	def draw(self):
		for y in range(17):
			line = ""
			for x in range(41):
				line += self.display[x][y]
			print(line)

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
	board.draw()

main()

#C:\%HOMEPATH%\Desktop\Python\2048
#C:\Users\s12710216\AppData\Local\Git\bin\git.exe