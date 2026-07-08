import pygame
from numpy.random.mtrand import random

from board import Board
from arrow import Arrow
from direction import Direction

pygame.init()

rows = 4
cols = 4
cell_size = 50
screen = pygame.display.set_mode(((cols + 2) * cell_size, (rows + 2) * cell_size))
pygame.display.set_caption("Arrow Game")
clock = pygame.time.Clock()

grid = [[Arrow(Direction.UP) for _ in range(cols)] for _ in range(rows)]

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