import pygame

"""
self.image	加载要显示的精灵图片，控制图片大小和填充色
self.rect	精灵图片显示在哪个位置
Sprite.update()	刷新精灵图，使其相应效果生效
Sprite.add()	添加精灵图到精灵组中（groups）
Sprite.remove()	从精灵组中删除选中的精灵图
Sprite.kill()	删除精灵组中全部的精灵
Sprite.alive()	判断某个精灵是否属于精灵组
# 方法
pygame.sprite.collide_rect() 	两个精灵之间的矩形检测，即矩形区域是否有交汇，返回一个布尔值。
pygame.sprite.collide_circle()	两个精灵之间的圆形检测，即圆形区域是否有交汇，返回一个布尔值。
pygame.sprite.collide_mask() 	两个精灵之间的像素蒙版检测，更为精准的一种检测方式。
pygame.sprite.spritecollide() 	精灵和精灵组之间的矩形碰撞检测，一个组内的所有精灵会逐一地对另外一个单个精灵进行碰撞检测，返回值是一个列表，包含了发生碰撞的所有精灵。
pygame.sprite.spritecollideany()	精灵和精灵组之间的矩形碰撞检测，上述函数的变体，当发生碰撞时，返回组内的一个精灵，无碰撞发生时，返回 None。
pygame.sprite.groupcollide()	检测在两个组之间发生碰撞的所有精灵，它返回值是一个字典，将第一组中发生碰撞的精灵作为键，第二个组中发生碰撞的精灵作为值。
"""

pygame.init()


class Snake(pygame.sprite.Sprite):

    def __init__(self, filename, location):
        super().__init__()
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()
        self.rect.topleft = location


screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')
image = '../Images/IMGS/1.jpg'
location = (100, 100)
location2 = (100, 250)
snakes = list()
for i in range(2):
    snake = Snake(filename=image, location=location if i == 0 else location2)
    snakes.append(snake)

crash_result = pygame.sprite.collide_rect(snakes[0], snakes[1])
if crash_result:
    print(1)
else:
    print(2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(snakes[0].image, snakes[0].rect)
    screen.blit(snakes[1].image, snakes[1].rect)
    pygame.display.update()
pygame.quit()
