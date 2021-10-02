from copy import deepcopy
from itertools import chain
from random import choice
from random import randint


class Box:
    def __init__(self, number, position):
        self.number = number
        self.position = position

        self.current_location = Board.get_position_location(position)
        self.frame_update = 30
        self.update_image = False

        self.slide_frames = 0
        self.slide_number = None
        self.slide_position = None

    def get_image(self, path):
        if self.slide_number == None:
            return path + str(self.number) + ".png"

        return path + str(self.slide_number) + ".png"

    def velocity_move(self):
        # When slide is done update number
        if self.slide_frames == 0 and not self.slide_number == None:
            self.slide_number = None
            self.update_image = True

        # When slide is done update box location
        if self.slide_frames == 0 and not self.slide_position == None:
            self.slide_position = None
            self.current_location = Board.get_position_location(self.position)
            self.update_image = True

        # Slide logic
        if not self.slide_frames == 0 and not self.slide_position == None:
            correct_position_location = Board.get_position_location(
                self.position)
            correct_slide_location = Board.get_position_location(
                self.slide_position)

            # Takes: 15 frames = Time: 1/2 a second with 30FPS < -Less clean. +Less resources
            # Takes: 30 frames = Time: 1/2 a second with 60FPS < +More clean. -More resources
            velocity = [(correct_position_location[0] - correct_slide_location[0])/self.frame_update,
                        (correct_position_location[1] - correct_slide_location[1])/self.frame_update]

            self.current_location[0] += velocity[0]
            self.current_location[1] += velocity[1]

            self.slide_frames -= 1
            self.update_image = True
        # For delayed number change
        elif not self.slide_frames == 0 and self.slide_position == None:
            self.slide_frames -= 1


class Board:
    def __init__(self):
        self.grid = list(map(lambda i: [Box(0, i), Box(
            0, i + 1), Box(0, i + 2), Box(0, i + 3)], [0, 4, 8, 12]))
        self.points = 0

        self.add_random_box()
        self.add_random_box()

    # Static helper functions
    @staticmethod
    def print_grid(grid):
        for array in grid:
            temp = []
            for box in array:
                temp.append(box.number)
            print(temp)
        print(" ")

    @staticmethod
    def get_grid_image(path):
        return path + "grid.png"

    @staticmethod
    def get_score_image(path):
        return path + "score.png"

    @staticmethod
    def get_title_image(path):
        return path + "title.png"

    @staticmethod
    def get_position_location(position):
        return [((position % 4) * 117) + 13, ((position // 4) * 117) + 13]

    # Class helper functions
    # Boxes linked to main 2d grid. Changing this grid doesnt affect main 2d grid
    def get_grid_as_list(self):
        return list(chain.from_iterable(self.grid))

    def index_to_2d(self, index):
        return [index // 4, index % 4]

    # Logic
    def add_random_box(self):
        empty_positions = []
        for box in self.get_grid_as_list():
            if box.number == 0:
                empty_positions.append(box.position)

        if not empty_positions:
            return

        position = choice(empty_positions)
        number = 2 if randint(1, 11) <= 9 else 4

        box = self.get_grid_as_list()[position]

        box.number = number
        box.update_image = True

    def can_move_box(self):
        grid = self.get_grid_as_list()
        if list(filter(lambda box: box.number == 0, grid)):
            return True

        for i in range(len(grid)):
            if i == 15:
                return False
            elif i == 15 % 4:
                if grid[i].number == grid[i + 4].number:  # Check below
                    return True
            elif i > 11:
                if grid[i].number == grid[i + 1].number:  # Check to the right
                    return True
            else:
                if grid[i].number == grid[i + 1].number:  # Check to the right
                    return True
                elif grid[i].number == grid[i + 4].number:  # Check below
                    return True

        return False

    def move_boxes(self, direction):
        return

    # Can only slide to zeros and combinable numbers
    def slide_box(self, box_position, box_to_position):
        box = self.get_grid_as_list()[box_position]
        box_to = self.get_grid_as_list()[box_to_position]

        if box_to.number == 0:
            box.slide_position = box.position
            box.position = box_to.position

            box.slide_frames = box.frame_update

            box_to.position = box.slide_position
            box_to.update_image
        else:
            box.slide_position = box.position
            box.position = box_to.position

            box.slide_number = box.number
            box.number *= 2

            box.slide_frames = box.frame_update

            box_to.position = box.slide_position

            box_to.slide_number = box_to.number
            box_to.number = 0

            box_to.slide_frames = box_to.frame_update

        box_index = self.index_to_2d(box.position)
        box_to_index = self.index_to_2d(box_to.position)

        self.grid[box_index[0]][box_index[1]] = box
        self.grid[box_to_index[0]][box_to_index[1]] = box_to
        self.print_grid(self.grid)
