import random

def moveUp():
	row = [8, 4, 2, 4]
	constant = row[:]

	row = slide(row)
	row = combine(row)
	row = slide(row)

	print(row)

	if constant == row:
		return False
	else:
		constant = row
		return True

def slide(row):
		for i in range(1, 4):
			for j in reversed(range(0, i)):
				if row[j] == 0:
					row[j] = row[j + 1]
					row[j + 1] = 0
				else:
					break
		return row

def combine(row):
	for i in range(0, 3):
		if row[i] == row[i + 1]:
			row[i] *= 2
			row[i + 1] = 0
	return row

if moveUp():
	print("add")