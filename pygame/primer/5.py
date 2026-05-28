"""
Sound Effects

From: A Primer on Pygame Game Programming - https://realpython.com/pygame-a-primer/
My reviewed version: https://github.com/egalli64/pythonesque/pygame/primer
"""

from typing import override
import pygame
import random

FPS = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_CENTER = SCREEN_SIZE / 2
SCREEN_RECT = (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

BACKGROUND_COLOR = (135, 206, 250)  # light sky blue

BACKGROUND_MUSIC = "pygame/primer/sound/Apoxode_-_Electric_1.mp3"
UP_SOUND = "pygame/primer/sound/Rising_putter.ogg"
DOWN_SOUND = "pygame/primer/sound/Falling_putter.ogg"
COLLISION_SOUND = "pygame/primer/sound/Collision.ogg"

PLAYER_IMAGE = "pygame/primer/img/jet.png"
PLAYER_TRANSPARENT_COLOR = (255, 255, 255)  # white to transparent
PLAYER_SPEED = 200

ENEMY_IMAGE = "pygame/primer/img/missile.png"
ENEMY_TRANSPARENT_COLOR = (255, 255, 255)  # white to transparent
ENEMY_MIN_SPEED = 100
ENEMY_MAX_SPEED = 200

CLOUD_IMAGE = "pygame/primer/img/cloud.png"
CLOUD_TRANSPARENT_COLOR = (0, 0, 0)  # black to transparent
CLOUD_SPEED = 100


class Player(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(PLAYER_IMAGE).convert()  # type: ignore
        self.image.set_colorkey(PLAYER_TRANSPARENT_COLOR, pygame.RLEACCEL)

        self.rect = self.image.get_rect(center=SCREEN_CENTER)  # type: ignore

    @override
    def update(self, pressed_keys, dt):
        """
        Move in place the sprite based on the keys pressed

        Keep it inside the screen area
        """
        delta_pixel = PLAYER_SPEED * dt
        dpos = pygame.Vector2()

        if pressed_keys[pygame.K_RIGHT]:
            dpos.x += delta_pixel
        if pressed_keys[pygame.K_DOWN]:
            move_down_sound.play()
            dpos.y += delta_pixel
        if pressed_keys[pygame.K_LEFT]:
            dpos.x -= delta_pixel
        if pressed_keys[pygame.K_UP]:
            move_up_sound.play()
            dpos.y -= delta_pixel

        self.rect.move_ip(dpos)
        self.rect.clamp_ip(SCREEN_RECT)


class Enemy(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(ENEMY_IMAGE).convert()  # type: ignore
        self.image.set_colorkey(ENEMY_TRANSPARENT_COLOR, pygame.RLEACCEL)

        x = random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
        y = random.randint(0, SCREEN_HEIGHT)
        self.rect = self.image.get_rect(center=(x, y))  # type: ignore

        self.speed = random.randint(ENEMY_MIN_SPEED, ENEMY_MAX_SPEED)

    @override
    def update(self, dt):
        """
        Move the sprite based on speed

        Remove the sprite from each group when it passes the left edge of the screen
        """
        dx = -self.speed * dt
        self.rect.move_ip(dx, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load(CLOUD_IMAGE).convert()  # type: ignore
        self.image.set_colorkey(CLOUD_TRANSPARENT_COLOR, pygame.RLEACCEL)

        x = random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100)
        y = random.randint(0, SCREEN_HEIGHT)
        self.rect = self.image.get_rect(center=(x, y))  # type: ignore

    @override
    def update(self, dt):
        """
        Move the sprite based on speed

        Remove the sprite from each group when it passes the left edge of the screen
        """
        self.rect.move_ip(-CLOUD_SPEED * dt, 0)
        if self.rect.right < 0:
            self.kill()


pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

ADD_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADD_ENEMY, 250)

ADD_CLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADD_CLOUD, 1000)

player = Player()
clock = pygame.time.Clock()

enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Load and play our background music
# Sound source: http://ccmixter.org/files/Apoxode/59262
# License: https://creativecommons.org/licenses/by/3.0/
pygame.mixer.music.load(BACKGROUND_MUSIC)
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.1)

# Load all our sound files
# Sound sources: Jon Fincher
move_up_sound = pygame.mixer.Sound(UP_SOUND)
move_down_sound = pygame.mixer.Sound(DOWN_SOUND)
collision_sound = pygame.mixer.Sound(COLLISION_SOUND)

# Set the base volume for all sounds
move_up_sound.set_volume(0.1)
move_down_sound.set_volume(0.1)
collision_sound.set_volume(0.1)

running = True
while running:
    dt = clock.tick(30) / 1000

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.QUIT:
            running = False
        elif event.type == ADD_ENEMY:
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)
        elif event.type == ADD_CLOUD:
            cloud = Cloud()
            clouds.add(cloud)
            all_sprites.add(cloud)

    pressed_keys = pygame.key.get_pressed()

    clouds.update(dt)
    enemies.update(dt)
    player.update(pressed_keys, dt)

    screen.fill(BACKGROUND_COLOR)

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()

        # Stop any moving sounds and play the collision sound
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()

        running = False

    pygame.display.flip()

# ensure no sound is pending
while pygame.mixer.get_busy():
    pygame.time.delay(100)

# we're done, stop and quit the mixer
pygame.mixer.music.stop()
pygame.mixer.quit()

print("Done.")
pygame.quit()
