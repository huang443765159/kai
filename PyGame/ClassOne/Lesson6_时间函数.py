"""
管理时间和游戏帧数

pygame.time.get_ticks() 	以毫秒为单位获取时间
pygame.time.wait()	使程序暂停一段时间
pygame.time.set_timer()	创建一个定时器，即每隔一段时间，去执行一些动作
pygame.time.Clock()	创建一个时钟对象来帮我们确定游戏要以多大的帧数运行

"""

import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')

t = pygame.time.get_ticks()
t1 = pygame.time.wait(3000)

clock = pygame.time.Clock()

image_surface = pygame.image.load('../Images/IMGS/spriderMan.png').convert()
running = True
while running:
    clock.tick(60)  # 降低CPU占用率
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.blit(image_surface, (0, 0))
        pygame.display.flip()
pygame.quit()
