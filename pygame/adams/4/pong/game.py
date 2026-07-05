"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong game
"""

import pygame
from settings import Settings
from background import Background
from pause import Pause
from help import Help
from paddle import Paddle
from ball import Ball
from score import Score
from events import Events

WIN_RECT = pygame.Rect(0, 0, 1000, 600)
TITLE = "Pong"


class Game:
    FPS = 60

    def __init__(self, window, screen):
        self.window = window
        self.screen = screen
        self.clock = pygame.time.Clock()

        self.background = Background(WIN_RECT)
        self.all_sprites = pygame.sprite.Group()
        self.paddle = {}
        self.paddle["left"] = Paddle("left", self.all_sprites)
        self.paddle["right"] = Paddle("right", self.all_sprites)
        self.ball = Ball(WIN_RECT, self.all_sprites)
        self.score = Score(self.all_sprites)
        self.running = True
        self.pausing = False
        self.helping = False
        self.pause = pygame.sprite.GroupSingle(Pause())
        self.help = Help(WIN_RECT)

    def run(self):
        while self.handle_events():
            dt = self.clock.tick(Game.FPS) / 1000
            self.update(dt)
            self.draw()

    def update(self, dt):
        if not (self.pausing or self.helping):
            self.check_collision()
            for i in Settings.KI.keys():
                if Settings.KI[i]:
                    self.paddlecontroler(self.paddle[i])
            self.all_sprites.update(dt, action="move")

    def draw(self):
        self.background.draw(self.screen)
        self.all_sprites.draw(self.screen)
        if self.pausing:
            self.pause.draw(self.screen)
        elif self.helping:
            self.help.draw(self.screen)
        self.window.flip()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_UP:
                    if not Settings.KI["right"]:
                        self.paddle["right"].update(action="up")
                elif event.key == pygame.K_DOWN:
                    if not Settings.KI["right"]:
                        self.paddle["right"].update(action="down")
                elif event.key == pygame.K_F2:
                    Settings.SOUNDFLAG = not Settings.SOUNDFLAG
                elif event.key == pygame.K_w:
                    if not Settings.KI["left"]:
                        self.paddle["left"].update(action="up")
                elif event.key == pygame.K_s:
                    if not Settings.KI["left"]:
                        self.paddle["left"].update(action="down")
                elif event.key == pygame.K_1:
                    Settings.KI["left"] = not Settings.KI["left"]
                    if not Settings.KI["left"]:
                        self.paddle["left"].update(action="halt")
                elif event.key == pygame.K_2:
                    Settings.KI["right"] = not Settings.KI["right"]
                    if not Settings.KI["right"]:
                        self.paddle["right"].update(action="halt")
                elif event.key == pygame.K_p:
                    if not self.helping:
                        self.pausing = not self.pausing
                elif event.key == pygame.K_h:
                    if not self.pausing:
                        self.helping = not self.helping
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if not Settings.KI["right"]:
                        self.paddle["right"].update(action="halt")
                elif event.key == pygame.K_w or event.key == pygame.K_s:
                    if not Settings.KI["left"]:
                        self.paddle["left"].update(action="halt")
            elif event.type == Events.POINT_FOR:
                self.score.update(player=event.player)
        return True

    def check_collision(self):
        if pygame.sprite.collide_rect(self.ball, self.paddle["left"]):
            self.ball.horizontal_flip()
            self.ball.rect.left = self.paddle["left"].rect.right + 1
        elif pygame.sprite.collide_rect(self.ball, self.paddle["right"]):
            self.ball.horizontal_flip()
            self.ball.rect.right = self.paddle["right"].rect.left - 1

    def paddlecontroler(self, paddle: Paddle) -> None:
        if paddle.rect.centery > self.ball.rect.centery and paddle.rect.top > 10:
            paddle.update(action="up")
        elif (
            paddle.rect.centery < self.ball.rect.centery
            and paddle.rect.bottom < WIN_RECT.bottom - 10
        ):
            paddle.update(action="down")
        else:
            paddle.update(action="halt")


if __name__ == "__main__":
    pygame.init()
    window = pygame.Window(TITLE, WIN_RECT.size)
    screen = window.get_surface()

    Ball.load_resources()

    try:
        Game(window, screen).run()
    finally:
        pygame.quit()
        print("Done.")
