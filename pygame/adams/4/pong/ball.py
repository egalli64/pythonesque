"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong ball
"""

from random import choice, uniform
import pygame
from events import Events


class Ball(pygame.sprite.Sprite):
    PLAYER_LEFT = "sounds/left.mp3"
    PLAYER_RIGHT = "sounds/right.mp3"
    BOUNCE = "sounds/bounce.mp3"
    SPEED = 333

    rect: pygame.FRect
    image: pygame.Surface

    @classmethod
    def load_resources(cls):
        cls.left_sound = pygame.mixer.Sound(Ball.PLAYER_LEFT)
        cls.right_sound = pygame.mixer.Sound(Ball.PLAYER_RIGHT)
        cls.bounce_sound = pygame.mixer.Sound(Ball.BOUNCE)

    def __init__(self, viewport: pygame.Rect, *groups) -> None:
        super().__init__(*groups)

        self.viewport = viewport
        self.channel = pygame.mixer.find_channel()
        self.sound_effect = True

        self.rect = pygame.FRect(0, 0, 20, 20)
        self.image = pygame.Surface(self.rect.size).convert()
        self.image.set_colorkey("black")
        pygame.draw.circle(self.image, "green", self.rect.center, self.rect.width // 2)
        self.velocity = pygame.Vector2()
        self.service()

    def toggle_sound_effect(self):
        self.sound_effect = not self.sound_effect

    def update(self, dt, action) -> None:  # TODO: remove action from all update methods
        self.rect.move_ip(self.velocity * dt)
        if self.rect.top <= 0:
            self.vertical_flip()
            self.rect.top = 0
        elif self.rect.bottom >= self.viewport.bottom:
            self.vertical_flip()
            self.rect.bottom = self.viewport.bottom
        elif self.rect.right < 0:
            Events.MY_EVENT.player = 2
            pygame.event.post(Events.MY_EVENT)
            self.service()
        elif self.rect.left > self.viewport.right:
            Events.MY_EVENT.player = 1
            pygame.event.post(Events.MY_EVENT)
            self.service()

    def service(self) -> None:
        self.rect.center = self.viewport.center
        self.velocity = pygame.Vector2(choice([-1, 1]), choice([-1, 1])) * Ball.SPEED

    def horizontal_flip(self) -> None:
        if self.sound_effect:
            if self.velocity.x < 0:
                self.channel.set_volume(0.9, 0.1)
                self.channel.play(Ball.left_sound)
            else:
                self.channel.set_volume(0.1, 0.9)
                self.channel.play(Ball.right_sound)

        self.velocity.x = -1 * (self.velocity.x + uniform(0, Ball.SPEED / 4))
        self.velocity.y += uniform(0, Ball.SPEED / 4)

    def vertical_flip(self) -> None:
        if self.sound_effect:
            rel_pos = self.rect.centerx / self.viewport.width
            self.channel.set_volume(1.0 - rel_pos, rel_pos)
            self.channel.play(Ball.bounce_sound)
        self.velocity.y *= -1
