"""
QUIT	用户按下窗口的关闭按钮	none
ATIVEEVENT	Pygame被激活或者隐藏	gain,state
KEYDOWN	键盘按下	unicode、key、mod
KEYUP	键盘放开	key、mod
MOUSEMOTION	鼠标移动  	pos, rel, buttons
MOUSEBUTTONDOWN	鼠标按下 	pos, button
MOUSEBUTTONUP	鼠标放开 	pos, button
JOYAXISMOTION	游戏手柄(Joystick or pad) 移动 	joy, axis, value
JOYBALLMOTION 	游戏球(Joy ball) 移动  	joy, axis, value
JOYHATMOTION	游戏手柄(Joystick) 移动    	joy, axis, value
JOYBUTTONDOWN	游戏手柄按下	joy, button
JOYBUTTONUP	游戏手柄放开    	joy, button
VIDEORESIZE	Pygame窗口缩放  	size, w, h
VIDEOEXPOSE	Pygame窗口部分公开(expose) 	none
USEREVENT	触发一个用户事件  	事件代码

"""
# 处理方法
"""
pygame.event.get()	从事件队列中获取一个事件，并从队列中删除该事件
pygame.event.wait() 	阻塞直至事件发生才会继续执行，若没有事件发生将一直处于阻塞状态
pygame.event.set_blocked() 	控制哪些事件禁止进入队列，如果参数值为None，则表示禁止所有事件进入
pygame.event.set_allowed()  	控制哪些事件允许进入队列
pygame.event.pump() 	调用该方法后，Pygame 会自动处理事件队列
pygame.event.poll() 	会根据实际情形返回一个真实的事件，或者一个None
pygame.event.peek()  	检测某类型事件是否在队列中
pygame.event.clear()	从队列中清除所有的事件
pygame.event.get_blocked() 	检测某一类型的事件是否被禁止进入队列
pygame.event.post()  	放置一个新的事件到队列中
pygame.event.Event()  	创建一个用户自定义的新事件

"""


import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((255, 0, 0))

running = True
while running:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print('鼠标按下')
        if event.button == pygame.BUTTON_LEFT:
            pass
    elif event.type == pygame.MOUSEBUTTONUP:
        print('鼠标弹起')
    elif event.type == pygame.MOUSEMOTION:
        print('鼠标移动')
    elif event.type == pygame.KEYDOWN:
        print('键盘按下')
        if event.key == pygame.K_ESCAPE:
            pass
        elif event.key == pygame.K_q:
            pass
    elif event.type == pygame.KEYUP:
        print('键盘弹起')
    pygame.display.flip()

pygame.quit()
