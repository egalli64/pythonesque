"""
My PyGame CE tutorial: https://github.com/egalli64/pythonesque/ pygame/my folder

User input: Keyboard Continuous Polling
"""
import pygame

TITLE = "Keyboard Continuous Polling"
WIN_SIZE = (400, 200)
FPS = 60
BACKGROUND_COLOR = "whitesmoke"

PLAYER_INITIAL_POS = (200.0, 150.0)
PLAYER_RADIUS = 20
PLAYER_SPEED = 4  # pixel for frame
PLAYER_INTERNAL_COLOR = "dodgerblue"
PLAYER_BORDER_COLOR = "darkblue"


class Game:
    def __init__(self, window: pygame.Window, screen: pygame.Surface) -> None:
        self.window = window
        self.screen = screen
        self.running = True

        self.pos = pygame.Vector2(PLAYER_INITIAL_POS)
        self.direction = pygame.Vector2(0, 0)

    def run(self) -> None:
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(FPS)

            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            self.running = False

        # Continuous polling
        keys = pygame.key.get_pressed()

        self.direction.update(0, 0)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y += 1

    def update(self) -> None:
        if self.direction:
            self.direction.normalize_ip()
            self.pos += self.direction * PLAYER_SPEED

            # clamp the target to the window
            self.pos.x = max(PLAYER_RADIUS, min(self.pos.x, self.window.size[0] - PLAYER_RADIUS))
            self.pos.y = max(PLAYER_RADIUS, min(self.pos.y, self.window.size[1] - PLAYER_RADIUS))

    def draw(self) -> None:
        self.screen.fill(BACKGROUND_COLOR)

        pygame.draw.circle(self.screen, PLAYER_INTERNAL_COLOR, self.pos, PLAYER_RADIUS)
        pygame.draw.circle(self.screen, PLAYER_BORDER_COLOR, self.pos, PLAYER_RADIUS, width=1)

        self.window.flip()


if __name__ == "__main__":
    pygame.init()
    main_window = pygame.Window(TITLE, WIN_SIZE)
    main_surface = main_window.get_surface()

    try:
        Game(main_window, main_surface).run()
    finally:
        pygame.quit()
