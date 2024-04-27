import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("C:/Users/Dias/Desktop/PP2/lab 7/music player/musices/1.mp3")  # Укажите путь к вашему файлу музыки
pygame.mixer.music.play()

# Ждем, пока музыка воспроизводится
while pygame.mixer.music.get_busy():
    time.sleep(1)
