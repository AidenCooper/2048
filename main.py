import sys
import pygame

pygame.init()

FPS = 30
SIZE = WIDTH, HEIGHT = 320, 240

SCREEN = pygame.display.set_mode(SIZE)

# image = pygame.image.lod("image.png")
# gif = pygame.image.lod("gif.gif")

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

# C:\%HOMEPATH%\Desktop\Python\Game
# C:\Users\s12710216\AppData\Local\Git\bin\git.exe