import pygame


pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')
screen.fill('white')
# 创建surface对象，非图片文字
# surface = pygame.Surface(size=(50, 50), flags=pygame.HWSURFACE, depth=0)
"""
size：表示 Surface 对象的矩形区域大小；
flags：功能标志位，有两个可选参数值 HWSURFACE 和 SPCALPHA，前者代表将创建的 Surface 对象存放于显存中，后者表示让图像的每一个像素都包含一个 alpha  通道
depth：指定像素的颜色深度，默认为自适应模式，由 Pygame 自动调节。
"""

face = pygame.Surface((50, 50), flags=pygame.HWSURFACE)
face.fill(color='green')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.blit(face, (100, 100))
    pygame.display.flip()

pygame.quit()

# 其它参数
"""
pygame.Surface.blit() 	将一个图像（Surface 对象）绘制到另一个图像上
pygame.Surface.convert() 	修改图像（Surface 对象）的像素格式
pygame.Surface.fill()  	使用纯色填充 Surface 对象
pygame.Surface.scroll() 	复制并移动 Surface 对象
pygame.Surface.set_alpha() 	设置整个图像的透明度
pygame.Surface.get_at() 	获取一个像素的颜色值
pygame.Surface.set_at() 	设置一个像素的颜色值
pygame.Surface.get_palette()	获取 Surface 对象 8 位索引的调色板
pygame.Surface.map_rgb()  	将一个 RGBA 颜色转换为映射的颜色值
pygame.Surface.set_clip() 	设置该 Surface 对象的当前剪切区域
pygame.Surface.subsurface()  	根据父对象创建一个新的子 Surface 对象
pygame.Surface.get_offset()	获取子 Surface 对象在父对象中的偏移位置
pygame.Surface.get_size()	获取 Surface 对象的尺寸
"""

