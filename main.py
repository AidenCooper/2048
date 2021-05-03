import random

class Box:
	def __init__(self, number, position):
		self.number = number
		self.position = position

class Board:
	def __init__(self):
		self.boxList = []

		for i in range(16):
			self.boxList.append(Box(-1, i))

	def draw(self):
		numberList = []
		for box in self.boxList:
			numberList.append(box.number)

		space1 = ""
		space2 = ""

		space3 = ""
		space4 = ""

		space5 = ""
		space6 = ""

		line1 = "-----------------------------------------"
		line2 = "|         |         |         |         |"
		line3 = f"|    {numberList[0]}    |    {numberList[1]}    |    {numberList[2]}    |    {numberList[3]}    |"
		line4 = "|         |         |         |         |"
		line5 = "|---------|---------|---------|---------|"
		line6 = "|         |         |         |         |"
		line7 = "|    {}    |    {}    |    {}    |    {}    |"
		line8 = "|         |         |         |         |"
		line9 = "|---------|---------|---------|---------|"
		line10 = "|         |         |         |         |"
		line11 = "|    {}    |    {}    |    {}    |    {}    |"
		line12 = "|         |         |         |         |"
		line13 = "|---------|---------|---------|---------|"
		line14 = "|         |         |         |         |"
		line15 = "|    {}    |    {}    |    {}    |    {}    |"
		line16 = "|         |         |         |         |"
		line17 = "-----------------------------------------"

		print(line1)
		print(line2)
		print(line3)
		print(line4)
		print(line5)
		print(line6)
		print(line7)
		print(line8)
		print(line9)
		print(line10)
		print(line11)
		print(line12)
		print(line13)
		print(line14)
		print(line15)
		print(line16)
		print(line17)


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