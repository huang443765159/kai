# 主要指rect的运用
# rect = pygame.Rect(left, top, width, height)

import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')

image = pygame.image.load('../Images/IMGS/spriderMan.png')
rect1 = pygame.Rect(50, 50, 100, 100)
print(rect1.x, rect1.y)
print(rect1.bottom, rect1.right)
print(rect1.midtop, rect1.midright)
print(rect1.size)
image_rect = image.subsurface(rect1)  # 从原图像截一个方块
rect2 = image_rect.get_rect()
rect1.left = 50  # 设置

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(image_rect, rect1)
    pygame.display.update()

pygame.quit()

# Rect 方法
"""
pygame.Rect.copy()	复制矩形
pygame.Rect.move()	移动矩形区域，接受一个列表参数
pygame.Rect.move_ip()	移动矩形（无返回）, 图像移动，
pygame.Rect.inflate()	增大或缩小矩形大小
pygame.Rect.clamp()	将矩形移到另一个矩形内
pygame.Rect.union()	返回一个两个矩形合并后的矩形。
pygame.Rect.fit()	按纵横比调整矩形的大小或移动矩形。
pygame.Rect.contains()	测试一个矩形是否在另一个矩形内
pygame.Rect.collidepoint() 	测试点是否在矩形内
pygame.Rect.colliderect()	测试两个矩形是否重叠
"""
