import pygame
import math
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

center_x, center_y = WIDTH // 2, HEIGHT // 2
triangle = [
    (0, -100),
    (-80, 60),
    (80, 60)
]

global_triangle = []
angle = 0
rotate_center = (center_x, center_y)  # центр поворота


def rotate_point(x, y, cx, cy, angle_deg):
    ##поворот точки на угол вокруг центра
    rad = math.radians(angle_deg)
    dx = x - cx
    dy = y - cy
    new_x = dx * math.cos(rad) - dy * math.sin(rad) + cx
    new_y = dx * math.sin(rad) + dy * math.cos(rad) + cy
    return (int(new_x), int(new_y))


def bresenham_line(x1, y1, x2, y2):
    ##aлгоритм Брезенхема
    points = []
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    x, y = x1, y1
    while True:
        points.append((x, y))
        if x == x2 and y == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy
    return points


def draw_triangle():
    for i in range(3):
        x1, y1 = global_triangle[i]
        x2, y2 = global_triangle[(i + 1) % 3]
        for px, py in bresenham_line(x1, y1, x2, y2):
            screen.set_at((px, py), GREEN)


running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #центр поворота
            if event.button == 1:
                rotate_center = pygame.mouse.get_pos()
                print(f"Новый центр: {rotate_center}")
        if event.type == pygame.MOUSEWHEEL:
            #поворот
            angle += event.y * 5
            print(f"Угол: {angle}°")


    global_triangle = []
    for x, y in triangle:
        px, py = rotate_point(center_x + x, center_y + y,
                              rotate_center[0], rotate_center[1], angle)
        global_triangle.append((px, py))

    draw_triangle()

    pygame.draw.circle(screen, RED, rotate_center, 8, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()