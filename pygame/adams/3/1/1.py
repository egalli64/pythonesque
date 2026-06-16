"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""

from time import time
from typing import Any

import pygame

from os import path

WINDOW = pygame.Rect(0, 0, 300, 200)
FPS = 30
DELTATIME = 1.0 / FPS
TITLE = "Cat animation"


class Timer:

    def __init__(self, duration: int, with_start: bool = True):
        self.duration = duration
        if with_start:
            self.next = pygame.time.get_ticks()
        else:
            self.next = pygame.time.get_ticks() + self.duration

    def is_next_stop_reached(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False

    def change_duration(self, delta: int = 10):
        self.duration += delta
        if self.duration < 0:
            self.duration = 0


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    def __init__(self) -> None:
        super().__init__()
        self.images: list[pygame.Surface] = []
        for i in range(6):
            bitmap = pygame.image.load(Cat.FILE_TEMPLATE.format(i)).convert()
            bitmap.set_colorkey(Cat.TRANSPARENT_COLOR)
            self.images.append(bitmap)

        self.imageindex = 0
        self.image: pygame.Surface = self.images[self.imageindex]
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = WINDOW.center
        self.animation_time = Timer(100)

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "animation_delta" in kwargs.keys():
            self.change_animation_time(kwargs["animation_delta"])
        if self.animation_time.is_next_stop_reached():
            self.imageindex += 1
            if self.imageindex >= len(self.images):
                self.imageindex = 0
            self.image = self.images[self.imageindex]
            # implement game logic here

    def change_animation_time(self, delta: int) -> None:
        self.animation_time.change_duration(delta)


class CatAnimation:

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WINDOW.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(pygame.font.get_default_font(), 12)
        self.cat = Cat()
        self.cat_group = pygame.sprite.GroupSingle(self.cat)
        self.running = False

    def run(self) -> None:
        time_previous = time()
        self.running = True
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            time_current = time()
            DELTATIME = time_current - time_previous
            time_previous = time_current

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_PLUS:
                    self.cat.update(animation_delta=-10)
                elif event.key == pygame.K_MINUS:
                    self.cat.update(animation_delta=10)

    def update(self) -> None:
        self.cat_group.update()

    def draw(self) -> None:
        self.screen.fill("gray")
        self.cat_group.draw(self.screen)
        text_image = self.font.render(
            f"animation time: {self.cat.animation_time.duration}",
            True,
            "white",
        )
        text_rect = text_image.get_rect()
        text_rect.centerx = WINDOW.centerx
        text_rect.bottom = WINDOW.bottom - 50
        self.screen.blit(text_image, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        CatAnimation().run()
    finally:
        pygame.quit()
        print("Done.")
