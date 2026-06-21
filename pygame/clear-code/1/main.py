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
from explosion import Explosion
from player import Player
from score import Score
from settings import WIN_RECT, EVENT_CREATE_METEOR, EVENT_FIRE_LASER


def collisions():
    global running

    collided = lambda left, right: pygame.sprite.collide_mask(left, right) is not None
    if pygame.sprite.spritecollide(player, meteor_sprites, True, collided):
        running = False

    for laser in laser_sprites:
        collided_sprites = pygame.sprite.spritecollide(laser, meteor_sprites, True)
        if collided_sprites:
            laser.kill()
            Explosion(laser.rect.midtop, all_sprites)


# general setup
pygame.init()
TITLE = "Space shooter"
FPS = 60

window = pygame.Window(TITLE, WIN_RECT.size)
screen = window.get_surface()

running = True
clock = pygame.time.Clock()

# resource loading
Star.load_resources()
Laser.load_resources()
Meteor.load_resources()
Player.load_resources()
Explosion.load_resources()
Score.load_resources()

# sprite groups
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

Star.create_field(20, WIN_RECT, all_sprites)
player = Player(all_sprites)
score = Score(WIN_RECT.midbottom)

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
    dt = clock.tick(FPS) / 1000
    if running := handle_events():  # event handling
        all_sprites.update(dt)  # update
        collisions()
        score.update()

        screen.fill("#3a2e3f")  # draw
        all_sprites.draw(screen)
        score.draw(screen)
        window.flip()

pygame.quit()
