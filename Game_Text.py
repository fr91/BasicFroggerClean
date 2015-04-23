import pygame


class GameText(object):
    def __init__(self, game_screen, x_position, y_position, text, font):
        self.game_screen = game_screen
        self.x_position = x_position
        self.y_position = y_position
        self.text = text
        self.font = font

    def game_object_draw(self):
        font = pygame.font.SysFont("Callisto", self.font)
        game_text = font.render(str(self.text), True, (0, 0, 0))
        self.game_screen.blit(game_text, (self.x_position, self.y_position))
