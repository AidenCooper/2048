from copy import deepcopy
from itertools import chain
from random import choice
from random import randint


class Box:
    def __init__(self, number, position):
        self.number = number
        self.position = position
        self.update_image = False

        # For sliding animation
        self.current_position = [((position % 4) * 117) +
                                 13, ((position // 4) * 117) + 13]
        self.velocity = [0, 0]

    def get_image(self, path):
        return path + str(self.number) + ".png"

    def velocity_move(self):
        if self.velocity == [0, 0]:
            return False

        self.current_position[0] += self.velocity[0]
        self.current_position[1] += self.velocity[1]

        return True


class Board:
    def __init__(self):
        self.grid = list(map(lambda i: [Box(0, i), Box(
            0, i + 1), Box(0, i + 2), Box(0, i + 3)], [0, 4, 8, 12]))
        self.points = 0

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

    def get_grid_image(self, path):
        return path + "grid.png"

    def get_score_image(self, path):
        return path + "score.png"

    def get_title_image(self, path):
        return path + "title.png"

    def get_box(self, position):
        return self.grid[position // 4][position % 4]

    def get_grid_as_list(self):
        return list(chain.from_iterable(self.grid))

    def get_position_location(self, position):
        return ((position // 4) * 117) + 13, ((position % 4) * 117) + 13

    # Logic
    def add_random_box(self):
        empty_positions = []
        for box in self.get_grid_as_list():
            if box.number == 0:
                empty_positions.append(box.position)

        if not empty_positions:
            return False

        position = choice(empty_positions)
        number = 2 if randint(1, 11) <= 9 else 4

        self.get_box(position).number = number

        return True

    def can_move_box(self):
        for i in range(0, len(self.get_grid_as_list())):
            pass
        return True

    def move_boxes(self, direction):
        return

# 0 0 0 2
# 0 2 0 0
# 0 2 0 0
# 4 0 2 2
