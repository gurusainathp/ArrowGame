from level_loader import load_level
from board import Board

class LevelManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.level = 1
        self.board = self.create_board(self.level)

    def create_board(self, level):
        grid = load_level(f'levels/level{level}.csv')

        if grid is None:
            exit("Invalid level file")

        board = Board(self.screen_width, self.screen_height, grid)

        return board

    def draw(self, screen):
        self.board.draw(screen)

    def handle_click(self, pos):
        self.board.handle_click(pos)

    def update(self, screen_width, screen_height):
        self.board.update(screen_width, screen_height)