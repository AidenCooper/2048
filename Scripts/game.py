from copy import deepcopy
from itertools import chain
from random import choice
from random import randint

import pygame


class Box:
    def __init__(self, number, position):
        self.number = number
        self.position = position

        # For sliding animation
        self.current_position = ((position % 4) * 117) + \
            13, ((position // 4) * 117) + 13
        self.velocity = 0, 0

    def get_image(self, path):
        return path + str(self.number) + ".png"

    def slide(self, location_from, location_to):
        self.velocity = [location_from[0] - location_to[0],
                         location_from[1] - location_to[1]]

    def move_box_location(self):
        self.current_position[0] += self.velocity[0]
        self.current_position[1] += self.velocity[1]


class Board:
    def __init__(self):
        self.grid = list(map(lambda i: [Box(0, i), Box(
            0, i + 1), Box(0, i + 2), Box(0, i + 3)], [0, 4, 8, 12]))
        self.points = 0
        self.update = False

        self.add_random_box()
        self.add_random_box()

    # Helper functions
    def print_grid(self, grid):
        for array in grid:
            temp = []
            for box in array:
                temp.append(box.number)
            print(temp)
        print(" ")

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

    def move_grid(self, direction):
        grid = deepcopy(self.grid)

        # direction Left = default
        if direction == "right":
            grid = [array[::-1] for array in grid]
        elif direction == "up":
            grid = list(map(list, list(zip(*grid))))
        elif direction == "down":
            grid = list(map(list, list(zip(*grid[::-1]))))

        modified = []
        for array in grid:
            for i in range(1, len(array)):
                if array[i].number == 0:
                    continue
                for j in range(i - 1, -1, -1):
                    if array[j].number == 0 and not j == 0:
                        continue
                    elif array[j].number == 0 and j == 0:
                        # array[j].number = array[i].number
                        # array[i].number = 0
                        break
                    elif not array[j].number == array[i].number and j + 1 == i:
                        break
                    elif array[j].number == array[i].number:
                        # array[j].number *= 2
                        # array[i].number = 0
                        break
                    elif not array[j].number == array[i].number and not j + 1 == i:
                        # array[j + 1].number = array[i].number
                        # array[i].number = 0
                        break
            modified.append(array)

        grid = modified

        # direction Left = default
        if direction == "right":
            grid = [array[::-1] for array in grid]
        elif direction == "up":
            grid = list(map(list, list(zip(*grid))))
        elif direction == "down":
            grid = list(map(list, list(zip(*grid))[::-1]))

        self.grid = grid
        self.update = True
