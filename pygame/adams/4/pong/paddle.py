"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Pong paddle
"""
import pygame


class Paddle(pygame.sprite.Sprite):
    BORDER_DISTANCE = {"horizontal": 50, "vertical": 10}
    DIRECTION = {"up": -1, "down": 1, "halt": 0}
    SPEED = 300
    RECT = ((0, 0), (15, 60))
    USER_COLOR = "yellow"
    AUTO_COLOR = "deepskyblue2"

    rect: pygame.FRect
    image: pygame.Surface

    @classmethod
    def load_resources(cls):
        cls.user_image = pygame.Surface(Paddle.RECT[1]).convert()
        cls.user_image.fill(Paddle.USER_COLOR)
        cls.auto_image = pygame.Surface(Paddle.RECT[1]).convert()
        cls.auto_image.fill(Paddle.AUTO_COLOR)

    def __init__(self, player: str, viewport: pygame.Rect) -> None:
        super().__init__()

        self.viewport = viewport
        self.auto = False
        self.rect: pygame.FRect = pygame.FRect(Paddle.RECT)
        self.rect.centery = viewport.centery
        self.player = player
        if self.player == "left":
            self.rect.left = Paddle.BORDER_DISTANCE["horizontal"]
        else:
            self.rect.right = viewport.right - Paddle.BORDER_DISTANCE["horizontal"]
        self.direction = Paddle.DIRECTION["halt"]
        self.select_image()

    def toggle_auto(self):
        self.auto = not self.auto
        self.select_image()

    def set_direction(self, direction):
        self.direction = direction

    def update(self, *args, **kwargs):
        if "action" in kwargs.keys():
            if kwargs["action"] == "move":
                self._move()
            elif kwargs["action"] in Paddle.DIRECTION.keys():
                self.direction = Paddle.DIRECTION[kwargs["action"]]
        self.select_image()

    def _move(self) -> None:
        dt = 1 / 60  # TODO: actual dt
        if self.direction != Paddle.DIRECTION["halt"]:
            self.rect.move_ip(0, Paddle.SPEED * self.direction * dt)
            if self.direction == Paddle.DIRECTION["up"]:
                self.rect.top = max(self.rect.top, Paddle.BORDER_DISTANCE["vertical"])
            elif self.direction == Paddle.DIRECTION["down"]:
                self.rect.bottom = min(
                    self.rect.bottom,
                    self.viewport.height - Paddle.BORDER_DISTANCE["vertical"],
                )

    def select_image(self):
        self.image = Paddle.auto_image if self.auto else Paddle.user_image

    def auto_move(self, y_target):
        if self.auto:
            if self.rect.centery > y_target and self.rect.top > 10:
                self.update(action="up")
            elif (
                    self.rect.centery < y_target
                    and self.rect.bottom < self.viewport.bottom - 10
            ):
                self.update(action="down")
            else:
                self.update(action="halt")
