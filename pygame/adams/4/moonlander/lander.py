"""
Introduction to Pygame-ce by Ralf Adams - https://github.com/adamsralf/pygame_book/

My version: https://github.com/egalli64/pythonesque/ pygame/adams folder

Moon Lander
"""
import pygame
import config as cfg


class Lander:
    def __init__(self, window: pygame.window.Window, horizont) -> None:
        self.screen = window.get_surface()
        self.viewport = self.screen.get_rect()
        self.horizont = horizont
        self.surface = pygame.Surface((90, 81), pygame.SRCALPHA)
        self.surface_thrusting = pygame.Surface((90, 81), pygame.SRCALPHA)
        self.rect = self.surface.get_frect()
        self.rect.centerx = self.viewport.centerx
        self.rect.top = self.rect.height
        self.create_lander()
        self.create_lander_thrusting()
        self.mode = "landing"
        self.thrusting = False
        self.velocity = 0
        self.fuel_initial = cfg.LEVEL["fair"]
        self.fuel = self.fuel_initial
        self.fuel_consumption = 20
        self.ai = False  # AI flag
        self.create_status_window(window)

    def create_lander(self) -> None:
        # A few abbreviations
        cx = self.rect.width // 2
        cy = self.rect.height // 2
        s = self.rect.width // 2
        sur = self.surface

        # Antenna
        pygame.draw.line(sur, (220, 220, 220), (cx, cy - s // 2), (cx, cy - s // 1.2), 2)
        pygame.draw.circle(sur, (255, 255, 255), (cx, cy - s // 1.2), 3)

        # Upper crew module (narrower)
        pygame.draw.polygon(
            sur, (160, 160, 160),
            [(cx - s // 4, cy - s // 2),
             (cx - s // 6, cy - s // 3),
             (cx + s // 6, cy - s // 3),
             (cx + s // 4, cy - s // 2)]
        )

        # Connector between base and crew module
        conn_color = (160, 160, 160)
        pygame.draw.line(sur, conn_color, (cx - s // 3, cy), (cx - s // 6, cy - s // 3), 2)
        pygame.draw.line(sur, conn_color, (cx, cy), (cx, cy - s // 3), 2)
        pygame.draw.line(sur, conn_color, (cx + s // 3, cy), (cx + s // 6, cy - s // 3), 2)

        # Module base (central capsule, light gray)
        pygame.draw.polygon(
            sur, (200, 200, 200),
            [(cx - s // 3, cy),
             (cx - s // 2, cy + s // 2),
             (cx + s // 2, cy + s // 2),
             (cx + s // 3, cy)]
        )

        # Windows in module
        r = 5
        window_color = (50, 50, 50)
        pygame.draw.circle(sur, window_color, (cx, cy + (s // 4)), r)
        pygame.draw.circle(sur, window_color, (cx - (s // 4), cy + (s // 4)), r)
        pygame.draw.circle(sur, window_color, (cx + (s // 4), cy + (s // 4)), r)

        # Landing legs
        leg_color = (100, 100, 100)
        pygame.draw.line(sur, leg_color, (cx - s // 2, cy + s // 2), (cx - s, cy + s), 3)
        pygame.draw.line(sur, leg_color, (cx + s // 2, cy + s // 2), (cx + s, cy + s), 3)
        pygame.draw.line(sur, leg_color, (cx - s // 4, cy + s // 2), (cx - s // 3, cy + s), 3)
        pygame.draw.line(sur, leg_color, (cx + s // 4, cy + s // 2), (cx + s // 3, cy + s), 3)

        # Feet
        feet_color = (150, 150, 150)
        pygame.draw.circle(sur, feet_color, (cx - s + (r + 2), cy + s - (r + 2)), r - 1)
        pygame.draw.circle(sur, feet_color, (cx + s - (r + 2), cy + s - (r + 2)), r - 1)
        pygame.draw.circle(sur, feet_color, (cx - s // 3 + (r - 4), cy + s - (r + 2)), r - 1)
        pygame.draw.circle(sur, feet_color, (cx + s // 3 - (r - 4), cy + s - (r + 2)), r - 1)

    def create_lander_thrusting(self) -> None:
        # A few abbreviations
        cx = self.rect.width // 2
        cy = self.rect.height // 2
        s = self.rect.width // 2
        sur = self.surface

        # Thruster exhaust
        self.surface_thrusting.blit(sur, (0, 0))
        pygame.draw.polygon(self.surface_thrusting, (255, 140, 0), [
            (cx - 5, cy + s // 2),
            (cx + 5, cy + s // 2),
            (cx, cy + s // 2 + 20)
        ])

    def create_status_window(self, window: pygame.window.Window) -> None:
        self.status_window = pygame.Window(size=(300, 140), title="Status")
        self.status_screen = self.status_window.get_surface()
        top = window.position[1]
        left = window.position[0] + self.viewport.width + 10
        self.status_window.position = (left, top)

    def update(self, *args, **kwargs) -> None:
        if "action" in kwargs.keys():
            if kwargs["action"] == "thrust":
                self.thrust(True)
            elif kwargs["action"] == "unthrust":
                self.thrust(False)
            elif kwargs["action"] == "toggle_ai":
                self.ai = not self.ai
                if not self.ai:
                    self.thrust(False)
            elif kwargs["action"] == "move":
                if self.mode == "landing":
                    if self.ai > 0:
                        self.controller()
                    self.move()
        if "mode" in kwargs.keys():
            self.mode = kwargs["mode"]
            if self.mode in ("landed", "crashed"):
                self.thrust(False)

    def controller(self):
        if self.mode in ("landed", "crashed"):
            self.thrust(False)
            return

        acc = -1 * (cfg.THRUST + cfg.GRAVITY)
        v_save = cfg.SAVE_SPEED_LANDING * 0.5  # 50% buffer
        if self.velocity <= v_save:
            self.thrust(False)
            return

        brake_distance = self.velocity ** 2 / (2 * acc)
        ground_distance = (self.viewport.height - 50) - self.rect.bottom
        self.thrust(ground_distance <= brake_distance)

    def thrust(self, thrusting: bool) -> None:
        self.thrusting = thrusting and self.fuel > 0

    def draw(self) -> None:
        if self.thrusting:
            self.screen.blit(self.surface_thrusting, self.rect.topleft)
        else:
            self.screen.blit(self.surface, self.rect.topleft)
        self.draw_status()

    def draw_status(self) -> None:
        if self.ai:
            self.status_screen.fill("darkgrey")
        else:
            self.status_screen.fill("black")

        # Text output
        h = -1 * (self.rect.bottom - (self.viewport.bottom - self.horizont))
        font = pygame.font.SysFont("Consolas", 14, bold=True)
        labels = "Maximal velocity (m/s):"
        labels += "\nVelocity (m/s):"
        labels += "\nHeight (m):"
        values = f"{cfg.SAVE_SPEED_LANDING / cfg.PIXELS_PER_METER:>7.2f}"
        values += f"\n{self.velocity / cfg.PIXELS_PER_METER:>7.2f}"
        values += f"\n{h / cfg.PIXELS_PER_METER:>7.2f}"
        text_labels = font.render(labels, True, "white")
        text_values = font.render(values, True, "white")
        if self.mode == "landed":
            text_mode = font.render(f"Status: {self.mode}", True, "green")
        elif self.mode == "crashed":
            text_mode = font.render(f"Status: {self.mode}", True, "red")
        else:
            text_mode = font.render(f"Status: {self.mode}", True, "white")
        text_mode_rect = text_mode.get_rect(top=120)
        text_mode_rect.left = self.status_screen.get_rect().centerx - text_mode_rect.centerx
        self.status_screen.blit(text_labels, (5, 10))
        self.status_screen.blit(text_values, (230, 10))
        self.status_screen.blit(text_mode, text_mode_rect.topleft)

        # Bar display
        if self.thrusting:
            pygame.draw.rect(self.status_screen, (255, 140, 0), (5, 90, 290, 20))
        pygame.draw.rect(self.status_screen, "grey", (5, 65, 290, 20))
        ratio = int(290 * self.fuel / self.fuel_initial)
        pygame.draw.rect(self.status_screen, "green", (5, 65, ratio, 20))
        self.status_window.flip()

    def move(self) -> None:
        dt = 1 / 60  # TODO: use actual dt instead
        if self.thrusting and self.fuel > 0:
            self.velocity += cfg.THRUST * dt
            self.fuel -= self.fuel_consumption * dt
            if self.fuel < 0:
                self.thrusting = False
                self.fuel = 0
        self.velocity += cfg.GRAVITY * dt
        self.rect.top += self.velocity * dt
        if self.rect.bottom >= self.viewport.bottom - self.horizont:
            self.rect.bottom = self.viewport.bottom - self.horizont

    def get_velocity(self) -> float:
        return self.velocity

    def is_landed(self) -> bool:
        return self.rect.bottom >= self.viewport.bottom - self.horizont
