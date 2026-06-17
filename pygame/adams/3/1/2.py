"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""

import random
from time import time
from typing import Any

import pygame
from os import path

WIN_RECT = pygame.Rect(0, 0, 300, 200)
FPS = 30
DELTATIME = 1.0 / FPS
TITLE = "Exploding rocks"
PATH: dict[str, str] = {}
PATH["file"] = path.dirname(path.abspath(__file__))
PATH["image"] = path.join(PATH["file"], "../images")


@staticmethod
def filepath(name: str) -> str:
    return path.join(PATH["file"], name)


@staticmethod
def imagepath(name: str) -> str:
    return path.join(PATH["image"], name)


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


class Animation:

    def __init__(
        self,
        namelist: list[str],
        endless: bool,
        animationtime: int,
        colorkey: tuple[int, int, int] | None = None,
    ) -> None:
        self.images: list[pygame.Surface] = []
        self.endless = endless
        self.timer = Timer(animationtime)
        for filename in namelist:
            if colorkey == None:
                bitmap = pygame.image.load(imagepath(filename)).convert_alpha()
            else:
                bitmap = pygame.image.load(imagepath(filename)).convert()
                bitmap.set_colorkey(colorkey)
            self.images.append(bitmap)
        self.imageindex = -1

    def next(self) -> pygame.Surface:
        if self.timer.is_next_stop_reached():
            self.imageindex += 1
            if self.imageindex >= len(self.images):
                if self.endless:
                    self.imageindex = 0
                else:
                    self.imageindex = len(self.images) - 1
        return self.images[self.imageindex]

    def is_ended(self) -> bool:
        if self.endless:
            return False
        return self.imageindex >= len(self.images) - 1


class Rock(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        i = random.randint(6, 9)
        self.image = pygame.image.load(imagepath(f"felsen-{i}.png")).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx = random.randint(
            self.rect.width, WIN_RECT.width - self.rect.width
        )
        self.rect.centery = random.randint(
            self.rect.height, WIN_RECT.height - self.rect.height
        )
        self.anim = Animation([f"explosion-{i}.png" for i in range(1, 5)], False, 50)
        self.timer_lifetime = Timer(random.randint(100, 2000), False)
        self.bumm = False

    def update(self, *args: Any, **kwargs: Any) -> None:
        if self.timer_lifetime.is_next_stop_reached():
            self.bumm = True
        if self.bumm:
            self.image = self.anim.next()
            c = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = c
        if self.anim.is_ended():
            self.kill()


class ExplosionAnimation(object):

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(size=WIN_RECT.size, title=TITLE)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.all_rocks = pygame.sprite.Group()
        self.timer_newrock = Timer(500)
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
        pygame.quit()

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self) -> None:
        if self.timer_newrock.is_next_stop_reached():
            self.all_rocks.add(Rock())
        self.all_rocks.update()

    def draw(self) -> None:
        self.screen.fill("black")
        self.all_rocks.draw(self.screen)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        ExplosionAnimation().run()
    finally:
        pygame.quit()
        print("Done.")
