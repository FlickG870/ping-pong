import pygame


pygame.init()

clock = pygame.time.Clock()
rungame = True
FPS = 60
winSize = [700, 500] 

pygame.display.set_caption('Пинг-Понг')
win = pygame.display.set_mode(winSize)

while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    win.fill([3, 177, 252])
    pygame.display.update()
    clock.tick(FPS) 