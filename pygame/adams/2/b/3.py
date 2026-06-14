"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""

from time import time
from typing import Any

import pygame

WIN_RECT: pygame.Rect = pygame.Rect(0, 0, 800, 224)
FPS = 30
DELTATIME = 1.0 / FPS


class Ground:
    IMAGE = "images/background.png"

    def __init__(self) -> None:
        tile = pygame.image.load(Ground.IMAGE).convert()

        self.background = pygame.Surface(WIN_RECT.size)

        for x in range(0, WIN_RECT.width, tile.get_width()):
            for y in range(0, WIN_RECT.height, tile.get_height()):
                self.background.blit(tile, (x, y))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class Tank(pygame.sprite.Sprite):
    IMAGE = "images/tank.png"

    def __init__(self) -> None:
        super().__init__()
        self.images = {}

        picture = pygame.image.load(Tank.IMAGE).convert()
        picture.set_colorkey("black")
        self.images["up"] = picture
        self.images["down"] = pygame.transform.rotate(picture, 180)
        self.images["left"] = pygame.transform.rotate(picture, +90)
        self.images["right"] = pygame.transform.rotate(picture, -90)

        self.direction = "right"
        self.image = self.images[self.direction]
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        self.rect.left, self.rect.top = 3 * self.rect.width, 2 * self.rect.height
        self.sound_drive = pygame.mixer.Sound("sounds/drive.wav")
        self.channel = pygame.mixer.find_channel()
        if self.channel:
            self.stereo()
            self.channel.play(self.sound_drive, -1)
        self.speed = 50

    def update(self, *args: Any, **kwargs: Any) -> None:
        if "go" in kwargs.keys():
            if kwargs["go"]:
                self.image = self.images[self.direction]
                if self.direction == "up" or self.direction == "left":
                    self.speed = -50
                elif self.direction == "down" or self.direction == "right":
                    self.speed = 50
                if self.direction == "up" or self.direction == "down":
                    self.rect.move_ip(0, self.speed * DELTATIME)
                    if self.rect.top <= WIN_RECT.top:
                        self.turn("down")
                    if self.rect.bottom >= WIN_RECT.bottom:
                        self.turn("up")
                elif self.direction == "left" or self.direction == "right":
                    self.rect.move_ip(self.speed * DELTATIME, 0)
                    if self.rect.left <= WIN_RECT.left:
                        self.turn("right")
                    if self.rect.right >= WIN_RECT.right:
                        self.turn("left")
                self.stereo()
        if "turn" in kwargs.keys():
            self.turn(kwargs["turn"])

    def stereo(self) -> None:
        volume_right = self.rect.centerx / WIN_RECT.width
        volume_left = 1 - volume_right
        self.channel.set_volume(volume_left, volume_right)

    def turn(self, direction: str) -> None:
        self.direction = direction


class Bullet(pygame.sprite.Sprite):
    SOUND_FIRE = None

    def __init__(self, tank: Tank) -> None:
        assert tank.direction not in ("up", "down"), "Unexpected fire direction"
        super().__init__()

        bulletspeed = 300
        directions = {
            "left": pygame.Vector2(-bulletspeed, 0),
            "right": pygame.Vector2(bulletspeed, 0),
        }
        fullfilename = f"images/bullet_{tank.direction}.png"
        self.image = pygame.image.load(fullfilename).convert()
        self.image.set_colorkey("black")
        self.rect: pygame.Rect = self.image.get_rect()
        self.direction = tank.direction
        self.rect.center = tank.rect.center
        self.speed = directions[tank.direction]

        if Bullet.SOUND_FIRE == None:
            Bullet.SOUND_FIRE = pygame.mixer.Sound("sounds/fire.wav")
        volume_right = self.rect.centerx / WIN_RECT.width
        volume_left = 1 - volume_right
        self.channel: pygame.mixer.Channel = pygame.mixer.find_channel()
        if self.channel:
            self.channel.set_volume(volume_left, volume_right)
            self.channel.play(Bullet.SOUND_FIRE)

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.move_ip(self.speed * DELTATIME)
        if not WIN_RECT.contains(self.rect):
            self.kill()


class Game:

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(size=WIN_RECT.size, title="Stereo panning sound")
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.ground = Ground()
        self.tankreference = Tank()
        self.tank = pygame.sprite.GroupSingle(self.tankreference)
        self.all_bullets = pygame.sprite.Group()
        self.running = True

    def watch_for_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_UP:
                    self.tank.update(turn="up")
                elif event.key == pygame.K_DOWN:
                    self.tank.update(turn="down")
                elif event.key == pygame.K_LEFT:
                    self.tank.update(turn="left")
                elif event.key == pygame.K_RIGHT:
                    self.tank.update(turn="right")
                elif event.key == pygame.K_SPACE:
                    self.fire()

    def fire(self) -> None:
        if self.tankreference.direction in ["up", "down"]:
            print("North/South fire disabled!")
        elif len(self.all_bullets) < 5:
            self.all_bullets.add(Bullet(self.tankreference))

    def draw(self) -> None:
        self.ground.draw(self.screen)
        self.tank.draw(self.screen)
        self.all_bullets.draw(self.screen)
        self.window.flip()

    def update(self) -> None:
        self.tank.update(go=True)
        self.all_bullets.update()

    def run(self) -> None:
        time_previous = time()
        self.running = True
        while self.running:
            self.watch_for_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            time_current = time()
            DELTATIME = time_current - time_previous
            time_previous = time_current
        pygame.quit()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
