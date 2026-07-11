import pygame

from level_loader import load_level
from board import Board

class LevelManager:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.current_level = 1
        self.max_levels = 2
        self.level_completed = False
        self.win_time = 0
        self.board = self.create_board(self.current_level)

        self.level_font = pygame.font.SysFont("Arial", 32)
        self.level_text = self.level_font.render("Level 1", True, (0, 0, 0))
        self.level_text_rect = self.level_text.get_rect(center=(screen_width / 2, 50))

        self.win_font = pygame.font.SysFont("Arial", 48)
        self.win_text = self.win_font.render("YOU WIN!!!", True, (0, 0, 0))
        self.win_text_rect = self.win_text.get_rect(center=(screen_width / 2, screen_height / 2))

    def create_board(self, level):
        grid = load_level(f'levels/level{level}.csv')

        if grid is None:
            exit("Invalid level file")

        board = Board(self.screen_width, self.screen_height + 100, grid)

        return board

    def draw(self, screen):
        screen.blit(self.level_text, self.level_text_rect)

        self.board.draw(screen)

        if self.board.has_won():
            screen.blit(self.win_text, self.win_text_rect)

    def handle_click(self, pos):
        self.board.handle_click(pos)

    def update(self, screen_width, screen_height):
        self.board.update(screen_width, screen_height)

        if self.board.has_won() and self.win_time == 0:
            self.win_time = pygame.time.get_ticks()

        if self.board.has_won() and not self.level_completed and pygame.time.get_ticks() - self.win_time > 3000:
            self.level_completed = True
            if self.current_level < self.max_levels:
                self.current_level += 1

                self.board = self.create_board(self.current_level)
                self.level_text = self.level_font.render(f"Level {self.current_level}", True, (0, 0, 0))
                self.win_time = 0
                self.level_completed = False