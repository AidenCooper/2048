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

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			pass

	SCREEN.fill(BACKGROUND)

	SCREEN.blit(GRID, [0, SCREEN.get_height() - GRID.get_height()])
	SCREEN.blit(TITLE, [(SCREEN.get_width() / 2) - (TITLE.get_width() / 2), (SCREEN.get_height() - GRID.get_height()) - (TITLE.get_height() + (TITLE.get_height() / 2))])
	
	pygame.display.flip()


# C:\%HOMEPATH%\Desktop\Python\2048\Scripts
# C:\Users\s12710216\AppData\Local\Git\bin\git.exe