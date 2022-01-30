import sys
import pygame


"""
surface对象：纸张的意思
screen 本质就是一个surface对象，最大的底层画面
text 也是一个surface对象，然后使用screen显示
"""

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')  # 窗口名字
screen.fill((0, 0, 0))  # 屏幕背景颜色，
# 文字对象
font = pygame.font.Font('../Font/华文细黑.ttf', 50)  # 外部字体
text = font.render('你好', True, (255, 0, 0), (0, 0, 0))  # 显示文本，是否平滑，颜色，背景色
text_rect = text.get_rect()  # 对象区域坐标
# text_rect.center = (250, 250)
text_rect.x = 100
text_rect.y = 100
screen.blit(text, text_rect)
# 图片对象
image = pygame.image.load('../Images/IMGS/superman.png').convert()
image_rect = image.get_rect()
image_rect.x = 0
image_rect.y = 200
screen.blit(image, image_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    pygame.display.flip()  # 更新屏幕内容
    # pygame.display.update()  # 更新屏幕
pygame.quit()
sys.exit()
