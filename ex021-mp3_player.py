# Exercício 021 - Tocando um MP3
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('/storage/emulated/0/Ringtones/zedge/54b31225-7076-45f6-9a67-de7648debc54/Obstacles.mp3')
pygame.mixer.music.play()
print("Tocando... Não feche o app!")

while pygame.mixer.music.get_busy():
    time.sleep(1)

print("Acabou a música!")
