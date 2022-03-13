import pygame

from pygame.locals import *

from sys import exit


pygame.init()

############## display ############
largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))

############## loop ############
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
######## reiniciar o jogo ########
    pygame.display.update()