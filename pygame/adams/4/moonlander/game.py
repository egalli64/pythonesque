"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
from time import time

import config as cfg
import pygame

from sky import Sky
from moon import Moon
from lander import Lander
from question import Question

WIN_RECT = pygame.Rect(0, 0, 600, 800)
TITLE = "Moon Lander"


class MyEvents:
    LANDED = pygame.event.custom_type()
    CRASHED = pygame.event.custom_type()


class Game:
    sky: Sky

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.active = True

    def run(self) -> None:
        self.restart()
        clock = pygame.time.Clock()
        time_previous = time()
        while self.handle_events():
            self.update()
            self.draw()
            clock.tick(cfg.FPS)
            time_current = time()
            cfg.DELTATIME = time_current - time_previous
            time_previous = time_current

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.WINDOWCLOSE:
                return False
            elif event.type == MyEvents.LANDED:
                self.active = False
                self.lander.update(mode="landed", velocity=event.volocity)
            elif event.type == MyEvents.CRASHED:
                self.active = False
                self.lander.update(mode="crashed", velocity=event.volocity)
            elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_SPACE:
                        self.lander.update(action="thrust")
                    elif event.key == pygame.K_h:
                        self.lander.update(action="toggle_ai")
                else:
                    if event.key == pygame.K_q:
                        return False
                    elif event.key == pygame.K_r:
                        self.restart()
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.lander.update(action="unthrust")

        return True

    def update(self) -> None:
        self.sky.update()
        self.lander.update(action="move")
        self.ckeck_landing()

    def draw(self) -> None:
        self.sky.draw(self.screen)
        self.moon.draw()
        self.lander.draw()
        if not self.active:
            self.question.draw()
        self.window.flip()

    def restart(self) -> None:
        self.active = True
        self.sky = Sky()
        self.moon = Moon(self.screen)
        self.lander = Lander(self.window)
        self.question = Question(self.screen)

    def ckeck_landing(self) -> None:
        velocity = self.lander.get_velocity()
        if self.lander.is_landed():
            velocity = self.lander.get_velocity()
            if velocity > cfg.SAVE_SPEED_LANDING:
                evt = pygame.event.Event(MyEvents.CRASHED, volocity=velocity)
                pygame.event.post(evt)
            else:
                evt = pygame.event.Event(MyEvents.LANDED, volocity=velocity)
                pygame.event.post(evt)


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_RECT.size, pygame.WINDOWPOS_CENTERED)
    pg_screen = pg_window.get_surface()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
