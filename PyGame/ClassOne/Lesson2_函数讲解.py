import pygame


info = pygame.display.Info()  # 获取现有屏幕的大小
w, h = info.current_w, info.current_h
screen = pygame.display.set_mode(size=(w, h), flags=pygame.FULLSCREEN)

"""
pygame.FULLSCREEN	创建一个全屏窗口。
pygame.HWSURFACE	创建一个硬件加速窗口，必须和 FULLSCREEN 同时使用。
pygame.OPENGL	创建一个 OPENGL 渲染窗口。
pygame.RESIZABLE	创建一个可以改变大小的窗口。
pygame.DOUBLEBUF	创建一个双缓冲区窗口，建议在 HWSURFACE 或者 OPENGL 时使用。
pygame.NOFRAME	创建一个没有边框的窗口。
"""

# 显示其它对象
screen.blit(source=0, dest=0, area=None, special_flags=0)
"""
source：表示要粘贴的 Surface 对象。
dest：主窗口中的一个标识的坐标位置，可以接受一个 (x,y) 元组，或者 (x,y,width,height) 元组，也可以是一个 Rect 对象；
area：接受一个 Rect 对象，默认为 None，如果提供该参数则相当于抠图操作，即在屏幕的指定区域显示想要的内容；
special_flags：可选参数，它是 Pygame.1.8 版本新增的功能，用于指定对应位置颜色的混合方式，
参数值有 BLEND_RGBA_ADD、BLEND_SUB 等。如果不提供该参数的情况下，默认使用 source 的颜色覆盖 screen 的颜色。
"""

# 其它参数
"""
pygame.display.get_surface()	获取当前显示的 Surface 对象。
pygame.display.flip()	更新整个待显示的 Surface 对象到屏幕上。
pygame.display.update()	更新部分软件界面显示。
pygame.display.Info()	产生一个 VideoInfo 对象，包含了显示界面的相关信息。
pygame.display.set_icon()	设置左上角的游戏图标，图标尺寸大小为 32*32。
pygame.display.iconify()	将显示的主窗口即 Surface 对象最小化，或者隐藏。
pygame.display.get_active()	当前显示界面显示在屏幕上时返回 True，如果窗口被隐藏和最小化则返回 False。
"""