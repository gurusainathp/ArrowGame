import pygame

from level_manager import LevelManager

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Arrow Game")
clock = pygame.time.Clock()

manager = LevelManager(screen.get_width(), screen.get_height())

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            manager.handle_click(event.pos)

    manager.update(screen.get_width(), screen.get_height())

    screen.fill((255, 255, 255))

    manager.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()