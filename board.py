import pygame
from arrow import Arrow
from Direction import Direction
from numpy import random


class Board:
    def __init__(self, rows, cols, cell_size, startPos):
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.startPos = startPos
        self.grid = [[None for _ in range(cols)] for _ in range(rows)]
        self.arrow_count = 0
        self.win_font = pygame.font.SysFont("Arial", self.cell_size)
        self.win_text = self.win_font.render("YOU WIN!!!", True, (0, 0, 0))
        self.win_text_rect = self.win_text.get_rect(center=(((cols + 2) * cell_size) / 2, ((rows + 2) * cell_size) / 2))

        self.populate_test_grid()


    def draw(self, screen):
        startX, startY = self.startPos

        for i in range(self.rows + 1):
            pygame.draw.line(screen, (0, 0, 0), (startX, startY + i * self.cell_size),
                             (startX + self.cols * self.cell_size, startY + i * self.cell_size))

        for j in range(self.cols + 1):
            pygame.draw.line(screen, (0, 0, 0), (startX + j * self.cell_size, startY),
                             (startX + j * self.cell_size, startY + self.rows * self.cell_size))

        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] is not None:
                    cell_rect = pygame.Rect(startX + j * self.cell_size, startY + i * self.cell_size, self.cell_size, self.cell_size)
                    self.grid[i][j].draw(screen, cell_rect)

        if self.has_won():
            screen.blit(self.win_text, self.win_text_rect)


    def get_cell_from_mouse(self, pos):
        x, y = pos
        startX, startY = self.startPos

        col = (x - startX) // self.cell_size
        row = (y - startY) // self.cell_size

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return None
        return row, col

    def populate_test_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                arrow = random.choice([Arrow(random.choice(list(Direction)) , self.cell_size), None])
                if arrow is not None:
                    self.set_arrow(i, j, arrow)
                    self.arrow_count += 1


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
                self.arrow_count -= 1

    def has_won(self):
        return self.arrow_count == 0
