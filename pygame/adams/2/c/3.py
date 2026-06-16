"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Periodic events
"""

import pygame
from random import choice, randint
from typing import List, override

WIN_RECT = pygame.Rect(0, 0, 600, 150)
EVENT_BUTTON_PRESSED = pygame.event.custom_type()
EVENT_OVERFLOW = pygame.event.custom_type()
EVENT_NEW_PARTICLE = pygame.event.custom_type()


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

    @override
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
    SPEED_RANGE = (50, 100)

    def __init__(self, groups, freezed=True) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((randint(3, 6), randint(3, 6)))
        self.image.fill((0, randint(100, 255), 0))
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.topleft = (
            randint(30, WIN_RECT.right - 30),
            randint(30, WIN_RECT.bottom - 30),
        )
        self.speed = randint(*Particle.SPEED_RANGE)
        self.direction = pygame.Vector2(choice((-1, 1)), choice((-1, 1)))
        self.freezed = freezed

    @override
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
    BACKGROUND_COLOR = "gray"
    VALUE_COLOR = "blue"
    VALUE_POS = (18, 1)

    def __init__(self, exp) -> None:
        super().__init__()
        self.image: pygame.Surface = pygame.Surface(Box.IMAGE_SIZE)
        pos = (WIN_RECT.right - 50 - exp * 100, WIN_RECT.centery)
        self.rect = self.image.get_rect(center=pos)
        self.font = pygame.font.SysFont(None, 30)
        self.value = 0
        self.exp = exp
        self.dirty = True

    @override
    def update(self) -> None:
        if self.dirty:
            self.image.fill(Box.BACKGROUND_COLOR)
            surface = self.font.render(f"{self.value}", False, Box.VALUE_COLOR)
            self.image.blit(surface, Box.VALUE_POS)
            self.dirty = False

    def increase(self, delta):
        self.dirty = True
        current = self.value + delta
        self.value = current % 10
        if x := current // 10:
            event = pygame.event.Event(EVENT_OVERFLOW, next=self.exp + 1, delta=x)
            pygame.event.post(event)


class Game:
    FPS = 30
    TITLE = "User defined events"
    BACKGROUND_COLOR = "white"
    PARTICLE_COUNT = 1000
    BOX_COUNT = 3

    def __init__(self) -> None:
        self.window = pygame.Window(Game.TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_particles: pygame.sprite.Group[Particle] = pygame.sprite.Group()
        for _ in range(Game.PARTICLE_COUNT):
            self.all_particles.add(Particle(self.all_sprites))

        self.button = StartButton((30, WIN_RECT.bottom - 30), self.all_sprites)
        self.all_boxes = pygame.sprite.Group()
        self.boxes: List[Box] = []
        for i in range(Game.BOX_COUNT):
            self.boxes.append(cur := Box(i))
            self.all_boxes.add(cur)
        self.all_sprites.add(self.all_boxes)

    def run(self) -> None:
        while self.handle_events():
            td = self.clock.tick(Game.FPS) / 1000

            self.button.update()
            self.all_particles.update(td)
            self.check_collisions()
            self.all_boxes.update()

            self.screen.fill(Game.BACKGROUND_COLOR)
            self.all_sprites.draw(self.screen)
            self.window.flip()

    def check_collisions(self):
        xs = pygame.sprite.groupcollide(self.all_particles, self.all_boxes, True, False)
        self.boxes[0].increase(len(xs))

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
                self.freezing(event.running)
            elif event.type == EVENT_OVERFLOW:
                if 0 <= event.next < Game.BOX_COUNT:
                    self.boxes[event.next].increase(event.delta)
            elif event.type == EVENT_NEW_PARTICLE:
                Particle((self.all_sprites, self.all_particles), False)
        return True

    def freezing(self, running: bool):
        for particle in self.all_particles:
            particle.set_freezed(running)
        pygame.time.set_timer(EVENT_NEW_PARTICLE, 0 if running else 1000)


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
