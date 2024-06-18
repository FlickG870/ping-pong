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
ball = GameSprite('ball.png', 50, 50, 120, 120, 4)

score_player1 = 0
score_player2 = 0

speed_ball_x = 4
speed_ball_y = 3

while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

    player1.move()
    player2.move()
    ball.rect.x += speed_ball_x
    ball.rect.y += speed_ball_y

    if ball.rect.y >= 450:
        speed_ball_y *= -1
    if ball.rect.y <= 0:
        speed_ball_y *= -1
    if ball.rect.x >= 700:
        score_player1 += 1
        ball.rect.x = 600
        ball.rect.y = 200
        speed_ball_x = -4 
    if ball.rect.x <= 0:
        score_player2 += 1
        ball.rect.x = 100
        ball.rect.y = 200
        speed_ball_x = 4

    if pygame.sprite.collide_rect(ball, player1):
        speed_ball_x = 4
    if pygame.sprite.collide_rect(ball, player2):
        speed_ball_x = -4     

    win.fill([3, 177, 252])
    player1.reset()
    player2.reset()
    ball.reset()

    pygame.display.update()
    clock.tick(FPS) 