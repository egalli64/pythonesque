"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Stereo sound
"""

from time import time
from typing import Any, override

import pygame

TILE_SIZE = 32  # square tile, in bit
MAP_SIZE = (25, 7)  # tiles, width, height
WIN_RECT = pygame.Rect(0, 0, TILE_SIZE * MAP_SIZE[0], TILE_SIZE * MAP_SIZE[1])


class Ground:
    IMAGE = "images/background.png"

    def __init__(self) -> None:
        tile = pygame.image.load(Ground.IMAGE).convert()
        assert tile.get_width() == tile.get_height() == TILE_SIZE, "Bad tile size"

        self.background = pygame.Surface(WIN_RECT.size)

        for x in range(0, WIN_RECT.width, tile.get_width()):
            for y in range(0, WIN_RECT.height, tile.get_height()):
                self.background.blit(tile, (x, y))

    def draw(self, screen):
        screen.blit(self.background, (0, 0))


class Tank(pygame.sprite.Sprite):
    IMAGE = "images/tank.png"
    SOUND_DRIVE = "sounds/drive.wav"
    TRANSPARENT_COLOR = "black"
    SPEED = 50

    def __init__(self) -> None:
        super().__init__()
        self.images = {}

        picture = pygame.image.load(Tank.IMAGE).convert()
        picture.set_colorkey(Tank.TRANSPARENT_COLOR)
        self.images["up"] = picture
        self.images["down"] = pygame.transform.rotate(picture, 180)
        self.images["left"] = pygame.transform.rotate(picture, +90)
        self.images["right"] = pygame.transform.rotate(picture, -90)

        self.direction = "right"
        self.image = self.images[self.direction]
        self.rect: pygame.FRect = pygame.FRect(self.image.get_rect())
        assert self.rect.width == self.rect.height == TILE_SIZE, "Bad tile size"

        self.rect.left, self.rect.top = 3 * TILE_SIZE, 2 * TILE_SIZE  # initial position
        self.sound_drive = pygame.mixer.Sound(Tank.SOUND_DRIVE)
        self.channel = pygame.mixer.find_channel()
        if self.channel:
            self.stereo()
            self.channel.play(self.sound_drive, -1)
        self.speed = Tank.SPEED

    def update(self, dt) -> None:
        self.image = self.images[self.direction]
        if self.direction == "up" or self.direction == "left":
            self.speed = -1 * Tank.SPEED
        elif self.direction == "down" or self.direction == "right":
            self.speed = Tank.SPEED
        if self.direction == "up" or self.direction == "down":
            self.rect.move_ip(0, self.speed * dt)
            if self.rect.top <= WIN_RECT.top:
                self.turn("down")
            if self.rect.bottom >= WIN_RECT.bottom:
                self.turn("up")
        elif self.direction == "left" or self.direction == "right":
            self.rect.move_ip(self.speed * dt, 0)
            if self.rect.left <= WIN_RECT.left:
                self.turn("right")
            if self.rect.right >= WIN_RECT.right:
                self.turn("left")
        self.stereo()

    def stereo(self) -> None:
        right = self.rect.centerx / WIN_RECT.width
        self.channel.set_volume(1 - right, right)

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

    @override
    def update(self, dt) -> None:
        self.rect.move_ip(self.speed * dt)
        if not WIN_RECT.contains(self.rect):
            self.kill()


class Game:
    FPS = 30

    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.Window(size=WIN_RECT.size, title="Stereo panning sound")
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.ground = Ground()
        self.tankreference = Tank()
        self.tank = pygame.sprite.GroupSingle(self.tankreference)
        self.all_bullets = pygame.sprite.Group()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_UP:
                    self.tankreference.turn("up")
                elif event.key == pygame.K_DOWN:
                    self.tankreference.turn("down")
                elif event.key == pygame.K_LEFT:
                    self.tankreference.turn("left")
                elif event.key == pygame.K_RIGHT:
                    self.tankreference.turn("right")
                elif event.key == pygame.K_SPACE:
                    self.fire()
        return True

    def fire(self) -> None:
        if self.tankreference.direction in ["up", "down"]:
            print("North/South fire disabled!")
        elif len(self.all_bullets) < 5:
            self.all_bullets.add(Bullet(self.tankreference))

    def run(self) -> None:
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000

            self.tank.update(dt)
            self.all_bullets.update(dt)

            self.ground.draw(self.screen)
            self.tank.draw(self.screen)
            self.all_bullets.draw(self.screen)
            self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        Game().run()
    finally:
        pygame.quit()
        print("Done.")
