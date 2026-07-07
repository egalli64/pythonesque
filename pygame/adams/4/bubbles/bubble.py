"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

from random import randint
from typing import Dict


import pygame
from settings import Settings
from bubble_container import BubbleContainer


class Bubble(pygame.sprite.Sprite):
    """The sprite class of the bubble."""

    BUBBLE_CONTAINER: Dict[str, BubbleContainer] = {}

    def __init__(self, speed: int) -> None:
        """Constructor."""
        super().__init__()

        Bubble.BUBBLE_CONTAINER["blue"] = BubbleContainer("bubble1.png")
        Bubble.BUBBLE_CONTAINER["red"] = BubbleContainer("bubble2.png")

        self.mode = "blue"
        self.radius = Settings.RADIUS["min"]
        self.image = Bubble.BUBBLE_CONTAINER[self.mode].get(self.radius)
        self.rect: pygame.Rect = self.image.get_rect()
        self.fradius = float(self.radius)
        self.speed = speed

    def update(self, *args, **kwargs) -> None:
        """Let the bubble grow.

        Args:
            *args (Tuple[int]): not used
            **kwargs Dict[str, Any]: possible key/value pairs:
                                      (action/grow), (action/sting),
                                      (mode/blue), (mode/red))
        """
        if "action" in kwargs.keys():
            dt = 1 / 60  # TODO: use actual dt
            if kwargs["action"] == "grow":
                self.fradius += self.speed * dt
                self.fradius = min(self.fradius, Settings.RADIUS["max"])
                self.radius = round(self.fradius)
                center = self.rect.center
                self.image = Bubble.BUBBLE_CONTAINER[self.mode].get(self.radius)
                self.rect = self.image.get_rect()
                self.rect.center = center
            elif kwargs["action"] == "sting":
                self.stung()
        elif "mode" in kwargs.keys():
            self.set_mode(kwargs["mode"])

    def set_mode(self, mode: str) -> None:
        """Sets the bubble in the mode "red" or "blue".

        Args:
            mode (str): "red" oder "blue"
        """
        if mode != self.mode:
            self.mode = mode
            self.image = Bubble.BUBBLE_CONTAINER[self.mode].get(self.radius)

    def randompos(self) -> None:
        """Computes a new position of the center by random."""
        bubbledistance = Settings.DISTANCE + Settings.RADIUS["min"]
        centerx = randint(
            Settings.PLAYGROUND.left + bubbledistance,
            Settings.PLAYGROUND.right - bubbledistance,
        )
        centery = randint(
            Settings.PLAYGROUND.top + bubbledistance,
            Settings.PLAYGROUND.bottom - bubbledistance,
        )
        self.rect.center = (centerx, centery)

    def stung(self):
        """The bubble removes itself and the score increases."""
        self.kill()
        Settings.POINTS += self.radius
