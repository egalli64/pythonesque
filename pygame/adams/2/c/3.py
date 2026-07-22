"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Periodic events
"""

import pygame
from typing import List
from common.box import Box
from common.particle import Particle
from common.button import StartButton
from common.custom_event import CustomEvent

WIN_SIZE = (600, 150)
FPS = 30
TITLE = "User defined events"
BACKGROUND_COLOR = "white"
PARTICLE_COUNT = 1000
BOX_COUNT = 3


class Game:
    all_particles: pygame.sprite.Group[Particle]
    boxes: List[Box]

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()

        self.all_sprites = pygame.sprite.Group()
        self.all_particles = pygame.sprite.Group[Particle]()
        for _ in range(PARTICLE_COUNT):
            self.all_particles.add(Particle(self.viewport, self.all_sprites))

        self.button = StartButton((30, self.viewport.bottom - 30), self.all_sprites)
        self.all_boxes = pygame.sprite.Group()
        self.boxes = []
        for i in range(BOX_COUNT):
            self.boxes.append(cur := Box(i, self.viewport))
            self.all_boxes.add(cur)
        self.all_sprites.add(self.all_boxes)
        self.running = True

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            td = clock.tick(FPS) / 1000

            self.handle_events()

            self.button.update()
            self.all_particles.update(td)
            self.check_collisions()
            self.all_boxes.update()

            self.screen.fill(BACKGROUND_COLOR)
            self.all_sprites.draw(self.screen)
            self.window.flip()

    def check_collisions(self):
        xs = pygame.sprite.groupcollide(self.all_particles, self.all_boxes, True, False)
        self.boxes[0].increase(len(xs))

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_SPACE:
                        self.button.toggle_running()
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        self.button.on_click(event.pos)
                case CustomEvent.BUTTON_PRESSED:
                    for particle in self.all_particles:
                        particle.set_frozen(event.running)
                    pygame.time.set_timer(CustomEvent.NEW_PARTICLE, 0 if event.running else 1000)
                case CustomEvent.OVERFLOW:
                    i: int = event.next
                    if 0 <= i < BOX_COUNT:
                        self.boxes[i].increase(event.delta)
                case CustomEvent.NEW_PARTICLE:
                    Particle(self.viewport, (self.all_sprites, self.all_particles), False)


# noinspection DuplicatedCode
if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    Box.load_resources()
    StartButton.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
