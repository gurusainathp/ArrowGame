import pygame

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

    screen.fill((255, 255, 255))

    board.draw(screen)

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()