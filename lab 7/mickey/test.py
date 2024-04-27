import pygame
import sys
from datetime import datetime


pygame.init()


width, height = 700, 525
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")


background = pygame.image.load("./date/background.png")
background = pygame.transform.scale(background, (width, height))


rightarm = pygame.image.load("./date/rightarm.png")
rightarm = pygame.transform.scale(rightarm, (1100, 500))

leftarm = pygame.image.load("./date/leftarm.png")
leftarm = pygame.transform.scale(leftarm, (63, 500))


def draw_clock_hands():

    date = datetime.now()
    minutes = date.minute
    seconds = date.second


    minute_angle = -(minutes % 60) * 6 - 66
    second_angle = -(seconds % 60) * 6 - 6


    minute_hand = pygame.transform.rotate(rightarm, minute_angle)
    second_hand = pygame.transform.rotate(leftarm, second_angle)

    screen.blit(minute_hand, (width // 2 - minute_hand.get_width() // 2, height // 2 - minute_hand.get_height() // 2))
    screen.blit(second_hand, (width // 2 - second_hand.get_width() // 2, height // 2 - second_hand.get_height() // 2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0)) # отображение
    draw_clock_hands() # обновить положение часов
    pygame.display.flip() # чтобы видетить измениение на экрена
    pygame.time.delay(1000) #задержка выполнение программы
