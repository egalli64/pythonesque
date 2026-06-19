"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong ball
"""

from random import choice, randint
import pygame
from settings import Settings
from events import Events


class Ball(pygame.sprite.Sprite):
    PLAYER_LEFT = "sounds/left.mp3"
    PLAYER_RIGHT = "sounds/right.mp3"
    BOUNCE = "sounds/bounce.mp3"

    def __init__(self, *groups) -> None:
        super().__init__(*groups)
        self.sounds: dict[str, pygame.mixer.Sound] = {}
        self.sounds["left"] = pygame.mixer.Sound(Ball.PLAYER_LEFT)
        self.sounds["right"] = pygame.mixer.Sound(Ball.PLAYER_RIGHT)
        self.sounds["bounce"] = pygame.mixer.Sound(Ball.BOUNCE)
        self.channel = pygame.mixer.find_channel()
        self.rect: pygame.FRect = pygame.FRect(0, 0, 20, 20)

        self.image = pygame.Surface(self.rect.size).convert()
        self.image.set_colorkey("black")
        pygame.draw.circle(self.image, "green", self.rect.center, self.rect.width // 2)
        self.speed = Settings.WINDOW.width // 3
        self.speedxy = pygame.Vector2()
        self.service()

    def update(self, *args, **kwargs) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "move":
                self.move()
            elif kwargs["action"] == "hflip":
                self.horizontal_flip()
            elif kwargs["action"] == "vflip":
                self.vertical_flip()
            elif kwargs["action"] == "reset":
                self.service()
        return super().update(*args, **kwargs)

    def move(self) -> None:
        dt = 1 / 60 # TODO: actual td
        self.rect.move_ip(self.speedxy * dt)
        if self.rect.top <= 0:
            self.vertical_flip()
            self.rect.top = 0
        elif self.rect.bottom >= Settings.WINDOW.bottom:
            self.vertical_flip()
            self.rect.bottom = Settings.WINDOW.bottom
        elif self.rect.right < 0:
            Events.MYEVENT.player = 2
            pygame.event.post(Events.MYEVENT)
            self.service()
        elif self.rect.left > Settings.WINDOW.right:
            Events.MYEVENT.player = 1
            pygame.event.post(Events.MYEVENT)
            self.service()

    def service(self) -> None:
        self.rect.center = Settings.WINDOW.center
        self.speedxy = pygame.Vector2(choice([-1, 1]), choice([-1, 1])) * self.speed

    def horizontal_flip(self) -> None:
        if Settings.SOUNDFLAG:
            if self.speedxy.x < 0:
                self.channel.set_volume(0.9, 0.1)
                self.channel.play(self.sounds["left"])
            else:
                self.channel.set_volume(0.1, 0.9)
                self.channel.play(self.sounds["right"])
        self.speedxy.x *= -1
        self.respeed()

    def vertical_flip(self) -> None:
        if Settings.SOUNDFLAG:
            rel_pos = self.rect.centerx / Settings.WINDOW.width
            self.channel.set_volume(1.0 - rel_pos, rel_pos)
            self.channel.play(self.sounds["bounce"])
        self.speedxy.y *= -1

    def respeed(self) -> None:
        self.speedxy.x += randint(0, self.speed // 4)
        self.speedxy.y += randint(0, self.speed // 4)
