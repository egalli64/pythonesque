"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

import pygame
from settings import Settings


class Points(pygame.sprite.Sprite):
    """Class in order to generate a image of the score."""

    def __init__(self) -> None:
        """Constructor"""
        super().__init__()
        self.font = pygame.font.Font(pygame.font.get_default_font(), 18)
        self.oldpoints = -1

    def update(self, *args, **kwargs) -> None:
        """Let the bubble grow.

        Args:
            *args (Tuple[int]): not used
            **kwargs Dict[str, Any]: not used
        """
        if self.oldpoints != Settings.POINTS:
            self.image = self.font.render(f"Points: {Settings.POINTS}", True, "red")
            self.rect = self.image.get_rect()
            self.rect.left = Settings.BOX.left
            self.rect.top = Settings.BOX.top
