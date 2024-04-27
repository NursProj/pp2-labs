import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 700, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

background = pygame.image.load("./date/background.png")
background = pygame.transform.scale(background, (width, height))

rightarm = pygame.image.load("./date/rightarm.png")
rightarm = pygame.transform.scale(rightarm, (1100, 500))

leftarm = pygame.image.load("./date/leftarm.png")
leftarm = pygame.transform.scale(leftarm, (63, 500))

font = pygame.font.SysFont(None, 36)

BLACK = (0, 0, 0)

def draw_clock_hands():
    date = datetime.now()
    minutes = date.minute
    seconds = date.second
    text_surface = font.render(date.strftime("%H:%M:%S"), True, BLACK)

    minute_angle = -(minutes % 60) * 6 - 66
    second_angle = -(seconds % 60) * 6 - 6
    text_rect = text_surface.get_rect()

    minute_hand = pygame.transform.rotate(rightarm, minute_angle)
    second_hand = pygame.transform.rotate(leftarm, second_angle)
    text_rect.center = (width // 2, height - height//20)


    screen.blit(minute_hand, (width // 2 - minute_hand.get_width() // 2, height // 2 - minute_hand.get_height() // 2))
    screen.blit(second_hand, (width // 2 - second_hand.get_width() // 2, height // 2 - second_hand.get_height() // 2))
    screen.blit(text_surface, text_rect)

def draw_digital_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    text_surface = font.render(current_time, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.bottomleft = (20, height - 40)
    screen.blit(text_surface, text_rect) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    draw_clock_hands()
    draw_digital_clock() 
    pygame.display.flip() 
    pygame.time.delay(1000)  
