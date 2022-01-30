import pygame
from random import randint


"""
pygame.event.MOUSEMOTION鼠标移动事件
event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
event.rel 鼠标相对运动距离(X,Y)，相对于上次事件
event.buttons 鼠标按钮初始状态(0,0,0)，分别对应(左键,滑轮,右键)，移动过程中点击那个键，相应位置变会为1
pygame.event.MOUSEBUTTONUP鼠标键释放事件
event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
event.button 鼠标释放键编号（整数）左键为1，按下滚动轮2、右键为3
pygame.event.MOUSEBUTTONDOWN 鼠标键按下事件
event.pos 相对于窗口左上角，鼠标的当前坐标值(x,y)
event.button 鼠标按下键编号（整数），左键为1，按下滚动轮2、右键为3，向前滚动滑轮4、向后滚动滑轮5
"""

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')

running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = event.pos
        pygame.draw.circle(screen, (255, 255, 0), (mx, my), 50)
        pygame.display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pass
    elif event.type == pygame.MOUSEMOTION:
        mx, my = event.pos
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        pygame.draw.circle(screen, (r, g, b), (mx, my), 50)
        pygame.display.update()
pygame.quit()