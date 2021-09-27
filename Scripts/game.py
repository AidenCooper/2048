from itertools import chain
from random import choice
from random import randint

import pygame

class Box:
    def __init__(self, number, position):
        self.number = number
        self.position = position
        self.current_position = ((self.position // 4) * 117) + 13, ((self.position % 4) * 117) + 13
    
    def get_image(self, path):
        return path + str(self.number) + ".png"
    
    def slide(self, location_from, location_to):
        return
    
class Board:
    def __init__(self):
        self.grid = list(map(lambda i: [Box(0, i), Box(0, i + 1), Box(0, i + 2), Box(0, i + 3)], [0, 4, 8, 12]))
        self.points = 0
        self.update = False

        self.add_random_box()
        self.add_random_box()

    # Helper functions
    def update_grid(self):
        for i, array in enumerate(self.grid):
            for j, box in enumerate(array):
                box.position = (i * 4) + j
        self.update = True

    def get_grid_image(self, path):
        return path + "grid.png"

    def get_score_image(self, path):
        return path + "score.png"

    def get_title_image(self, path):
        return path + "title.png"

    def get_box(self, position):
        return self.grid[position // 4][position % 4]

    def get_list(self):
        return list(chain.from_iterable(self.grid))
    
    def get_position_location(self, position):
        return ((position // 4) * 117) + 13, ((position % 4) * 117) + 13

    # Logic
    def add_random_box(self):
        empty_positions = []
        for box in self.get_list():
            if box.number == 0:
                empty_positions.append(box.position)
        
        if not empty_positions:
            return False
        
        position = choice(empty_positions)
        number = 2 if randint(1, 11) <= 9 else 4
        self.get_box(position).number = number

        return True

    def can_move(self):
        return True

    def _move_array(self, grid):
        modified = []
        for array in grid:
            print("Test")
        return modified

    def move_up(self):
        return
    
    def move_down(self):
        return
    
    def move_left(self):
        grid = self.grid[::-1]
        grid = self._move_array(grid)

        self.grid = grid
        self.update_grid()
        return

    def move_right(self):
        grid = self.grid
        grid = self._move_array(grid)
        return

    def slide_box(self, position_from, position_to):
        return