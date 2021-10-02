import game
import pygame
from operator import attrgetter

board = game.Board()

# BOXES = [print(board.get_grid_as_list()[box[1]]) for box in [[board.get_grid_as_list()[i].number, i]
# for i in range(len(board.get_grid_as_list()))].sort(key=lambda content: content[0])]

array = []
for i in range(len(board.get_grid_as_list())):
    array.append([board.get_grid_as_list()[i].number, i])
array.sort(key=lambda content: content[0])
print(array)
