import pygame

from board import Board

pygame.init()

rows = 4
cols = 4
cell_size = 100
screen = pygame.display.set_mode(((cols + 2) * cell_size, (rows + 2) * cell_size))
pygame.display.set_caption("Arrow Game")
clock = pygame.time.Clock()
board = Board(rows, cols, cell_size, (cell_size, cell_size))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.handle_click(event.pos)

    screen.fill((255, 255, 255))

    board.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()