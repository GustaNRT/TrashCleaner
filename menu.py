import pygame
from moviepy.editor import *
#import shelve

from catador import Carro
from player import Player
from lixos import LixoL
from lixos import LixoR
from lixos import tiro
from time import sleep


import math
from random import randint
import os


os.environ['SDL_VIDEO_CENTERED'] = '1'

WIDTH = 980
HEIGHT = 720

pygame.init()
pygame.display.set_caption("Trash Cleaner")
tela = pygame.display.Info()
width = tela.current_w -386
height = tela.current_h -48
print(width, height)
#screen = pygame.display.set_mode((tela.current_w, tela.current_h -25)), pygame.FULLSCREEN
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# Iniciando imagens, sons e fontes e arquivos


invissible = (0, 0, 0, 0,)

titulo = pygame.image.load('imagens/menu/titulo.png')
fundo = pygame.image.load('imagens/menu/fundo.png')
if screen == 1366:
    fundo = pygame.transform.scale(fundo, [1366, 768])

jogar = pygame.image.load('imagens/menu/jogar.png')
jogar_alt = pygame.image.load('imagens/menu/jogaralt.png')

sair = pygame.image.load('imagens/menu/sair.png')
sair_alt = pygame.image.load('imagens/menu/sairalt.png')

config = pygame.image.load('imagens/menu/config.png')
config_alt = pygame.image.load('imagens/menu/configalt.png')

pts = pygame.image.load('imagens/hud/pts2.png')
mochila = pygame.image.load('imagens/hud/mochila2.png')
time = pygame.image.load('imagens/hud/timer2.png')

gameover = pygame.image.load('imagens/gameover.png')

botao = [jogar, jogar_alt, sair, sair_alt]

#MUSICAS
menu_music = pygame.mixer.Sound('Sons/menu.ogg')
jogo_music = pygame.mixer.Sound('Sons/jogo.ogg')
jogar_saco = pygame.mixer.Sound('Sons/jogar o saco.wav')
click_music = pygame.mixer.Sound('Sons/click.ogg')

menu_music.set_volume(0.5)
jogo_music.set_volume(0.5)
jogar_saco.set_volume(0.5)
click_music.set_volume(0.5)

#CONFIGURAÇOES

seleçao = pygame.image.load('imagens/opçoes/dificuldade/seleçao.png')

fundo_conf = pygame.image.load('imagens/opçoes/ret5.png')
fundo_conf = pygame.transform.scale(fundo_conf, (width, height))

sfx_titulo = pygame.image.load('imagens/opçoes/sfx/titulosfx.png')
sfx_musica = pygame.image.load('imagens/opçoes/sfx/musica.png')
sfx_ef = pygame.image.load('imagens/opçoes/sfx/efsonoros.png')
sfx_mais_ef = pygame.image.load('imagens/opçoes/sfx/+.png')
sfx_menos_ef = pygame.image.load('imagens/opçoes/sfx/-.png')
sfx_mais_mu = pygame.image.load('imagens/opçoes/sfx/+.png')
sfx_menos_mu = pygame.image.load('imagens/opçoes/sfx/-.png')
sfx_click = pygame.image.load('imagens/opçoes/sfx/clique.png')
sfx_barra = pygame.image.load('imagens/opçoes/sfx/separaçao.png')

sfx_botao = [sfx_menos_ef, sfx_mais_ef, sfx_menos_mu, sfx_mais_mu]

dificuldade_titulo = pygame.image.load('imagens/opçoes/dificuldade/titulo.png')
facil = pygame.image.load('imagens/opçoes/dificuldade/facil.png')
medio = pygame.image.load('imagens/opçoes/dificuldade/medio.png')
dificil = pygame.image.load('imagens/opçoes/dificuldade/dificil.png')

video_titulo = pygame.image.load('imagens/opçoes/video/video.png')
full = pygame.image.load('imagens/opçoes/video/fullscreen.png')
janela = pygame.image.load('imagens/opçoes/video/janela.png')

aplicar = pygame.image.load('imagens/opçoes/botao/aplicar.png')
aplicar_alt = pygame.image.load('imagens/opçoes/botao/aplicaralt.png')
fechar = pygame.image.load('imagens/opçoes/botao/fechar.png')
fechar_alt = pygame.image.load('imagens/opçoes/botao/fecharalt.png')

#passos = pygame.mixer.Sound('Sons/passos.wav')

clip = VideoFileClip('imagens/intro.mp4')
clip.preview()


# Menu
def menu():
    
    # Coloca as imagens
    screen.blit(fundo_conf, (0, 0))
    screen.blit(fundo, (0, 0))
    screen.blit(titulo, (WIDTH / 4.5, 0))
    screen.blit(jogar, (WIDTH / 3.1, 300))
    # screen.blit(jogar_alt, (WIDTH / 4,0))
    screen.blit(sair, (WIDTH / 3, 460))
    # screen.blit(sair_alt, (WIDTH / 4,0))
    screen.blit(config, (899, 0))
    # screen.blit(config_alt, (800,0))
    pygame.display.flip()

    

    menu_music.stop()
    jogo_music.stop()
    menu_music.play()
    

    # Eventos clicáveis do Menu

    while pygame.event.wait() or pygame.event.get():

        # Pega a posição do mouse e
        # (Posição hitbox direita) > Posição X do mouse > (Posição hitbox esquerda) and (Posição hitbox baixo)
        # > Posição Y do mouse > (Posição hitbox cima) então:

        mouse = pygame.mouse.get_pos()
        pres = pygame.mouse.get_pressed()[0]

        #if pres:
            #click_music.play()

        if WIDTH / 3.1 + 359 > mouse[0] > WIDTH / 3.1 and 300 + 142 > mouse[1] > 300:
            screen.blit(jogar_alt, (WIDTH / 3.3, 288))
            if pres:
                click_music.play()
                jogo()

        else:
            screen.blit(jogar, (WIDTH / 3.1, 300))

        if WIDTH / 3 + 316 > mouse[0] > WIDTH / 3 and 460 + 115 > mouse[1] > 460:
            screen.blit(sair_alt, (WIDTH / 3, 460))
            if pygame.mouse.get_pressed()[0]:
                click_music.play()
                quit()
        else:
            screen.blit(sair, (WIDTH / 3, 460))

        if 900 + 67 > mouse[0] > 900 and 0 + 67 > mouse[1] > 0:
            screen.blit(config_alt, (899, -1))
            if pygame.mouse.get_pressed()[0]:
                click_music.play()
                conf()

        else:
            screen.blit(config, (900, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
        pygame.display.flip()

font_name = pygame.font.match_font('berlin sans FB', True, True)
def text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (238,175,81,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def vol_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (0,255,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    

def conf():
    vol_ef = 0.5
    vol_music = 0.5
    ef_txt = 5
    music_txt = 5
    pygame.display.flip()

    #invisivel
    #botao[0].fill(invissible)
    #botao[1].fill(invissible)
    #botao[2].fill(invissible)
    #botao[3].fill(invissible)

    #colocando na tela
    screen.blit(fundo_conf, (0, 0))

    #audio
    screen.blit(sfx_titulo, (200, 70))
    screen.blit(sfx_ef, (100, 154))
    screen.blit(sfx_musica, (205, 203))

    screen.blit(sfx_botao[0], (300, 150))
    screen.blit(sfx_botao[1], (382, 150))
    screen.blit(sfx_barra, (370, 145))

    screen.blit(sfx_botao[0], (300, 200))
    screen.blit(sfx_botao[1], (382, 200))
    screen.blit(sfx_barra, (370, 195))

    #video
    screen.blit(video_titulo, (670, 250))
    screen.blit(full, (600, 355))
    screen.blit(janela, (600, 390))

    #dificuldade
    screen.blit(dificuldade_titulo, (100, 350))
    screen.blit(facil, (100, 450))
    screen.blit(medio, (100, 485))
    screen.blit(dificil, (100, 520))

    screen.blit(aplicar, (width -320, height -90))
    screen.blit(fechar, (width -140, height -90))

      

    while pygame.event.wait() or pygame.event.get():

        # Pega a posição do mouse e
        # (Posição hitbox direita) > Posição X do mouse > (Posição hitbox esquerda) and (Posição hitbox baixo)
        # > Posição Y do mouse > (Posição hitbox cima) então:

        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()[0]

        #CONTROLE DE VOLUME
        if 300 + 62 > mouse[0] > 300 and 150 + 35 > mouse[1] > 150:
            if press:
                screen.blit(sfx_click, (300, 150))
                vol_ef -= 0.1
                ef_txt -= 1
                
                print (vol_ef)
            else:
                screen.blit(sfx_botao[0], (300, 150))

        if 382 + 62 > mouse[0] > 382 and 150 + 35 > mouse[1] > 150:
            if press:
                screen.blit(sfx_click, (382, 150))
                vol_ef += 0.1
                ef_txt += 1
                
                print (vol_ef)
            else:
                screen.blit(sfx_botao[1], (382, 150))

        if 300 + 62 > mouse[0] > 300 and 200 + 35 > mouse[1] > 200:
            if press:
                screen.blit(sfx_click, (300, 200))
                vol_music -= 0.1
                music_txt -= 1
                print (vol_music)
            else:
                screen.blit(sfx_botao[2], (300, 200))

        if 382 + 62 > mouse[0] > 382 and 200 + 35 > mouse[1] > 200:
            if press:
                screen.blit(sfx_click, (382, 200))
                vol_music += 0.1
                music_txt += 1
                print (vol_music)
            else:
                screen.blit(sfx_botao[3], (382, 200))

        #APLICAR E SAIR
        if (width-320) + 169 > mouse[0] > (width-320) and (height-90) + 58 > mouse[1] > (height-90):
            screen.blit(aplicar_alt, (width -318, height -87))
            if press:
                #screen.blit(aplicar_alt, (width -320, height -90))
                vol()
                
        else:
            screen.blit(aplicar, (width -320, height -90))

        if (width-140) + 105 > mouse[0] > (width-140) and (height-90) + 55 > mouse[1] > (height-90):
            screen.blit(fechar_alt, (width -139, height -88))
            if press:
                #screen.blit(fechar_alt, (width -140, height -90))
                menu() 

        else:
            screen.blit(fechar, (width -140, height -90))

        #if vol_ef <= 0.0 or vol_ef => 1.0 or vol_music <= 0.0 or vol_music => 1.0:
            #print('limite alcançado')

        if 0 <= ef_txt >= 10 or 0 <= music_txt >= 10:
            print('limite alcançado:')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()      

        
        vol_text(screen, f"{ef_txt}", 50, 480, 135)
        vol_text(screen, f'{music_txt}', 50, 480, 188)
            

        pygame.display.update()

        #pygame.display.flip()

        def vol():
            menu_music.set_volume(vol_music)
            jogo_music.set_volume(vol_music)
            jogar_saco.set_volume(vol_ef)
            click_music.set_volume(vol_ef)

# Game
def jogo():

    # objetos
    temporizador = 0
    pontos = 0
    lixomochila = 0
    timer = 0
    contagem = 60
    t = 2
    fps = 30

    objectGroup = pygame.sprite.Group()

    #lixos = LixoL(objectGroup)
    #lixos.rect.center = [100, 100]
    #lixos2 = LixoL(objectGroup)
    #lixos.rect.center = [200, 200]
    #lixos3 = LixoL(objectGroup)
    #lixos.rect.center = [300, 300]


    Lixo_group = pygame.sprite.Group()
    tiro_group = pygame.sprite.Group()
    #lixoL = LixoL()
    #lixoR = LixoR()
    #Lixo_group.add(lixoL)
    #Lixo_group.add(lixoR)

    Player_group = pygame.sprite.Group()
    player = Player()
    Player_group.add(player)

    Carro_group = pygame.sprite.Group()
    carro = Carro()
    Carro_group.add(carro)

    all_group = pygame.sprite.Group()
    #all_group.add(player)
    #all_group.add(carro)
    #all_group.add(lançar)
    #all_group.add(lixoL)
    #all_group.add(lixoR)

    # Fundo
    bg = pygame.image.load('Imagens/jogo/fundosemobjetos.png').convert()
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
    bg_y = 0

    # Sounds
    andar = pygame.mixer.Sound('Sons/passos.wav')

    # Música

    menu_music.stop()
    jogo_music.play()

    # enemies_spd = 0

    clock = pygame.time.Clock()
    tela = True
    while tela:
        clock.tick(fps)
        # Faz o Fundo continuar infinito
        bg_y1 = bg_y % bg.get_height()
        bg_y += 10

        screen.blit(bg, (0, bg_y1 - bg.get_height()))

        
        if bg_y1 < HEIGHT:
            screen.blit(bg, (0, bg_y1))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                if event.key == pygame.K_SPACE:
                    atirar = tiro(objectGroup, tiro_group)

                    if lixomochila >= 1:
                        atirar.rect.center = player.rect.center
                        lixomochila -= 1
                        jogar_saco.stop()
                        jogar_saco.play()

        timer += 1
        if timer == fps:
            #time.sleep(0.1)
            timer = 0
            lixol = LixoL(objectGroup, Lixo_group)
            lixor = LixoR(objectGroup, Lixo_group)
            contagem -= 1
        if contagem == 0:
            screen.blit(gameover,(WIDTH/4.5, 200))
        if contagem == -1:
            screen.blit(gameover,(WIDTH/4.5, 200))
            sleep(10)

        # Update
        objectGroup.update()
        #objectGroup.draw(screen)

        #colisão
        if pygame.sprite.groupcollide(Lixo_group, Player_group, True, False):
            lixomochila += 1

        if pygame.sprite.groupcollide(tiro_group, Carro_group, True, False):
            pontos += 2

        #Lixo_group.update()
        #Lixo_group.draw(screen)

        objectGroup.draw(screen)

        Player_group.update()
        Player_group.draw(screen)

        Carro_group.update()
        Carro_group.draw(screen)

        all_group.update()
        all_group.draw(screen)

        #draw_shield_bar(screen, 5, 5)

        #screen.blit(fundodados, (0, 0))
        screen.blit(pts, (15, 20))
        screen.blit(mochila, (15, 80))
        screen.blit(time, (655, 20))

        text(screen, f"{pontos}", 50, 280, 15)
        text(screen, f"{lixomochila}", 30, 260, 80)
        text(screen, f"{contagem}", 30, 799, 22)

        pygame.display.update()
        #screen.fill((0, 0, 0))
        
menu()
pygame.quit()
