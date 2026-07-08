import pygame
import numpy as np


class Board:
    def __init__(self, screen, grid):
        self.screen = screen
        self.grid = grid
        self.rows = self.calculate_rows_from_grid()
        self.cols = self.calculate_cols_from_grid()
        self.cell_size = self.calculate_cell_size()
        self.startPos = self.calculate_starting_pos()
        self.arrow_count = self.calculate_arrow_count()
        self.win_font = pygame.font.SysFont("Arial", self.cell_size)
        self.win_text = self.win_font.render("YOU WIN!!!", True, (0, 0, 0))
        self.win_text_rect = self.win_text.get_rect(center=(screen.get_width() / 2, screen.get_height() / 2))

    def calculate_rows_from_grid(self):
        return len(self.grid)

    def calculate_cols_from_grid(self):
        return len(self.grid[0])

    def calculate_cell_size(self):
        return min(self.screen.get_width() // (self.rows + 2), self.screen.get_width() // (self.cols + 2))

    def calculate_starting_pos(self):
        return (self.screen.get_width() // 2) - int((self.cols / 2) * self.cell_size), (self.screen.get_height() // 2) - int((self.rows / 2) * self.cell_size)

    def calculate_arrow_count(self):
        return np.count_nonzero(self.grid)

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
                arrow = self.grid[i][j]
                if arrow is not None:
                    arrow.set_arrow_size(self.cell_size)
                    if arrow.is_animating:
                        arrow.draw(screen, arrow.pixel_x, arrow.pixel_y)
                    elif -arrow.size < arrow.pixel_x < screen.get_width() and -arrow.size < arrow.pixel_y < screen.get_height():
                        arrow.draw(screen, startX + j * self.cell_size, startY + i * self.cell_size)

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
            if self.grid[row][col] is not None and not self.grid[row][col].is_animating:
                return False

        return True

    def handle_click(self, pos):
        cell = self.get_cell_from_mouse(pos)
        if cell is not None:
            row, col = cell
            arrow = self.get_arrow(row, col)
            if arrow is not None and self.can_arrow_exit(row, col):
                startX, startY = self.startPos
                arrow.start_animation(startX + col * self.cell_size, startY + row * self.cell_size)


    def has_won(self):
        return self.arrow_count == 0

    def update(self, screen_width, screen_height):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] is not None:
                    if self.grid[i][j].is_animating:
                        self.grid[i][j].update(screen_width, screen_height)
                    elif self.grid[i][j].finished:
                        self.set_arrow(i, j, None)
                        self.arrow_count -= 1
