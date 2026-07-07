"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Bubble game

Credits:
 * Fishtank image: https://www.pngwing.com/en/free-png-vadpk
 * Sound: https://www.fesliyanstudios.com/royalty-free-sound-effects-download
"""

from math import sqrt
from time import time
from typing import Dict, Tuple

import pygame
from settings import Settings
from timing import Timer
from background import Background
from message import Message
from bubble import Bubble
from score import Points


class Game:
    """The class Game is main starting class of the game."""

    SOUND_CONTAINER: Dict[str, pygame.mixer.Sound] = {}

    def __init__(self) -> None:
        """Constructor."""
        pygame.init()
        self.window = pygame.Window(size=Settings.WINDOW.size, title=Settings.CAPTION)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()
        Game.SOUND_CONTAINER["bubble"] = pygame.mixer.Sound(
            Settings.get_sound("pop.mp3")
        )
        Game.SOUND_CONTAINER["burst"] = pygame.mixer.Sound(
            Settings.get_sound("burst.mp3")
        )
        Game.SOUND_CONTAINER["clash"] = pygame.mixer.Sound(
            Settings.get_sound("clash.wav")
        )
        self.background = pygame.sprite.GroupSingle(Background())
        self.all_sprites = pygame.sprite.Group()
        self.running = True
        self.pausing = False
        self.msgpause = Message("pause.png")
        self.msgrestart = Message("restart.png")

        self.restart()

    def watch_for_events(self) -> None:
        """Looking for any type of event and poke a reaction."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    self.setpause()
                elif event.key == pygame.K_j:
                    self.do_start = True
                elif event.key == pygame.K_n:
                    self.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.setpause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left
                    self.sting(pygame.mouse.get_pos())

    def draw(self) -> None:
        """Draws all sprite on the screen."""
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)
        # pygame.draw.rect(self.screen, "red", Settings.playground, 2)
        # for b in self.all_bubbles:
        #     pygame.draw.rect(self.screen, "red", b.rect, 2)  # type: ignore
        self.window.flip()

    def update(self) -> None:
        """This method is responsible for the main game logic."""
        if self.do_start:
            self.restart()
        if not self.pausing and self.running:
            if self.check_bubblecollision():
                if not self.restarting:
                    Game.SOUND_CONTAINER["clash"].play()
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
                        Game.SOUND_CONTAINER["bubble"].play()
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
                Game.SOUND_CONTAINER["burst"].play()
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
        """Starting point and main loop of the game."""
        time_previous = time()
        self.running = True
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(Settings.FPS)
            time_current = time()
            Settings.DELTATIME = time_current - time_previous
            time_previous = time_current
        pygame.quit()


def main():
    Game().run()


if __name__ == "__main__":
    main()
