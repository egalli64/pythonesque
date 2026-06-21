"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

import pygame
from random import randint
from star import Star
from laser import Laser
from meteor import Meteor
from player import Player
from settings import WIN_RECT, EVENT_CREATE_METEOR, EVENT_FIRE_LASER


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

window = pygame.Window(TITLE, WIN_RECT.size)
screen = window.get_surface()

running = True
clock = pygame.time.Clock()

# resource loading
Star.load_resources()
Laser.load_resources()
Meteor.load_resources()
Player.load_resources()
meteor_surf = pygame.image.load("images/meteor.png").convert_alpha()
font = pygame.font.Font(None, 40)
explosion_frames = [
    pygame.image.load(f"images/explosion/{i}.png").convert_alpha() for i in range(21)
]

explosion_sound = pygame.mixer.Sound("audio/explosion.wav")

# sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
Star.create_field(20, WIN_RECT, all_sprites)
player = Player(all_sprites)

pygame.time.set_timer(EVENT_CREATE_METEOR, 200)


def handle_events() -> bool:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            player.request_shoot()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Laser(event.pos, (all_sprites, laser_sprites))  # cheat fire
        elif event.type == EVENT_CREATE_METEOR:
            Meteor(randint(0, WIN_RECT.width), (all_sprites, meteor_sprites))
        elif event.type == EVENT_FIRE_LASER:
            Laser(event.pos, (all_sprites, laser_sprites))

    keys = pygame.key.get_pressed()  # for continuous events

    x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
    y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
    player.set_direction(x, y)  # arrows determine the player direction

    return True


while running:
    dt = clock.tick() / 1000
    if running := handle_events():
        all_sprites.update(dt)
        collisions()

        screen.fill("#3a2e3f")
        display_score()
        all_sprites.draw(screen)
        window.flip()

pygame.quit()
