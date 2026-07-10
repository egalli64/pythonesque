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


class MyEvents:
    LANDED = pygame.event.custom_type()
    CRASHED = pygame.event.custom_type()


class Game:
    sky: Sky

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(size=cfg.WINDOW.size, title="MyMoonlander", position=pygame.WINDOWPOS_CENTERED)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        self.landing = True

    def run(self) -> None:
        self.restart()
        time_previous = time()
        while self.running:
            self.watch_for_events()
            self.update()
            if self.running:
                self.draw()
            self.clock.tick(cfg.FPS)
            time_current = time()
            cfg.DELTATIME = time_current - time_previous
            time_previous = time_current
        pygame.quit()

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.WINDOWCLOSE:
                self.running = False
                event.window.destroy()
            elif event.type == MyEvents.LANDED:
                self.landing = False
                self.lander.update(mode="landed", velocity=event.volocity)
            elif event.type == MyEvents.CRASHED:
                self.landing = False
                self.lander.update(mode="crashed", velocity=event.volocity)
            elif event.type == pygame.KEYDOWN:
                if self.landing:
                    if event.key == pygame.K_SPACE:
                        self.lander.update(action="thrust")
                    elif event.key == pygame.K_h:
                        self.lander.update(action="toggle_ai")
                else:
                    if event.key == pygame.K_q:
                        self.running = False
                    elif event.key == pygame.K_r:
                        self.restart()
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.lander.update(action="unthrust")

    def update(self) -> None:
        self.sky.update()
        self.lander.update(action="move")
        self.ckeck_landing()

    def draw(self) -> None:
        self.sky.draw(self.screen)
        self.moon.draw()
        self.lander.draw()
        if not self.landing:
            self.question.draw()
        self.window.flip()

    def restart(self) -> None:
        self.landing = True
        self.sky = Sky()
        self.moon = Moon(self.screen)
        self.lander = Lander(self.window)
        self.question = Question(self.screen)
        self.running = True

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


def main():
    Game().run()


if __name__ == "__main__":
    main()
