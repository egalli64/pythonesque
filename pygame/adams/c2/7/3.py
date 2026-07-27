"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

List of installed fonts (to be reviewed for better understanding)
"""
import pygame

WIN_SIZE = (900, 800)
WIN_POS = (10, 50)
TITLE = "List of installed fonts"
FPS = 15


class TextSprite(pygame.sprite.Sprite):
    DEFAULT_COLOR = (0, 0, 0)
    DEFAULT_SIZE = 18
    DEFAULT_TEXT = "abcdefghijklmnopqrstxyz+-*/0123456789"

    image: pygame.Surface
    rect: pygame.Rect

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

    def update(self) -> None:
        self.render()


class BigImage(pygame.sprite.Sprite):
    image: pygame.Surface
    rect: pygame.Rect

    def __init__(self, width: int, height: int, viewport: pygame.Rect):
        super().__init__()

        self.offset = viewport.copy()
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


def main(window: pygame.Window, screen: pygame.Surface):
    viewport = screen.get_rect()
    fonts = pygame.font.get_fonts()
    print(f"There are {len(fonts)} available fonts")

    texts = pygame.sprite.Group()
    height = 0
    width = 0
    for name in sorted(fonts):
        try:
            text = TextSprite(name)
            text.rect.top = height
            height += text.rect.height
            width = text.rect.width if text.rect.width > width else width
            texts.add(text)
        except OSError as err:
            print(f"OS error {err}")
        except pygame.error as perr:
            print(f"Pygame error: {perr} with font {name}")

    big_image = BigImage(width, height, viewport)
    bi_group = pygame.sprite.GroupSingle(big_image)
    texts.draw(big_image.image_total)

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_UP:
                    bi_group.update(-WIN_SIZE[1] // 2)
                if event.key == pygame.K_DOWN:
                    bi_group.update(WIN_SIZE[1] // 2)

        bi_group.draw(screen)
        window.flip()


if __name__ == "__main__":
    pygame.init()
    pg_window = pygame.Window(TITLE, WIN_SIZE)
    pg_screen = pg_window.get_surface()

    try:
        main(pg_window, pg_screen)
    finally:
        pygame.quit()
        print("Done.")
