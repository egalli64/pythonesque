"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

from typing import Tuple

import pygame
from settings import Settings
from background import Background
from message import Message
from bubble import Bubble
from score import Score
from bubble_factory import BubbleFactory

WIN_RECT = pygame.Rect(0, 0, 1220, 1002)
TITLE = "Bubbles"


class Game:
    terminated: bool
    bubble_speed: int
    bubbles: pygame.sprite.Group[Bubble]

    FPS = 60
    POP_SOUND_FILE = "sounds/pop.mp3"
    BURST_SOUND_FILE = "sounds/burst.mp3"
    CLASH_SOUND_FILE = "sounds/clash.wav"

    SPAWN_BUBBLE_EVENT = pygame.event.custom_type()
    SPAWN_DELTA_TIME = 500
    SPEED_UP_EVENT = pygame.event.custom_type()
    SPEED_UP_DELTA_TIME = 10 * 1000
    BUBBLE_SPEED_RANGE = (10, 100)
    BUBBLE_SPEED_DELTA = 5

    @classmethod
    def load_resources(cls):
        cls.pop_sound = pygame.mixer.Sound(Game.POP_SOUND_FILE)
        cls.burst_sound = pygame.mixer.Sound(Game.BURST_SOUND_FILE)
        cls.clash_sound = pygame.mixer.Sound(Game.CLASH_SOUND_FILE)

    def __init__(self, window, screen) -> None:
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.background = Background(WIN_RECT)
        self.message = pygame.sprite.GroupSingle()
        self.bubbles = pygame.sprite.Group[Bubble]()
        self.paused = False
        self.m_pause = Message("pause.png")
        self.m_restart = Message("restart.png")
        self.score = Score()

        self.reset()

    def handle_events(self) -> bool:
        """Looking for any type of event and poke a reaction."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    self.set_pause()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.set_pause()

            if self.terminated:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_j:
                        self.reset()
                    elif event.key == pygame.K_n:
                        return False

            if not self.paused and not self.terminated:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.sting(pygame.mouse.get_pos())
                elif event.type == Game.SPAWN_BUBBLE_EVENT:
                    self.spawn_bubble()
                elif event.type == Game.SPEED_UP_EVENT:
                    if self.bubble_speed < Game.BUBBLE_SPEED_RANGE[1]:
                        self.bubble_speed += Game.BUBBLE_SPEED_DELTA

        return True

    def draw(self) -> None:
        self.background.draw(self.screen)
        self.score.draw(self.screen)
        self.message.draw(self.screen)
        self.bubbles.draw(self.screen)
        self.window.flip()

    def update(self, dt) -> None:
        if not self.paused:
            self.score.update(None)
            if self.check_collision():
                if not self.terminated:
                    Game.clash_sound.play()
                    self.message.add(self.m_restart)
                    self.terminated = True
            else:
                self.bubbles.update(dt)
            self.set_cursor()

    def reset(self):
        self.score.change_score()
        self.message.empty()
        self.bubbles.empty()
        self.bubble_speed = Game.BUBBLE_SPEED_RANGE[0]
        self.terminated = False

        pygame.time.set_timer(Game.SPAWN_BUBBLE_EVENT, Game.SPAWN_DELTA_TIME)
        pygame.time.set_timer(Game.SPEED_UP_EVENT, Game.SPEED_UP_DELTA_TIME)

    def set_pause(self):
        self.paused = not self.paused

        if self.paused:
            self.message.add(self.m_pause)
            pygame.time.set_timer(Game.SPEED_UP_EVENT, 0)
            pygame.time.set_timer(Game.SPAWN_BUBBLE_EVENT, 0)
        else:
            self.m_pause.kill()
            pygame.time.set_timer(Game.SPAWN_BUBBLE_EVENT, Game.SPAWN_DELTA_TIME)
            pygame.time.set_timer(Game.SPEED_UP_EVENT, Game.SPEED_UP_DELTA_TIME)

    def spawn_bubble(self) -> None:
        if len(self.bubbles) <= Settings.MAX_BUBBLES:
            bubble = Bubble(self.bubble_speed)
            for _ in range(100):
                bubble.randompos()
                bubble.radius += Settings.DISTANCE
                collided = pygame.sprite.spritecollide(
                    bubble, self.bubbles, False, pygame.sprite.collide_circle
                )
                bubble.radius -= Settings.DISTANCE
                if not collided:
                    self.bubbles.add(bubble)
                    Game.pop_sound.play()
                    break

    def set_cursor(self) -> None:
        pos = pygame.mouse.get_pos()
        for bubble in self.bubbles:
            if bubble.contains(pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                break
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    def sting(self, pos: Tuple[int, int]) -> None:
        for bubble in self.bubbles:
            if bubble.contains(pos):
                Game.burst_sound.play()
                self.score.change_score(bubble.pop())

    def check_collision(self) -> bool:
        for bubble in self.bubbles:
            if not Settings.PLAYGROUND.contains(bubble):
                bubble.offending()
                return True

        collisions = pygame.sprite.groupcollide(self.bubbles, self.bubbles, False, False, pygame.sprite.collide_circle)
        for left in collisions:
            for right in collisions[left]:
                if left != right:
                    left.offending()
                    right.offending()
                    return True

        return False

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            if not self.paused and not self.terminated:
                self.update(dt)
            self.draw()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_RECT.size)
    pg_screen = pg_window.get_surface()

    Game.load_resources()
    Background.load_resources()
    BubbleFactory.load_resources()
    Score.load_resources()

    try:
        Game(pg_window, pg_screen).run()
    finally:
        pygame.quit()
        print("Done.")
