"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

from math import sqrt
from typing import Tuple

import pygame
from settings import Settings
from timing import Timer
from background import Background
from message import Message
from bubble import Bubble
from score import Points
from bubble_factory import BubbleFactory

WIN_RECT = pygame.Rect(0, 0, 1220, 1002)
TITLE = "Bubbles"


class Game:
    FPS = 60
    POP_SOUND_FILE = "sounds/pop.mp3"
    BURST_SOUND_FILE = "sounds/burst.mp3"
    CLASH_SOUND_FILE = "sounds/clash.wav"

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
        self.all_sprites = pygame.sprite.Group()
        self.pausing = False
        self.msgpause = Message("pause.png")
        self.msgrestart = Message("restart.png")

        self.restart()

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
                    self.setpause()
                elif event.key == pygame.K_j:
                    self.do_start = True
                elif event.key == pygame.K_n:
                    return False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.setpause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left
                    self.sting(pygame.mouse.get_pos())
        return True

    def draw(self) -> None:
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.window.flip()

    def update(self, dt) -> None:
        if self.do_start:
            self.restart()
        if not self.pausing:
            if self.check_bubblecollision():
                if not self.restarting:
                    Game.clash_sound.play()
                    self.all_sprites.add(self.msgrestart)
                    self.restarting = True
            else:
                self.all_sprites.update(action="grow")
                self.spawn_bubble()
            self.set_mousecursor()

    def restart(self):
        """Resets all attributes in order to start/restart the game."""
        Settings.POINTS = 0
        self.all_sprites.empty()
        self.all_sprites.add(Points())
        self.bubble_speed = 10
        self.timer_bubble = Timer(500, False)
        self.timer_bubble_speed = Timer(10000, False)
        self.do_start = False
        self.restarting = False

    def setpause(self):
        """Manages the pause mode."""
        if not self.pausing:
            self.all_sprites.add(self.msgpause)
        else:
            self.msgpause.kill()
        self.pausing = not self.pausing

    def spawn_bubble(self) -> None:
        """Spawns a new bubble and checks if there is enough space around the bubble."""
        if self.timer_bubble_speed.is_next_stop_reached():
            if self.bubble_speed < 100:
                self.bubble_speed += 5
        if self.timer_bubble.is_next_stop_reached():
            if len(self.all_sprites) <= Settings.MAX_BUBBLES:
                b = Bubble(self.bubble_speed)
                for _ in range(100):
                    b.randompos()
                    b.radius += Settings.DISTANCE
                    collided = pygame.sprite.spritecollide(
                        b, self.all_sprites, False, pygame.sprite.collide_circle
                    )
                    b.radius -= Settings.DISTANCE
                    if not collided:
                        self.all_sprites.add(b)
                        Game.pop_sound.play()
                        break

    def collidepoint(
        self, point: Tuple[int, int], sprite: pygame.sprite.Sprite
    ) -> bool:
        """Checks if a point is inside or on the edge of the circle.

        Args:
            point (Tuple[int, int]): Coordinates of the point
            sprite (pygame.sprite.Sprite): Sprite with self.radius attribute

        Returns:
            bool: True if the point is inside or on the edge; otherwise False
        """
        if hasattr(sprite, "radius"):
            deltax = point[0] - sprite.rect.centerx  # type: ignore
            deltay = point[1] - sprite.rect.centery  # type: ignore
            return sqrt(deltax * deltax + deltay * deltay) <= sprite.radius  # type: ignore
        return False

    def set_mousecursor(self) -> None:
        """Changes the mouse cursor depending if it is inside or on the edge of a bubble."""
        is_over = False
        pos = pygame.mouse.get_pos()
        for b in self.all_sprites:
            if self.collidepoint(pos, b):
                is_over = True
                break
        if is_over:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    def sting(self, mousepos: Tuple[int, int]) -> None:
        """If the mouse position is inside a bubble, burst it."""
        for bubble in self.all_sprites:
            if self.collidepoint(mousepos, bubble):
                Game.burst_sound.play()
                bubble.update(action="sting")

    def check_bubblecollision(self) -> bool:
        """Checks if two bubbles collide or a bubble the playground border reaches.

        Returns:
            bool: True if bubbles or a bubble collides; otherwise False
        """
        for index1 in range(0, len(self.all_sprites) - 1):
            for index2 in range(index1 + 1, len(self.all_sprites)):
                bubble1 = self.all_sprites.sprites()[index1]
                bubble2 = self.all_sprites.sprites()[index2]
                if (
                    type(bubble1).__name__ == "Bubble"
                    and type(bubble2).__name__ == "Bubble"
                ):
                    if pygame.sprite.collide_circle(bubble1, bubble2):
                        bubble1.update(mode="red")
                        bubble2.update(mode="red")
                        return True
                    if not Settings.PLAYGROUND.contains(bubble1):
                        bubble1.update(mode="red")
                        return True
                    if not Settings.PLAYGROUND.contains(bubble2):
                        bubble2.update(mode="red")
                        return True
        return False

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.update(dt)
            self.draw()


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Game.load_resources()
    Background.load_resources()
    BubbleFactory.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
