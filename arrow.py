import pygame
from Direction import Direction

class Arrow:
    SYMBOLS = {
        Direction.UP: "↑",
        Direction.DOWN: "↓",
        Direction.LEFT: "←",
        Direction.RIGHT: "→"
    }

    def __init__(self, direction, size):
        self.direction = direction
        self.font = pygame.font.SysFont("segoeuisymbol",size)

    def draw(self, screen, box_rect):
        char = self.SYMBOLS[self.direction]
        text = self.font.render(char, True, (0, 0, 0))
        text_rect = text.get_rect(center=box_rect.center)
        screen.blit(text, text_rect)