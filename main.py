import pygame

from board import Board
from level_loader import load_level

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Arrow Game")
clock = pygame.time.Clock()

grid = load_level("levels/level1.csv")

if grid is None:
    exit("Invalid level file")

board = Board(screen.get_width(), screen.get_height(), grid)

#Initial Grid
board.draw_initial_arrow_grid(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.handle_click(event.pos)

    board.update(screen.get_width(), screen.get_height())

    screen.fill((255, 255, 255))

    board.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()