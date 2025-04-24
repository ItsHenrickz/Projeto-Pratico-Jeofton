# configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo da Cobrinha")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanho_quadrado = 20
velocidade_cobra = 15

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho_quadrado, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])


def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True

        #desenhar_comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

# criar um loop infinito

# desenhar os objetos do jogo na tela
# pontuação
# cobrinha
# comida

# criar a logica de terminar o jogo
# o que acontece:
# cobra bateu na parede
# cobra bateu na propria cobra

# pegar as interações do usuario
# fechou a tela
# apertou as teclas do teclado pra mover a cobra


rodar_jogo()