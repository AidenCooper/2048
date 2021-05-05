from enum import Enum
import random

class Position(Enum):
	First = [5, 2]
	Second = [15, 2]
	Third = [25, 2]
	Fourth = [35, 2]
	Fifth = [5, 6]
	Sixth = [15, 6]
	Seventh = [25, 6]
	Eigth = [35, 6]
	Ninth = [5, 10]
	Tenth = [15, 10]
	Eleventh = [15, 10]
	Twelfth = [15, 10]
	Thirteenth = [5, 14]
	Fourteenth = [15, 14]
	Fifteenth = [25, 14]
	Sixteenth = [35, 14]

class Box:
	def __init__(self, number, position):
		self.number = number
		self.position = position

class Board:
	def __init__(self):

		self.boxList = [Box(-1, position) for position in Position]
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
				line += str(self.display[x][y])
			print(line)

	def setPosition(self, box, toPos):
		if(box.number == -1):
			return

		length = len(str(box.number))

		if length == 1:
			self.display[toPos.value[0]][toPos.value[1]] =  box.number
		elif length % 3 == 0:
			sideLength = length % 2

			index = 0
			for i in range(toPos.value[0] - sideLength, toPos.value[0] + sideLength + 1):
				self.display[i][toPos.value[1]] = str(box.number)[index]
				index += 1
		else:
			if(length == 2):
				self.display[toPos.value[0] - 1][toPos.value[1]] = int(str(box.number)[0])
				self.display[toPos.value[0]][toPos.value[1]] = int(str(box.number)[1])
			else:
				number = str(box.number)[1:len(str(box.number))]
				newLength = len(str(number)) 
				sideLength = newLength % 2

				index = 0
				for i in range(toPos.value[0] - sideLength - 1, toPos.value[0] + sideLength + 1):
					self.display[i][toPos.value[1]] = str(box.number)[index]
					index += 1

		box.position = toPos

def main():
	board = Board()
	board.draw()

main()

#C:\%HOMEPATH%\Desktop\Python\2048
#C:\Users\s12710216\AppData\Local\Git\bin\git.exe