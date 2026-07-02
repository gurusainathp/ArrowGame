import pygame
from arrow import Arrow
from Direction import Direction
from numpy import random

class Board:
    def __init__(self, rows, cols, size, startPos):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.startPos = startPos
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]

        self.populate_test_grid()


    def draw(self, screen):
        startX, startY = self.startPos

        for i in range(self.rows + 1):
            pygame.draw.line(screen, (0, 0, 0), (startX + i * self.size, startY),
                             (startX + i * self.size, startY + self.cols * self.size))

        for j in range(self.cols + 1):
            pygame.draw.line(screen, (0, 0, 0), (startX, startY + j * self.size),
                             (startX + self.rows * self.size, startY + j * self.size))

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] is not None:
                    cell_rect = pygame.Rect(startX + i * self.size, startY + j * self.size, self.size, self.size)
                    self.grid[i][j].draw(screen, cell_rect)

    def get_cell_from_mouse(self, pos):
        x, y = pos
        startX, startY = self.startPos

        row = (startX - x) // self.rows
        col = (startY - y) // self.cols

        return row, col

    def populate_test_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = Arrow(random.choice(list(Direction)) , self.size)