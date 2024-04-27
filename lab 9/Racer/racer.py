import pygame
import os
import random
import sys

pygame.init()

colorBlack = pygame.Color(0, 0, 0)
colorWhite = pygame.Color(255, 255, 255)
colorGrey = pygame.Color(128, 128, 128)
colorBlue = pygame.Color(0, 0, 255)
colorRed = pygame.Color(255, 0, 0)
colorGreen = pygame.Color(0, 255, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(colorWhite)
pygame.display.set_caption("Racer")

SPEED = 2
SCORE = 0
COINS = 0

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./date/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
            SCORE += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        self.cost = random.randint(1, 3)
        super().__init__()
        self.image = pygame.image.load("./date/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(9, SCREEN_WIDTH - 9), 560 - 13)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def reg(self):
        self.rect.center = (random.randint(9, SCREEN_WIDTH - 9), 560 - 13)
        self.cost = random.randint(1, 3)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./date/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 540)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 5)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E1 = Enemy()
C = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C)
CC = pygame.sprite.Group()
CC.add(C)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 10000)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBlack)

done = False
background = pygame.image.load("./date/background_race.png")

while not done:
    N = random.randint(5, 10)
    scores = font_small.render(str(SCORE), True, colorBlack)
    n_c = font_small.render(str(COINS), True, colorBlack)
    DISPLAYSURF.blit(background, (0, 0))
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(n_c, (370, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == INC_SPEED:
            SPEED += 1

    P1.update()
    E1.move()

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if isinstance(entity, Enemy):
            entity.move()

    if pygame.sprite.spritecollideany(P1, CC):
        for entity in CC:
            COINS += 1
            entity.reg()

    pygame.display.update()
