# Faça um programa em python que abra e reproduza o áudio de um arq mp3

from pygame import mixer
mixer.init()
mixer.music.load('dis.mp3')
mixer.music.play()
import time
time.sleep(5)
