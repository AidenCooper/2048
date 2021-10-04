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

        # Start the slide and go for this many frames
        self.slide_frames = 0
        # The pre updated number during slide that is being shown
        self.slide_number = None
        # Starting position of slide where position immediatly updates to end position
        self.slide_position = None
        # Forces the box to slide to this position instead of end position
        self.slide_combine_position = None

    def get_image(self, path):
        if self.slide_number == None:
            return path + str(self.number) + ".png"

        return path + str(self.slide_number) + ".png"

    def velocity_move(self):
        if not self.slide_frames == 0:
            self.slide_frames -= 1

            position_location = Board.get_position_location(self.position)
            slide_location = []
            if self.slide_combine_position == None:
                slide_location = Board.get_position_location(
                    self.slide_position)
            else:
                slide_location = Board.get_position_location(
                    self.slide_combine_position)

            velocity = [(slide_location[0] - position_location[0])/self.frame_update,
                        (slide_location[1] - position_location[0])/self.frame_update]

            self.update_image = True
        elif self.slide_frames == 0 and (not self.slide_position == None or not self.slide_combine_position == None):
            self.slide_position = None
            self.slide_combine_position = None


class Board:
    def __init__(self):
        self.grid = list(map(lambda i: [Box(0, i), Box(
            0, i + 1), Box(0, i + 2), Box(0, i + 3)], [0, 4, 8, 12]))
        self.points = 0

        # self.add_random_box()
        # self.add_random_box()

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
        if direction == "up":
            for i in range(4):
                combined_pos = None
                for j in range(1, 4):
                    for k in range(j - 1, -1, -1):
                        if self.grid[j][i].number == 0:
                            break
                        elif self.grid[k][i].number == 0 and k == 0:
                            self.slide_box(j * 4 + i, k * 4 + i)
                            break
                        elif not self.grid[k][i].number == 0 and not self.grid[k][i].number == self.grid[j][i].number:
                            if not k + 1 == j and self.grid[k + 1][i].number == 0:
                                self.slide_box(j * 4 + i, (k + 1) * 4 + i)
                            break
                        elif self.grid[k][i].number == self.grid[k][i].number and combined_pos == k:
                            if not k + 1 == j and self.grid[k + 1][i].number == 0:
                                self.slide_box(j * 4 + i, (k + 1) * 4 + i)
                            break
                        elif self.grid[k][i].number == self.grid[j][i].number and not combined_pos == k:
                            combined_pos = k
                            self.slide_box(j * 4 + i, k * 4 + i)
                            break
        elif direction == "down":
            for i in range(3, -1, -1):
                combined_pos = None
                for j in range(2, -1, -1):
                    for k in range(j + 1, 4):
                        if self.grid[j][i].number == 0:
                            break
                        elif self.grid[k][i].number == 0 and k == 3:
                            self.slide_box(j * 4 + i, k * 4 + i)
                            break
                        elif not self.grid[k][i].number == 0 and not self.grid[k][i].number == self.grid[j][i].number:
                            if not k - 1 == j and self.grid[k - 1][i].number == 0:
                                self.slide_box(j * 4 + i, (k - 1) * 4 + i)
                            break
                        elif self.grid[k][i].number == self.grid[k][i].number and combined_pos == k:
                            if not k - 1 == j and self.grid[k - 1][i].number == 0:
                                self.slide_box(j * 4 + i, (k - 1) * 4 + i)
                            break
                        elif self.grid[k][i].number == self.grid[j][i].number and not combined_pos == k:
                            combined_pos = k
                            self.slide_box(j * 4 + i, k * 4 + i)
                            break
        elif direction == "left":
            for i in range(4):
                combined_pos = None
                for j in range(1, 4):
                    for k in range(j - 1, -1, -1):
                        if self.grid[i][j].number == 0:
                            break
                        elif self.grid[i][k].number == 0 and k == 0:
                            self.slide_box(i * 4 + j, i * 4 + k)
                            break
                        elif not self.grid[i][k].number == 0 and not self.grid[i][k].number == self.grid[i][j].number:
                            if not k + 1 == j and self.grid[i][k + 1].number == 0:
                                self.slide_box(i * 4 + j, i * 4 + (k + 1))
                            break
                        elif self.grid[i][k].number == self.grid[i][k].number and combined_pos == k:
                            if not k + 1 == j and self.grid[i][k + 1].number == 0:
                                self.slide_box(i * 4 + j, i * 4 + (k + 1))
                            break
                        elif self.grid[i][k].number == self.grid[i][j].number and not combined_pos == k:
                            combined_pos = k
                            self.slide_box(i * 4 + j, i * 4 + k)
                            break
        elif direction == "right":
            for i in range(3, -1, -1):
                combined_pos = None
                for j in range(2, -1, -1):
                    for k in range(j + 1, 4):
                        if self.grid[i][j].number == 0:
                            break
                        elif self.grid[i][k].number == 0 and k == 3:
                            self.slide_box(i * 4 + j, i * 4 + k)
                            break
                        elif not self.grid[i][k].number == 0 and not self.grid[i][k].number == self.grid[i][j].number:
                            if not k - 1 == j and self.grid[i][k - 1].number == 0:
                                self.slide_box(i * 4 + j, i * 4 + (k - 1))
                            break
                        elif self.grid[i][k].number == self.grid[i][k].number and combined_pos == k:
                            if not k - 1 == j and self.grid[i][k - 1].number == 0:
                                self.slide_box(i * 4 + j, i * 4 + (k - 1))
                            break
                        elif self.grid[i][k].number == self.grid[i][j].number and not combined_pos == k:
                            combined_pos = k
                            self.slide_box(i * 4 + j, i * 4 + k)
                            break

    # Can only slide to zeros and combinable numbers
    def slide_box(self, box_position, box_to_position):
        box = self.get_grid_as_list()[box_position]
        box_to = self.get_grid_as_list()[box_to_position]

        if box_to.number == 0:
            box.slide_position = box.position
            box.position = box_to.position
            box.slide_frames = box.frame_update

            box_to.position = box.slide_position
            box_to.slide_frames = box_to.frame_update
        else:
            box.slide_position = box.position
            box.position = box_to.position
            box.slide_number = box.number
            box.number *= 2
            box.slide_frames = box.frame_update

            box_to.slide_combine_position = box_to.position
            box_to.position = box.slide_position
            box_to.slide_number = box_to.number
            box_to.number = 0
            box_to.slide_frames = box_to.frame_update

        box.update_image = True
        box_to.update_image = True

        box_index = self.index_to_2d(box.position)
        box_to_index = self.index_to_2d(box_to.position)

        self.grid[box_index[0]][box_index[1]] = box
        self.grid[box_to_index[0]][box_to_index[1]] = box_to
