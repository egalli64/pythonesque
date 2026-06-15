"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""

import pygame
from random import choice, randint
from time import time
from typing import Any, Tuple

WINDOW = pygame.Rect(0, 0, 600, 150)
FPS = 30
DELTATIME = 1.0 / FPS
STARTNOFPARTICLES = 999
NOFBOXES = 3
BOXWIDTH = 50

EVENT_BUTTON_PRESSED = pygame.event.custom_type()
EVENT_OVERFLOW = pygame.event.custom_type()


class Button(pygame.sprite.Sprite):

    def __init__(self, text, position, group) -> None:
        super().__init__(group)
        self.font = pygame.font.SysFont(None, 30)
        self.centerxy = (WINDOW.centerx, self.font.get_height() // 2)
        self.text = text
        self.image = self.font.render(self.text, True, "black")
        self.rect: pygame.Rect = self.image.get_rect(topleft=(position))

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "pressed":
                evt = pygame.event.Event(EVENT_BUTTON_PRESSED, text=self.text)
                pygame.event.post(evt)
        return super().update(*args, **kwargs)


class Particle(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(*group)
        self.image = pygame.Surface((randint(3, 6), randint(3, 6)))
        self.image.fill((0, randint(100, 255), 0))
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = (
            randint(30, WINDOW.right - 30),
            randint(30, WINDOW.bottom - 30),
        )
        self.speed = randint(100, 400)
        self.direction = pygame.Vector2(choice((-1, 1)), choice((-1, 1)))
        self.halted = False

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "move":
                if not self.halted:
                    self._move()
            elif kwargs["action"] == "Start":
                self.halted = False
            elif kwargs["action"] == "Stop":
                self.halted = True

    def _move(self) -> None:
        self.rect.move_ip(self.speed * self.direction * DELTATIME)
        if self.rect.left < WINDOW.left or self.rect.right > WINDOW.right:
            self.direction[0] *= -1
        if self.rect.top < WINDOW.top or self.rect.bottom > WINDOW.bottom:
            self.direction[1] *= -1
        self.rect.clamp_ip(WINDOW)


class Box(pygame.sprite.Sprite):
    def __init__(self, index, position, group) -> None:
        super().__init__(group)
        self.image: pygame.Surface = pygame.Surface((BOXWIDTH, 20))
        self.rect = self.image.get_rect(center=position)
        self.font = pygame.font.SysFont(None, 30)
        self.counter = 0
        self.index = index
        self.fill()

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "counter" in kwargs.keys():
            if kwargs["counter"] == "inc":
                self.counter += 1
                if self.counter == 10:
                    evt = pygame.event.Event(EVENT_OVERFLOW, index=self.index)
                    pygame.event.post(evt)
                    self.counter = 0
                self.fill()
        return super().update(*args, **kwargs)

    def fill(self) -> None:
        self.image.fill("gray")
        number = self.font.render(f"{self.counter}", False, "Blue")
        self.image.blit(number, (18, 1))


class Game:
    def __init__(self) -> None:
        self.window = pygame.Window("Event (1)", WINDOW.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.all_particles = pygame.sprite.Group()
        self.generate_particles(STARTNOFPARTICLES)
        self.all_buttons = pygame.sprite.Group()
        pos: Tuple[int, int] = (30, WINDOW.bottom - 30)
        start = Button("Start", pos, self.all_sprites)
        self.all_buttons.add(start)
        stop = Button("Stop", (100, WINDOW.bottom - 30), self.all_sprites)
        self.all_buttons.add(stop)
        self.all_boxes = pygame.sprite.Group()
        self.generate_boxes(NOFBOXES)
        self.running = True

    def run(self) -> None:
        time_previous = time()
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.check_button_pressed(event.pos)
            elif event.type == EVENT_BUTTON_PRESSED:
                self.all_particles.update(action=event.text)
            elif event.type == EVENT_OVERFLOW:
                if event.index < NOFBOXES - 1:
                    self.all_boxes.sprites()[event.index + 1].update(counter="inc")

    def update(self):
        self.all_buttons.update()
        self.all_particles.update(action="move")
        self.check_boxcollision()

    def draw(self) -> None:
        self.screen.fill("white")
        self.all_sprites.draw(self.screen)
        self.window.flip()

    def generate_boxes(self, number: int) -> None:
        for i in range(number):
            self.all_boxes.add(
                Box(
                    i,
                    (WINDOW.right - 50 - i * 100, WINDOW.centery),
                    self.all_sprites,
                )
            )

    def generate_particles(self, number: int) -> None:
        for i in range(number):
            self.all_particles.add(Particle(self.all_sprites))

    def check_button_pressed(self, position: Tuple[int]) -> None:
        for b in self.all_buttons.sprites():
            if b.rect.collidepoint(position):
                b.update(action="pressed")

    def check_boxcollision(self) -> None:
        c = pygame.sprite.groupcollide(self.all_particles, self.all_boxes, True, False)
        for _ in c:
            self.all_boxes.sprites()[0].update(counter="inc")


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
