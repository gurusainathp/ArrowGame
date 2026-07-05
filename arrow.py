from enum import Enum

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
        self.pixel_x = 0
        self.pixel_y = 0
        self.is_animating = False
        self.finished = False
        self.speed = 5
        self.direction = direction
        self.size = size
        self.font = pygame.font.SysFont("segoeuisymbol",self.size)

    def draw(self, screen, pixel_x, pixel_y):
        box_rect = pygame.Rect(pixel_x, pixel_y, self.size, self.size)
        char = self.SYMBOLS[self.direction]
        text = self.font.render(char, True, (0, 0, 0))
        text_rect = text.get_rect(center=box_rect.center)
        screen.blit(text, text_rect)


    def update(self, screen_width, screen_height):
        dr, dc = self.direction.value
        if self.is_animating:
            self.pixel_x += dc * self.speed
            self.pixel_y += dr * self.speed
            if  self.pixel_x < -self.size or self.pixel_x > screen_width or self.pixel_y < -self.size or self.pixel_y > screen_height:
                    self.is_animating = False
                    self.finished = True

    def start_animation(self, pixel_x, pixel_y):
        self.pixel_x = pixel_x
        self.pixel_y = pixel_y
        self.is_animating = True

