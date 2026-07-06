"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong paddle
"""

import pygame

from settings import Settings


class Paddle(pygame.sprite.Sprite):
    BORDERDISTANCE = {"horizontal": 50, "vertical": 10}
    DIRECTION = {"up": -1, "down": 1, "halt": 0}

    def __init__(self, player: str, viewport: pygame.Rect) -> None:
        super().__init__()

        self.viewport = viewport
        self.rect: pygame.FRect = pygame.FRect(0, 0, 15, viewport.height // 10)
        self.rect.centery = viewport.centery
        self.images = {
            "byhand": pygame.Surface(self.rect.size).convert(),
            "byki": pygame.Surface(self.rect.size).convert(),
        }
        self.images["byhand"].fill("yellow")
        self.images["byki"].fill("deepskyblue2")
        self.player = player
        if self.player == "left":
            self.rect.left = Paddle.BORDERDISTANCE["horizontal"]
        else:
            self.rect.right = viewport.right - Paddle.BORDERDISTANCE["horizontal"]
        self.speed = viewport.height // 2
        self.direction = Paddle.DIRECTION["halt"]
        self.select_image()

    def update(self, *args, **kwargs) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "move":
                self._move()
            elif kwargs["action"] in Paddle.DIRECTION.keys():
                self.direction = Paddle.DIRECTION[kwargs["action"]]
        self.select_image()
        return super().update(*args, **kwargs)

    def _move(self) -> None:
        dt = 1 / 60  # TODO: actual dt
        if self.direction != Paddle.DIRECTION["halt"]:
            self.rect.move_ip(0, self.speed * self.direction * dt)
            if self.direction == Paddle.DIRECTION["up"]:
                self.rect.top = max(self.rect.top, Paddle.BORDERDISTANCE["vertical"])
            elif self.direction == Paddle.DIRECTION["down"]:
                self.rect.bottom = min(
                    self.rect.bottom,
                    self.viewport.height - Paddle.BORDERDISTANCE["vertical"],
                )

    def select_image(self) -> None:
        if self.player == "left":
            if Settings.KI["left"]:
                self.image = self.images["byki"]
            else:
                self.image = self.images["byhand"]
        else:
            if Settings.KI["right"]:
                self.image = self.images["byki"]
            else:
                self.image = self.images["byhand"]
