import pygame


pygame.init()
info = pygame.display.Info()  # 获取屏幕分辨率
window = pygame.display.set_mode([info.current_w, info.current_h], pygame.FULLSCREEN)  # 全屏幕代码
# window = pygame.display.set_mode([500, 500])  # 非全屏

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        window.fill((255, 0, 0))
        pygame.display.flip()
        pygame.display.update()
pygame.quit()
