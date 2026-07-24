"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fish tank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""
import pygame
from settings import Settings


class Score:
    image: pygame.Surface
    rect: pygame.Rect
    dirty: bool

    FILENAME = None
    TEXT = "Points: {}"
    COLOR = "red"

    @classmethod
    def load_resources(cls):
        cls.font = pygame.font.Font(Score.FILENAME, 32)

    def __init__(self):
        self.score = 0

        self.reset()

    def reset(self):
        self.image = Score.font.render(f"Score: {self.score}", True, Score.COLOR)
        self.rect = self.image.get_rect()
        self.rect.left = Settings.BOX.left
        self.rect.top = Settings.BOX.top
        self.dirty = False

    def change_score(self, delta=None):
        self.score = self.score + delta if delta else 0
        self.dirty = True

    def update(self, action):
        if self.dirty:
            self.reset()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
