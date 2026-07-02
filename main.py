import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Arrow Game")


running = True

rows = 6
cols = 6

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for i in range(rows + 1):
        for j in range(cols + 1):
            pygame.draw.line(screen, (0, 0, 0), ((i+  1)*100, 100), ((i + 1)*100, 700))
            pygame.draw.line(screen, (0, 0, 0), (100, (i + 1) * 100), (700, (i + 1) * 100))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()