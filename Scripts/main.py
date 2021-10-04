import game
import pygame
from sys import exit
from os import getcwd


def main():
    # Initialize game and board
    pygame.init()
    board = game.Board()

    # Set the settings for graphics
    BACKGROUND = 250, 248, 239
    CLOCK = pygame.time.Clock()
    FONT = pygame.font.SysFont("bell mt.ttf", 32)
    FPS = 120
    SIZE = 480, 668

    screen = pygame.display.set_mode(SIZE)

    # Find Asset path from where your running
    path = ".\\Assets\\"
    if "Scripts" in getcwd():
        path = "..\\Assets\\"

    # Makes zeroes transparent
    BOXES = [pygame.image.load(box.get_image(path)).convert_alpha()
             for box in board.get_grid_as_list()]
    GRID = pygame.image.load(board.get_grid_image(path))
    SCORE = pygame.image.load(board.get_score_image(path))
    SCORE_TEXT = FONT.render(str(board.points), True, (255, 255, 255))
    TITLE = pygame.image.load(board.get_title_image(path))

    # Constant position/size rectangles
    GRID_RECT = GRID.get_rect()
    GRID_RECT.bottom = SIZE[1]

    SCORE_RECT = SCORE.get_rect()
    SCORE_RECT.topright = SIZE[0] - 10, 10

    SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
    SCORE_TEXT_RECT.centerx = SCORE_RECT.centerx
    SCORE_TEXT_RECT.top = SCORE_RECT.centery

    TITLE_RECT = TITLE.get_rect()
    TITLE_RECT.centerx = GRID_RECT.centerx
    TITLE_RECT.bottom = GRID_RECT.top - 15

    box1 = board.get_grid_as_list()[0]
    box2 = board.get_grid_as_list()[4]
    box3 = board.get_grid_as_list()[8]
    box4 = board.get_grid_as_list()[12]

    box1.number = 2
    box2.number = 2
    box3.number = 0
    box4.number = 4

    box1.update_image = True
    box2.update_image = True
    box3.update_image = True
    box4.update_image = True

    board.print_grid(board.grid)

    # Run game loop
    while board.can_move_box():
        # Update non constant rectangles and box images
        BOXES_RECT = []
        for i in range(len(BOXES)):
            board.get_grid_as_list()[i].velocity_move()

            if board.get_grid_as_list()[i].update_image:
                BOXES[i] = pygame.image.load(
                    board.get_grid_as_list()[i].get_image(path))
                board.get_grid_as_list()[i].update_image = False

            BOX_RECT = BOXES[i].get_rect().topleft = GRID_RECT.left + \
                board.get_grid_as_list()[i].current_location[0], GRID_RECT.top + \
                board.get_grid_as_list()[i].current_location[1]
            BOXES_RECT.append(BOX_RECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.constants.KEYDOWN:
                direction = None

                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = "down"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = "right"
                else:
                    continue

                for box in board.get_grid_as_list():
                    box.slide_frames = 0

                board.move_boxes(direction)
                board.print_grid(board.grid)
                # board.add_random_box()

        # Display Graphics
        screen.fill(BACKGROUND)

        screen.blit(GRID, GRID_RECT)
        screen.blit(SCORE, SCORE_RECT)
        screen.blit(SCORE_TEXT, SCORE_TEXT_RECT)
        screen.blit(TITLE, TITLE_RECT)

        [screen.blit(BOXES[i], BOXES_RECT[i]) for i in range(len(BOXES))]

        # Pygame Updates
        pygame.display.update()
        CLOCK.tick(FPS)

    return


if __name__ == "__main__":
    main()

# TODO
# Fix velocity movement
# Point System

# C:\Users\s12710216\AppData\Local\Git\bin\git.exe
