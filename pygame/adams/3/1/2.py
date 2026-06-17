"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Exploding rocks
"""

import random
from time import time
from typing import Any

import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 200)
FPS = 30
DELTATIME = 1.0 / FPS
TITLE = "Exploding rocks"


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
    def __init__(self, namelist: list[str], delta: int) -> None:
        self.images: list[pygame.Surface] = []
        self.timer = Timer(delta)
        for filename in namelist:
            bitmap = pygame.image.load(filename).convert_alpha()
            self.images.append(bitmap)
        self.i = 0

    def next(self) -> pygame.Surface:
        if self.timer.is_next_stop_reached():
            self.i += 1
        return self.images[self.i] if self.i < len(self.images) else self.images[0]

    def is_ended(self) -> bool:
        return self.i == len(self.images)


class Rock(pygame.sprite.Sprite):
    FILENAME = "../images/rock.png"
    EXPLOSION_TEMPLATE = "../images/explosion-{:d}.png"

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Rock.FILENAME).convert_alpha()
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.centerx = random.randint(
            self.rect.width, WIN_RECT.width - self.rect.width
        )
        self.rect.centery = random.randint(
            self.rect.height, WIN_RECT.height - self.rect.height
        )
        explosions = [Rock.EXPLOSION_TEMPLATE.format(i) for i in range(1, 5)]
        self.anim = Animation(explosions, 100)
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
