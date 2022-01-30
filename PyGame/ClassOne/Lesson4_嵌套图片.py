import pygame
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')

image = pygame.image.load('../Images/IMGS/1.jpg').convert()  # 加速用的
size = image.get_size()  # 获取图像的尺寸
image = pygame.transform.scale(image, (size[0] * 0.7, size[1] * 0.7))  # 缩小，后面是想缩放的尺寸
image.fill((0, 0, 255), rect=(0, 300, 0, 300), special_flags=0)
image.scroll(100, 50)  # 滚动


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(image, (0, 0))
    pygame.display.update()
