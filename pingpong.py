import pygame


pygame.init()

clock = pygame.time.Clock()
rungame = True
FPS = 60
winSize = [700, 500] 

pygame.display.set_caption('Пинг-Понг')
win = pygame.display.set_mode(winSize)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_name, length, width, x, y, speed):
        super().__init__()
        sprite = pygame.image.load(img_name)
        self.image = pygame.transform.scale(sprite, [length, width])
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        win.blit(self.image, [self.rect.x, self.rect.y])

class Player(GameSprite):
    def __init__(self, img_name, length, width, x, y, speed, button_up, button_down):
        super().__init__(img_name, length, width, x, y, speed)
        self.button_up = button_up
        self.button_down = button_down

    def move(self):
        list_key = pygame.key.get_pressed()
        if list_key[self.button_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if list_key[self.button_down] and self.rect.y < 300:
            self.rect.y += self.speed


player1 = Player('platform.png', 50, 200, 0, 150, 3, pygame.K_UP, pygame.K_DOWN) 
player2 = Player('platform2.png', 50, 200, 655, 150, 3, pygame.K_w, pygame.K_s)

score_player1 = 0
score_player2 = 0

while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    player1.move()
    player2.move()

    win.fill([3, 177, 252])
    player1.reset()
    player2.reset()

    pygame.display.update()
    clock.tick(FPS) 