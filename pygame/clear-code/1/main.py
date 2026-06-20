"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect: pygame.FRect = self.image.get_frect(center=(WIN_RECT.center))
        self.direction = pygame.Vector2()
        self.speed = 300

        # cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400

        # mask
        self.mask = pygame.mask.from_surface(self.image)

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = (
            self.direction.normalize() if self.direction else self.direction
        )
        self.rect.center += self.direction * self.speed * dt

        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surf, self.rect.midtop, (all_sprites, laser_sprites))
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        self.laser_timer()


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        center = (randint(0, WIN_RECT.w), randint(0, WIN_RECT.h))
        self.rect = self.image.get_rect(center=center)


class Laser(pygame.sprite.Sprite):
    SPEED = 400

    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect: pygame.FRect = self.image.get_frect(midbottom=pos)

    def update(self, dt):
        self.rect.centery -= Laser.SPEED * dt
        if self.rect.bottom < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, x, groups):
        super().__init__(groups)
        self.original_surf = surf
        self.image = surf
        self.rect: pygame.FRect = self.image.get_frect(centerx=x)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 500)
        self.rotation_speed = randint(40, 80)
        self.rotation = 0

    def update(self, dt):
        self.rect.center += self.direction * self.speed * dt
        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()
        self.rotation += self.rotation_speed * dt
        self.image = pygame.transform.rotozoom(self.original_surf, self.rotation, 1)
        self.rect = self.image.get_frect(center=self.rect.center)


class Explosion(pygame.sprite.Sprite):
    DURATION_MODIFIER = 20  # decrease it for longer lasting explosion

    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames = frames
        self.fractional_index = 0.0
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        self.fractional_index += dt * Explosion.DURATION_MODIFIER
        if self.fractional_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.fractional_index)]


def collisions():
    global running

    collided = lambda left, right: pygame.sprite.collide_mask(left, right) is not None
    if pygame.sprite.spritecollide(player, meteor_sprites, True, collided):
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            Explosion(explosion_frames, laser.rect.midtop, all_sprites)
            explosion_sound.play()


def display_score():
    score = pygame.time.get_ticks() // 100
    surf = font.render(str(score), True, "gray94")
    rect = surf.get_frect(midbottom=(WIN_RECT.w / 2, WIN_RECT.h - 50))
    screen.blit(surf, rect)
    pygame.draw.rect(screen, "gray94", rect.inflate(20, 10).move(0, -2), 4, 10)


# general setup
pygame.init()
TITLE = "Space shooter"
WIN_RECT = pygame.Rect(0, 0, 1280, 720)

window = pygame.Window(TITLE, WIN_RECT.size)
screen = window.get_surface()

running = True
clock = pygame.time.Clock()

# import
star_surf = pygame.image.load("images/star.png").convert_alpha()
meteor_surf = pygame.image.load("images/meteor.png").convert_alpha()
laser_surf = pygame.image.load("images/laser.png").convert_alpha()
font = pygame.font.Font(None, 40)
explosion_frames = [
    pygame.image.load(f"images/explosion/{i}.png").convert_alpha() for i in range(21)
]

laser_sound = pygame.mixer.Sound("audio/laser.wav")
laser_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound("audio/explosion.wav")

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)

CREATE_METEOR_EVENT = pygame.event.custom_type()
pygame.time.set_timer(CREATE_METEOR_EVENT, 200)

while running:
    dt = clock.tick() / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == CREATE_METEOR_EVENT:
            x = randint(0, WIN_RECT.width)
            Meteor(meteor_surf, x, (all_sprites, meteor_sprites))

    all_sprites.update(dt)
    collisions()

    screen.fill("#3a2e3f")
    display_score()
    all_sprites.draw(screen)
    window.flip()

pygame.quit()

# 37:55
