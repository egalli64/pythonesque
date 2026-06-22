"""
Master Python by making 5 games - 1: Space shooter

YouTube: https://www.youtube.com/watch?v=8OMghdHP-zs
GitHub: https://github.com/clear-code-projects/5games/tree/main/space%20shooter
Drive: https://drive.google.com/drive/folders/1bUGO9sv5SM3gYO_t9zgifedkQKHUYudO

My version: https://github.com/egalli64/pythonesque/ pygame/clear-code folder
"""

from random import randint
import pygame
from player import Player
from laser import Laser
from meteor import Meteor
from score import Score
from star import Star
from explosion import Explosion

WIN_RECT = pygame.Rect(0, 0, 1280, 720)
TITLE = "Space shooter"


class Game:
    FPS = 60
    EVENT_CREATE_METEOR = pygame.event.custom_type()

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()

        Star.create_field(20, WIN_RECT, self.all_sprites)
        self.player = Player(WIN_RECT.center, self.all_sprites)
        self.score = Score(WIN_RECT.centerx, WIN_RECT.bottom - 50)
        pygame.time.set_timer(Game.EVENT_CREATE_METEOR, 200)

    def run(self):
        while self.handle_events():  # event handling
            dt = self.clock.tick(Game.FPS) / 1000

            self.all_sprites.update(dt)  # update
            self.player.rect.clamp_ip(WIN_RECT)

            self.score.update()  # game logic
            if self.player_collision():
                break
            self.meteor_collisions()

            self.screen.fill("#3a2e3f")  # draw
            self.all_sprites.draw(self.screen)
            self.score.draw(self.screen)
            self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if laser := self.player.request_shoot():
                        self.all_sprites.add(laser)
                        self.lasers.add(laser)
                if event.key == pygame.K_ESCAPE:
                    return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Laser(event.pos, (self.all_sprites, self.lasers))  # cheat fire
            elif event.type == Game.EVENT_CREATE_METEOR:
                x = randint(0, WIN_RECT.width)
                Meteor(x, (self.all_sprites, self.meteors))

        keys = pygame.key.get_pressed()  # for continuous events

        x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
        y = keys[pygame.K_DOWN] - keys[pygame.K_UP]
        self.player.set_direction(x, y)  # arrows determine the player direction

        return True

    def player_collision(self):
        collided = lambda a, b: pygame.sprite.collide_mask(a, b) is not None
        return pygame.sprite.spritecollideany(self.player, self.meteors, collided)

    def meteor_collisions(self):
        for laser in self.lasers:
            collisions = pygame.sprite.spritecollide(laser, self.meteors, True)
            if collisions:
                laser.kill()
                Explosion(laser.rect.midtop, self.all_sprites)


if __name__ == "__main__":
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    # resource loading
    Star.load_resources()
    Laser.load_resources()
    Meteor.load_resources()
    Player.load_resources()
    Explosion.load_resources()
    Score.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.time.wait(500)
        pygame.quit()
        print("Done.")
