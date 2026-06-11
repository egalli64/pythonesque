"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Mouse actions
"""

from time import time
from typing import Any, Tuple
import pygame
from pygame.constants import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT


class Ball(pygame.sprite.Sprite):
    FILENAME = "../images/blue_ball.png"

    def __init__(self) -> None:
        super().__init__()
        self.image_orig = pygame.image.load(Ball.FILENAME).convert_alpha()
        self.scale = 10
        self.image = pygame.transform.scale(self.image_orig, (self.scale, self.scale))
        self.rect: pygame.Rect = self.image.get_rect()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "go" in kwargs.keys():  # Parameter present?§\label{srcMaus0009}§
            if kwargs["go"]:
                self.rect.clamp_ip(Game.INNER_RECT)
                c = self.rect.center  # Store previous center
                self.image: pygame.Surface = pygame.transform.scale(
                    self.image_orig, (self.scale, self.scale)
                )
                self.rect = self.image.get_rect()
                self.rect.center = c  # Reset center

        if "rotate" in kwargs.keys():  # §\label{srcMaus0010}§
            self.rotate(kwargs["rotate"])

        if "scale" in kwargs.keys():  # §\label{srcMaus0011}§
            self.resize(kwargs["scale"])

        if "center" in kwargs.keys():  # §\label{srcMaus0012}§
            self.set_center(kwargs["center"])

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)

    def rotate(self, angle: float) -> None:
        self.image_orig = pygame.transform.rotate(self.image_orig, angle)

    def resize(self, delta: int) -> None:
        self.scale += delta
        if self.scale > Game.INNER_RECT.width:
            self.scale = Game.INNER_RECT.width
        elif self.scale < 5:
            self.scale = 5

    def set_center(self, center: Tuple[int, int]) -> None:
        self.rect.center = center


class Game:
    WINDOW = pygame.Rect((0, 0), (600, 600))
    INNER_RECT = pygame.Rect(100, 100, WINDOW.width - 200, WINDOW.height - 200)
    FPS = 60
    DELTATIME = 1.0 / FPS

    def __init__(self) -> None:
        self.window = pygame.Window(
            size=Game.WINDOW.size, title="Dealing with mouse events"
        )
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.ball = Ball()  # Create ball object§\label{srcMaus0001}§
        self.running = True

    def run(self) -> None:
        time_previous = time()
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(Game.FPS)
            time_current = time()
            Game.DELTATIME = time_current - time_previous
            time_previous = time_current

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
            elif (
                event.type == MOUSEBUTTONDOWN
            ):  # Mouse button pressed§\label{srcMaus0002}§
                if event.button == 1:  # Left§\label{srcMaus0004}§
                    self.ball.update(rotate=90)
                elif event.button == 2:  # Middle§\label{srcMaus0005}§
                    self.running = False
                elif event.button == 3:  # Right§\label{srcMaus0006}§
                    self.ball.update(rotate=-90)
                elif event.button == 4:  # Scroll up§\label{srcMaus0007}§
                    self.ball.update(scale=2)
                elif event.button == 5:  # Scroll down§\label{srcMaus0008}§
                    self.ball.update(scale=-2)

    def update(self):
        newpos = pygame.mouse.get_pos()
        self.ball.update(center=newpos)
        if Game.INNER_RECT.collidepoint(
            pygame.mouse.get_pos()
        ):  # Hide cursor?§\label{srcMaus0003}§
            pygame.mouse.set_visible(False)
        else:
            pygame.mouse.set_visible(True)
        self.ball.update(go=True)

    def draw(self) -> None:
        self.screen.fill((250, 250, 250))
        pygame.draw.rect(self.screen, "red", Game.INNER_RECT, 1)
        self.ball.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
