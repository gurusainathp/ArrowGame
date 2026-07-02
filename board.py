import pygame

class Board:
    def __init__(self, rows, cols, size, startPos):
        self.rows = rows
        self.cols = cols
        self.size = size
        self.startPos = startPos

    def draw(self, screen):
        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                pygame.draw.line(screen, (0, 0, 0), ((i + 1) * 100, 100), ((i + 1) * 100, 700))
                pygame.draw.line(screen, (0, 0, 0), (100, (i + 1) * 100), (700, (i + 1) * 100))

    def get_cell_from_mouse(self, pos):
        x, y = pos
        startX, startY = self.startPos

        row = (startX - x) // self.rows
        col = (startY - y) // self.cols

        return row, col
