"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

List of installed fonts (to be reviewed for better understanding)
"""

import pygame

WIN_RECT = pygame.Rect(0, 0, 900, 800)
WIN_POS = (10, 50)
TITLE = "List of installed fonts"
FPS = 15


class TextSprite(pygame.sprite.Sprite):
    DEFAULT_COLOR = (0, 0, 0)
    DEFAULT_SIZE = 18
    DEFAULT_TEXT = "abcdefghijklmnopqrstxyzßöäü0123456789"

    def __init__(self, fontname: str) -> None:
        super().__init__()
        self.fontname = fontname
        self.size = TextSprite.DEFAULT_SIZE
        self.color: list[int] = list(TextSprite.DEFAULT_COLOR)
        self.font = pygame.font.Font(pygame.font.match_font(self.fontname), self.size)
        self.text = f"{self.fontname}: {self.DEFAULT_TEXT}"
        self.render()

    def render(self) -> None:
        self.image: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect: pygame.Rect = self.image.get_rect()

    def change_size(self, step: int = 1) -> None:
        self.size += step
        self.font = pygame.font.Font(pygame.font.match_font(self.fontname), self.size)

    def change_color(self, delta: list[int]) -> None:
        for i in range(3):
            self.color[i] = (self.color[i] + delta[i]) % 256

    def update(self) -> None:
        self.render()


class BigImage(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.offset = WIN_RECT.copy()
        self.image_total = pygame.Surface((width, height))
        self.image_total.fill("white")
        self.update(0)

    def update(self, delta: int) -> None:
        if self.offset.top + delta >= 0:
            it_rect = self.image_total.get_rect()
            if self.offset.bottom + delta <= it_rect.height:
                self.offset.move_ip(0, delta)
            else:
                self.offset.bottom = it_rect.height
        else:
            self.offset.top = 0

        self.image = self.image_total.subsurface(self.offset)
        self.rect = self.image.get_rect()


def main():
    pygame.init()

    window = pygame.Window(TITLE, WIN_RECT.size, WIN_POS)
    screen = window.get_surface()
    clock = pygame.time.Clock()

    fonts = pygame.font.get_fonts()
    print(fonts)

    list_of_fontsprites = pygame.sprite.Group()
    height = 0
    width = 0
    for name in sorted(fonts):
        try:
            t = TextSprite(name)
            t.rect.top = height
            height += t.rect.height
            width = t.rect.width if t.rect.width > width else width
            list_of_fontsprites.add(t)
        except OSError as err:
            print(f"OS error {err}")
        except pygame.error as perr:
            print(f"Pygame error: {perr} with font {name}")

    big_image = BigImage(width, height)
    bigimage_group = pygame.sprite.GroupSingle(big_image)
    list_of_fontsprites.draw(big_image.image_total)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    bigimage_group.update(-WIN_RECT.height // 2)
                if event.key == pygame.K_DOWN:
                    bigimage_group.update(WIN_RECT.height // 2)

        bigimage_group.draw(screen)
        window.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()
