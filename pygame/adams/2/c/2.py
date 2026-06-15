"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""

import pygame
from random import choice, randint
from typing import Any

WIN_RECT = pygame.Rect(0, 0, 600, 150)
EVENT_BUTTON_PRESSED = pygame.event.custom_type()
EVENT_OVERFLOW = pygame.event.custom_type()


class StartButton(pygame.sprite.Sprite):
    TEXT_COLOR = "black"
    TEXT = ("Stop", "Start")

    def __init__(self, pos, group) -> None:
        super().__init__(group)
        self.font = pygame.font.SysFont(None, 30)
        self.running = False
        self.image = self.font.render(StartButton.TEXT[1], True, StartButton.TEXT_COLOR)
        self.rect: pygame.Rect = self.image.get_rect(topleft=pos)
        self.dirty = False

    def update(self) -> None:
        if self.dirty:
            text = StartButton.TEXT[0] if self.running else StartButton.TEXT[1]
            self.image = self.font.render(text, True, StartButton.TEXT_COLOR)
            self.dirty = False

    def on_click(self, event_in):
        if event_in.button == 1 and self.rect.collidepoint(event_in.pos):
            event_out = pygame.event.Event(EVENT_BUTTON_PRESSED, running=self.running)
            pygame.event.post(event_out)

            self.running = not self.running
            self.dirty = True


class Particle(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((randint(3, 6), randint(3, 6)))
        self.image.fill((0, randint(100, 255), 0))
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = (
            randint(30, WIN_RECT.right - 30),
            randint(30, WIN_RECT.bottom - 30),
        )
        self.speed = randint(50, 100)
        self.direction = pygame.Vector2(choice((-1, 1)), choice((-1, 1)))
        self.freezed = True

    def update(self, td) -> None:
        if not self.freezed:
            self.rect.move_ip(self.speed * self.direction * td)
            if self.rect.left < WIN_RECT.left or self.rect.right > WIN_RECT.right:
                self.direction[0] *= -1
            if self.rect.top < WIN_RECT.top or self.rect.bottom > WIN_RECT.bottom:
                self.direction[1] *= -1
            self.rect.clamp_ip(WIN_RECT)

    def set_freezed(self, freezed: bool):
        self.freezed = freezed


class Box(pygame.sprite.Sprite):
    IMAGE_SIZE = (50, 20)

    def __init__(self, index, pos, group) -> None:
        super().__init__(group)
        self.image: pygame.Surface = pygame.Surface(Box.IMAGE_SIZE)
        self.rect = self.image.get_rect(center=pos)
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
    FPS = 30
    TITLE = "User defined events"
    PARTICLE_COUNT = 100
    BOX_COUNT = 3

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_particles: pygame.sprite.Group[Particle] = pygame.sprite.Group()
        self.generate_particles()
        self.button = StartButton((30, WIN_RECT.bottom - 30), self.all_sprites)
        self.all_boxes = pygame.sprite.Group()
        self.generate_boxes()

    def run(self) -> None:
        while self.handle_events():
            td = self.clock.tick(Game.FPS) / 1000

            self.button.update()
            self.all_particles.update(td)
            self.check_boxcollision()

            self.screen.fill("white")
            self.all_sprites.draw(self.screen)
            self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.button.on_click(event)
            elif event.type == EVENT_BUTTON_PRESSED:
                for particle in self.all_particles:
                    particle.set_freezed(event.running)
            elif event.type == EVENT_OVERFLOW:
                if event.index < Game.BOX_COUNT - 1:
                    self.all_boxes.sprites()[event.index + 1].update(counter="inc")

        return True

    def generate_boxes(self) -> None:
        for i in range(Game.BOX_COUNT):
            self.all_boxes.add(
                Box(
                    i,
                    (WIN_RECT.right - 50 - i * 100, WIN_RECT.centery),
                    self.all_sprites,
                )
            )

    def generate_particles(self) -> None:
        for _ in range(Game.PARTICLE_COUNT):
            self.all_particles.add(Particle(self.all_sprites))

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
