import pygame
import math

class Carro(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('Imagens/jogo/caminhãodelixo.png')
        self.image = pygame.transform.scale(self.image, [140, 330])
        self.rect = pygame.Rect(440, -150, 100, 320)
        self.timer = 0

    def update(self, *args):
        self.timer += 0.06
        self.rect.x = 35

        self.rect.x = 425 + math.sin(self.timer) * 225

        #if self.rect.top < 0:
            #self.rect.top = 0
        if self.rect.bottom > 650:
            self.rect.bottom = 650
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
