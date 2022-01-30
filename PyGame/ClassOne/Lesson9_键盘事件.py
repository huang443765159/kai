import pygame


"""
K_BACKSPACE	退格键（Backspace）
K_TAB	制表键（Tab）
K_CLEAR	清除键（Clear）
K_RETURN	回车键（Enter）
K_PAUSE	暂停键（Pause）
K_ESCAPE	退出键（Escape）
K_SPACE	空格键（Space）
K_0...K_9	0...9
K_a...Kz	a...z
K_DELETE	删除键（delete）
K_KP0...K_KP9	0（小键盘）...9（小键盘）
K_F1...K_F15	F1...F15
K_UP	向上箭头（up arrow）
K_DOWN	向下箭头（down arrow）
K_RIGHT	向右箭头（right arrow）
K_LEFT	向左箭头（left arrow）
KMOD_ALT	同时按下Alt键
"""
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello')
image = pygame.image.load('../Images/IMGS/spriderMan.png').convert()
image_rect = image.get_rect()

running = True
while running:
    site = [0, 0]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                site[1] -= 8
            elif event.key == pygame.K_DOWN:
                site[1] += 8
            elif event.key == pygame.K_LEFT:
                site[0] -= 8
            elif event.key == pygame.K_RIGHT:
                site[0] += 8
    image_rect = image_rect.move(site)
    screen.fill('white')
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
