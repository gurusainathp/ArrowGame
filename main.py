import pygame

from arrow import Arrow
from board import Board

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Arrow Game")
board = Board(6, 6, 100, (100, 100))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            cell = board.get_cell_from_mouse(pos)
            if cell is not None:
                row, col = cell
                arrow = board.get_arrow(row, col)
                if arrow is not None:
                    print("Clicked arrow at (",row,",",col,") facing ",arrow.direction)

    screen.fill((255, 255, 255))

    board.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()