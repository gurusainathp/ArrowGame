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
                    cell_rect = pygame.Rect(startX + j * self.size, startY + i * self.size, self.size, self.size)
                    self.grid[i][j].draw(screen, cell_rect)

    def get_cell_from_mouse(self, pos):
        x, y = pos
        startX, startY = self.startPos

        col = (x - startX) // self.size
        row = (y - startY) // self.size

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return row, col

    def populate_test_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = Arrow(random.choice(list(Direction)) , self.size)

    def get_arrow(self, row, col):
        return self.grid[row][col]

    def set_arrow(self, row, col, arrow):
        self.grid[row][col] = arrow

    def can_arrow_exit(self, row, col):
        arrow = self.get_arrow(row, col)
        dr, dc = arrow.direction.value

        while 0 <= row + dr < self.rows and 0 <= col + dc < self.cols:
            row += dr
            col += dc
            if self.grid[row][col] is not None:
                return False

        return True

    def handle_click(self, pos):
        cell = self.get_cell_from_mouse(pos)
        if cell is not None:
            row, col = cell
            arrow = self.get_arrow(row, col)
            if arrow is not None and self.can_arrow_exit(row, col):
                self.set_arrow(row, col, None)
