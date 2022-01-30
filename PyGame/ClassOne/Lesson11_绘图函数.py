import pygame
from math import pi


"""
pygame.draw.rect() 	绘制矩形
pygame.draw.polygon() 	绘制多边形
pygame.draw.circle() 	根据圆心和半径绘制圆形
pygame.draw.ellipse() 	绘制一个椭圆形
pygame.draw.arc() 	绘制弧线（挥着椭圆的一部分）
pygame.draw.line() 	绘制线段（直线）
pygame.draw.lines() 	绘制多条连续的线段
pygame.draw.aaline() 	绘制一条平滑的线段（抗锯齿）
pygame.draw.aalines() 	绘制多条连续的线段
"""
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.line(screen, (0, 255, 100), (0, 0), (500, 500), 3)
    pygame.draw.lines(screen, (0, 0, 255), True, [(0, 10), (50, 50), (259, 230), (99, 100)], 1)
    pygame.draw.rect(screen, (100, 0, 0), [200, 200, 300, 300], 2)
    pygame.draw.arc(screen, (100, 255, 0), (210, 75, 150, 125), 0, pi / 2, 2)
    pygame.display.flip()

pygame.quit()
