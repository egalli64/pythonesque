"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

User defined events
"""
import pygame
from typing import List
from box import Box
from particle import Particle
from button import StartButton

WIN_SIZE = (600, 150)
EVENT_BUTTON_PRESSED = pygame.event.custom_type()
EVENT_OVERFLOW = pygame.event.custom_type()


class Game:
    FPS = 30
    TITLE = "User defined events"
    BACKGROUND_COLOR = "white"
    PARTICLE_COUNT = 100
    BOX_COUNT = 3

    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.viewport = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_particles: pygame.sprite.Group[Particle] = pygame.sprite.Group()
        for _ in range(Game.PARTICLE_COUNT):
            self.all_particles.add(Particle(self.viewport, self.all_sprites))

        self.button = StartButton((30, self.viewport.bottom - 30), self.all_sprites)
        self.all_boxes = pygame.sprite.Group()
        self.boxes: List[Box] = []
        for i in range(Game.BOX_COUNT):
            self.boxes.append(cur := Box(i, self.viewport))
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
                if event.button == pygame.BUTTON_LEFT:
                    self.button.on_click(event.pos)
            elif event.type == EVENT_BUTTON_PRESSED:
                for particle in self.all_particles:
                    particle.set_frozen(event.running)
            elif event.type == EVENT_OVERFLOW:
                if 0 <= event.next < Game.BOX_COUNT:
                    self.boxes[event.next].increase(event.delta)
        return True


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(Game.TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
