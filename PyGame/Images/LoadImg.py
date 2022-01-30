import sys
import pygame


pygame.init()
window = pygame.display.set_mode([500, 500])
img = pygame.image.load('IMGS/1.jpg')  # pygame 无法直接播放gif图片，需要存成每一帧然后逐帧加载
rect = img.get_rect()
window.fill((255, 255, 255))  # 设置窗口背景，要在加载图形之前设置，如果在图形之后会覆盖掉图片
window.blit(img, rect)  # 加载图片

while True:
    for event in pygame.event.get():
        if event.type in [pygame.QUIT, pygame.KEYDOWN]:
            sys.exit()
    pygame.display.update()
