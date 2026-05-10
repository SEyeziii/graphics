import pygame
import math
import sys
from pygame import gfxdraw

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
YELLOW = (255, 200, 0)
RED = (255, 0, 0)


def create_star_relative(r1, r2, points):
    #звездa в относительных координатах (центр в 0,0)
    vertices = []
    for i in range(points * 2):
        angle = math.pi * 2 * i / (points * 2) - math.pi / 2
        r = r1 if i % 2 == 0 else r2
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        vertices.append((x, y))
    return vertices

#oтносительные координаты звезды (центр в 0,0)
star_relative = create_star_relative(150, 60, 5)

angle = 0
rotate_center = (WIDTH // 2, HEIGHT // 2)  # центр поворота

def rotate_point(x, y, cx, cy, angle_deg):
    #поворот точки
    rad = math.radians(angle_deg)
    dx = x - cx
    dy = y - cy
    new_x = dx * math.cos(rad) - dy * math.sin(rad) + cx
    new_y = dx * math.sin(rad) + dy * math.cos(rad) + cy
    return (new_x, new_y)


def draw_smooth_polygon(points):
    #сглаженный многоугольник
    if not points:
        return
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        gfxdraw.line(screen, int(x1), int(y1), int(x2), int(y2), YELLOW)

running = True
rotation_speed = 0.5
frame = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rotate_center = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEWHEEL:
            angle += event.y * 5

    angle += rotation_speed
    if angle >= 360:
        angle -= 360

    #сначала переносим в центр, потом поворачиваем
    rotated_star = []
    for dx, dy in star_relative:
        #добавляем центр звезды
        star_center = rotate_center

        world_x = star_center[0] + dx
        world_y = star_center[1] + dy
        #относительно центра вращения
        final_x, final_y = rotate_point(world_x, world_y, rotate_center[0], rotate_center[1], angle)
        rotated_star.append((final_x, final_y))


    draw_smooth_polygon(rotated_star)

    pygame.draw.circle(screen, RED, rotate_center, 8, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()