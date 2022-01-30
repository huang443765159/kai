import pygame
from pygame.locals import *

# 图像方法
"""
pygame.transform.scale()	将图片缩放至指定的大小，并返回一个新的 Surface 对象。
pygame.transform.rotate()	将图片旋转至指定的角度。
pygame.transform.rotozoom()	以角度旋转图像，同时将图像缩小或放大至指定的倍数
"""
pygame.init()
screen = pygame.display.set_mode((2000, 2000))
pygame.display.set_caption('Hello')
screen.fill('white')

image = pygame.image.load('../Images/IMGS/superman.png').convert()
image_size = image.get_size()
image_scale = pygame.transform.scale(image, (image_size[0] * 0.7, image_size[1] * 0.7))
image_rotate = pygame.transform.rotate(image, 45)
image_rotezoom = pygame.transform.rotozoom(image, 180, 0.5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(image, (0, 0))
    screen.blit(image_scale, (500, 500))
    screen.blit(image_rotate, (1000, 500))
    screen.blit(image_rotezoom, (500, 1000))
    pygame.display.update()
pygame.quit()
