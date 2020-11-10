import pygame
import time
from random import randint

clock = pygame.time.Clock()
pygame.mixer.init()

LIXOVELOCIDADE = 10

class LixoL(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/L1.png'),
                    pygame.image.load('Imagens/jogo/L2.png'),
                    pygame.image.load('Imagens/jogo/L3.png'),
                    pygame.image.load('Imagens/jogo/L4.png'),
                    pygame.image.load('Imagens/jogo/L5.png')]

        self.current_image = randint(0, 4)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(130, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y += LIXOVELOCIDADE
        if self.rect.bottom > 750:
            self.kill()


class LixoR(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/L1.png'),
                    pygame.image.load('Imagens/jogo/L2.png'),
                    pygame.image.load('Imagens/jogo/L3.png'),
                    pygame.image.load('Imagens/jogo/L4.png'),
                    pygame.image.load('Imagens/jogo/L5.png')]

        self.current_image = randint(0, 4)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(810, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y += LIXOVELOCIDADE
        if self.rect.bottom > 750:
            self.kill()

class tiro(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.images = [pygame.image.load('Imagens/jogo/L1.png'),
                    pygame.image.load('Imagens/jogo/L2.png'),
                    pygame.image.load('Imagens/jogo/L3.png'),
                    pygame.image.load('Imagens/jogo/L4.png'),
                    pygame.image.load('Imagens/jogo/L5.png')]

        self.current_image = randint(0, 4)
        self.image = pygame.image.load('Imagens/jogo/Lixo1.png')
        self.image = pygame.transform.scale(self.image, [69, 146])
        self.rect = pygame.Rect(130, randint(-150, 0), 0, 0)

    def update(self, *args):
        self.image = self.images[self.current_image]
        self.rect.y -= 28
        if self.rect.bottom < -10:
            self.kill()
