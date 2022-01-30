import pygame

"""
pygame.font.init()	初始化字体模块
pygame.font.quit() 	取消初始化字体模块
pygame.font.get_init() 	检查字体模块是否被初始化，返回一个布尔值。
pygame.font.get_default_font() 	获得默认字体的文件名。返回系统中字体的文件名
pygame.font.get_fonts() 	获取所有可使用的字体，返回值是所有可用的字体列表
pygame.font.match_font() 	从系统的字体库中匹配字体文件，返回值是完整的字体文件路径
pygame.font.SysFont() 	从系统的字体库中创建一个 Font 对象
pygame.font.Font()	从一个字体文件创建一个 Font 对象

pygame.font.Font.render() 	该函数创建一个渲染了文本的 Surface 对象
pygame.font.Font.size() 	该函数返回渲染文本所需的尺寸大小，返回值是一个一元组 (width,height)
pygame.font.Font.set_underline() 	是否为文本内容绘制下划线
pygame.font.Font.get_underline() 	检查文本是否绘制了下划线
pygame.font.Font.set_bold() 	启动粗体字渲染
pygame.font.Font.get_bold() 	检查文本是否使用粗体渲染
pygame.font.Font.set_italic() 	启动斜体字渲染
pygame.font.Font.metrics() 	获取字符串中每一个字符的详细参数
pygame.font.Font.get_italic() 	检查文本是否使用斜体渲染
pygame.font.Font.get_linesize() 	获取字体文本的行高
pygame.font.Font.get_height() 	获取字体的高度
pygame.font.Font.get_ascent() 	获取字体顶端到基准线的距离
pygame.font.Font.get_descent() 	获取字体底端到基准线的距离
"""

# 方法
# pygame.font.SysFont(name=, size=, bold=False, italic=False)  名字，大小，黑体， 斜体
# 无法显示中文，只能额外加载中文字体

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill((20, 90, 50))
pygame.display.set_caption('Hello')
font = pygame.font.Font('../Font/微软雅黑粗体.ttf', 50)
text = font.render('刘贺，我是你爹', True, (255, 0, 0))
textRect = text.get_rect()
textRect.center = (250, 250)
screen.blit(text, textRect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()
