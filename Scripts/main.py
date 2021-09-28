from pygame.constants import KEYDOWN
import game
from game import pygame
from sys import exit
from os import getcwd


def main():
    pygame.init()
    board = game.Board()

    BACKGROUND = 250, 248, 239
    FONT = pygame.font.SysFont("bell mt.ttf", 32)
    FPS = 30
    SIZE = 480, 668

    screen = pygame.display.set_mode(SIZE)

    path = ".\\Assets\\"
    if "Scripts" in getcwd():
        path = "..\\Assets\\"

    GRID = pygame.image.load(board.get_grid_image(path))
    GRID_RECT = GRID.get_rect()
    GRID_RECT.bottom = SIZE[1]

    SCORE = pygame.image.load(board.get_score_image(path))
    SCORE_RECT = SCORE.get_rect()
    SCORE_RECT.topright = SIZE[0] - 10, 10

    SCORE_TEXT = FONT.render(str(board.points), True, (255, 255, 255))
    SCORE_TEXT_RECT = SCORE_TEXT.get_rect()
    SCORE_TEXT_RECT.centerx = SCORE_RECT.centerx
    SCORE_TEXT_RECT.top = SCORE_RECT.centery

    TITLE = pygame.image.load(board.get_title_image(path))
    TITLE_RECT = TITLE.get_rect()
    TITLE_RECT.centerx = GRID_RECT.centerx
    TITLE_RECT.bottom = GRID_RECT.top - 15

    BOXES = [pygame.image.load(box.get_image(path))
             for box in board.get_list()]
    BOXES_RECT = [BOX.get_rect() for BOX in BOXES]
    for i in range(len(BOXES)):
        size = board.get_box(i).current_position
        BOXES_RECT[i].topleft = GRID_RECT.left + \
            size[0], GRID_RECT.top + size[1]

    while board.can_move():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    board.move_grid("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    board.move_grid("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    board.move_grid("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    board.move_grid("right")

        if board.update:
            BOXES = [pygame.image.load(box.get_image(path))
                     for box in board.get_list()]
            board.update = False

        screen.fill(BACKGROUND)

        screen.blit(GRID, GRID_RECT)
        screen.blit(SCORE, SCORE_RECT)
        screen.blit(SCORE_TEXT, SCORE_TEXT_RECT)
        screen.blit(TITLE, TITLE_RECT)

        [screen.blit(BOXES[i], BOXES_RECT[i]) for i in range(len(BOXES))]

        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    main()
