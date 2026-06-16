"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

A running cat
"""

from typing import override
import pygame

WIN_RECT = pygame.Rect(0, 0, 300, 200)
TITLE = "Cat animation"


class Timer:
    MIN_DURATION = 10

    def __init__(self, duration: int):
        self.duration = duration
        self.next = pygame.time.get_ticks() + duration

    def is_time(self) -> bool:
        if pygame.time.get_ticks() > self.next:
            self.next = pygame.time.get_ticks() + self.duration
            return True
        return False

    def change_duration(self, delta: int):
        self.duration = max(Timer.MIN_DURATION, self.duration + delta)


class Cat(pygame.sprite.Sprite):
    FILE_TEMPLATE = "../images/cat-{:d}.bmp"
    TRANSPARENT_COLOR = "black"

    def __init__(self) -> None:
        super().__init__()
        self.images: list[pygame.Surface] = []
        for i in range(6):
            bitmap = pygame.image.load(Cat.FILE_TEMPLATE.format(i)).convert()
            bitmap.set_colorkey(Cat.TRANSPARENT_COLOR)
            self.images.append(bitmap)

        self.imageindex = 0
        self.image: pygame.Surface = self.images[self.imageindex]
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.center = WIN_RECT.center
        self.timer = Timer(100)

    @override
    def update(self) -> None:
        if self.timer.is_time():
            self.imageindex += 1
            if self.imageindex >= len(self.images):
                self.imageindex = 0
            self.image = self.images[self.imageindex]

    def change_timing(self, delta: int) -> None:
        self.timer.change_duration(delta)


class CatAnimation:
    FPS = 30

    def __init__(self) -> None:
        self.window = pygame.Window(TITLE, WIN_RECT.size)
        self.screen = self.window.get_surface()
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 12)
        self.cat = Cat()
        self.cat_group = pygame.sprite.GroupSingle(self.cat)

    def run(self) -> None:
        while self.handle_events():
            self.clock.tick(CatAnimation.FPS)

            self.cat.update()
            self.draw()

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                elif event.key == pygame.K_PLUS:
                    self.cat.change_timing(-10)
                elif event.key == pygame.K_MINUS:
                    self.cat.change_timing(10)
        return True

    def update(self) -> None:
        self.cat_group.update()

    def draw(self) -> None:
        self.screen.fill("gray")
        self.cat_group.draw(self.screen)
        text_image = self.font.render(
            f"animation time: {self.cat.timer.duration}",
            True,
            "white",
        )
        text_rect = text_image.get_rect()
        text_rect.centerx = WIN_RECT.centerx
        text_rect.bottom = WIN_RECT.bottom - 50
        self.screen.blit(text_image, text_rect)
        self.window.flip()


if __name__ == "__main__":
    pygame.init()

    try:
        CatAnimation().run()
    finally:
        pygame.quit()
        print("Done.")
