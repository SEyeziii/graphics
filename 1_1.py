import pygame
import math
import sys

def draw_line_bresenham(screen, color, p1, p2):
    x1, y1 = map(round, p1)
    x2, y2 = map(round, p2)
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    while True:

        if 0 <= x1 < 800 and 0 <= y1 < 600:
            screen.set_at((x1, y1), color)
        if x1 == x2 and y1 == y2: break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

def rotate_point(p, center, angle_deg):
    rad = math.radians(angle_deg)
    x, y = p[0] - center[0], p[1] - center[1]
    nx = x * math.cos(rad) - y * math.sin(rad)
    ny = x * math.sin(rad) + y * math.cos(rad)
    return nx + center[0], ny + center[1]


print("--- Задача А: Поворот отрезка ---")
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
cx = float(input("Введите x центра поворота: "))
cy = float(input("Введите y центра поворота: "))
angle = float(input("Введите угол поворота (градусы): "))

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Задача А: Поворот отрезка")
screen.fill((255, 255, 255))

p1_rot = rotate_point((x1, y1), (cx, cy), angle)
p2_rot = rotate_point((x2, y2), (cx, cy), angle)


draw_line_bresenham(screen, (200, 200, 200), (x1, y1), (x2, y2))
draw_line_bresenham(screen, (0, 0, 0), p1_rot, p2_rot)
pygame.draw.circle(screen, (255, 0, 0), (int(cx), int(cy)), 3)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()