"""
A Simple 3D Engine

From: Beginnning Python Games Development with PyGame - https://link.springer.com/book/10.1007/978-1-4842-0970-7
My reviewed version: https://github.com/egalli64/pythonesque/pygame/beginning
"""

import pygame
import math

FPS = 30

SCREEN_SIZE = pygame.Vector2(640, 480)
BACKGROUND_COLOR = (0, 0, 0)
DIAGRAM_COLOR = (50, 255, 50)  # neon green
TEXT_COLOR = (255, 255, 255)  # white
CUBE_SIZE = 300
SPRITE_IMG = "pygame/beginning/img/ball.png"
FONT_SIZE = 24

# Field Of View (in degrees)
MIN_FOV = 30
DEFAULT_FOV = 90
MAX_FOV = 120


def calculate_viewing_distance(fov_deg):
    """
    Given the angular range of the visible scene, calculate the viewing distance
    Both fov (field of view) and screen width are diveded by two, to operate on a rectagle triangle
    """
    return (SCREEN_SIZE.x / 2) / math.tan(math.radians(fov_deg / 2))


def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    font = pygame.font.SysFont(None, FONT_SIZE)
    ball = pygame.image.load(SPRITE_IMG).convert_alpha()

    BALL_SIZE = ball.get_size()
    BALL_CENTER = (BALL_SIZE[0] / 2, BALL_SIZE[1] / 2)

    fov = DEFAULT_FOV
    viewing_distance = calculate_viewing_distance(fov)

    # The 3D points
    points = []
    for x in range(0, CUBE_SIZE + 1, 20):
        edge_x = x == 0 or x == CUBE_SIZE

        for y in range(0, CUBE_SIZE + 1, 20):
            edge_y = y == 0 or y == CUBE_SIZE

            for z in range(0, CUBE_SIZE + 1, 20):
                edge_z = z == 0 or z == CUBE_SIZE

                if sum((edge_x, edge_y, edge_z)) >= 2:
                    point = pygame.Vector3(x, y, z) - pygame.Vector3(CUBE_SIZE / 2)
                    points.append(point)

    # Sort points in z order
    points.sort(key=lambda p: p.z, reverse=True)

    camera_pos = pygame.Vector3(0, 0, -700)
    camera_speed = pygame.Vector3(300)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOR)
        pressed_keys = pygame.key.get_pressed()
        dt = clock.tick(FPS) / 1000

        direction = pygame.Vector3()
        if pressed_keys[pygame.K_LEFT]:
            direction.x = -1
        elif pressed_keys[pygame.K_RIGHT]:
            direction.x = 1

        if pressed_keys[pygame.K_UP]:
            direction.y = 1
        elif pressed_keys[pygame.K_DOWN]:
            direction.y = -1

        if pressed_keys[pygame.K_q]:
            direction.z = 1
        elif pressed_keys[pygame.K_a]:
            direction.z = -1

        if pressed_keys[pygame.K_w]:
            fov = min(MAX_FOV, fov + 1)
            viewing_distance = calculate_viewing_distance(fov)
        elif pressed_keys[pygame.K_s]:
            fov = max(MIN_FOV, fov - 1)
            viewing_distance = calculate_viewing_distance(fov)

        camera_pos += direction * camera_speed * pygame.Vector3(dt)

        # Draw the 3D points
        for point in points:
            x, y, z = point - camera_pos

            if z > 0:
                x = x * viewing_distance / z
                y = -y * viewing_distance / z
                x += SCREEN_SIZE.x / 2
                y += SCREEN_SIZE.y / 2
                screen.blit(ball, (x - BALL_CENTER[0], y - BALL_CENTER[1]))

        # Draw the field of view diagram
        diagram_width = SCREEN_SIZE.x / 4
        diagram_points = []
        diagram_points.append((diagram_width / 2, 100 + viewing_distance / 4))
        diagram_points.append((0, 100))
        diagram_points.append((diagram_width, 100))
        diagram_points.append((diagram_width / 2, 100 + viewing_distance / 4))
        diagram_points.append((diagram_width / 2, 100))
        pygame.draw.lines(screen, DIAGRAM_COLOR, False, diagram_points, 2)

        # Draw the text
        cam_text = font.render(f"camera = {camera_pos}", True, TEXT_COLOR)
        screen.blit(cam_text, (5, 5))
        fov_text = font.render("field of view = %i" % int(fov), True, TEXT_COLOR)
        screen.blit(fov_text, (5, 35))
        d_text = font.render(f"distance = {viewing_distance:.3f}", True, TEXT_COLOR)
        screen.blit(d_text, (5, 65))

        pygame.display.update()


if __name__ == "__main__":
    run()
    print("Done.")
    pygame.quit()
