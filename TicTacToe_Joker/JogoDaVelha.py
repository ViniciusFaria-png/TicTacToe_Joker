#GRUPO
#VINÍCIUS RODRIGUES FIGUEIRA DE FARIA
#TIA: 32013639
#OBSERVACAO
#No menu principal, nao é em toda a area da carta que ao clickar inicia o jogo ou o manual
#Por isso desenhei dois quadrados vermelhos para auxilio
#No quadrado vermelho que inicia o jogo, é necessario clickar duas vezes
import pygame
from pygame.locals import *
from sys import exit
from pygame import mixer

WHITE = (255, 255, 255)
GREEN = (60, 95, 39)
RED = (190, 0, 0)
ROXO = (126, 23, 149)
CINZA = (128,128,128)
pontosSalvo = "pontos.txt"
um = 0
dois = 0

pygame.init()
jokerBack = pygame.image.load(r'Cartas.jpg')
instruMenu = pygame.image.load(r'Instrucoes.jpg')
tela = pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo da velha, Edicao Coringa")
pygame.mixer.music.load(r'CircoBack.ogg')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1, 0.0)

with open(r"Jogador1.txt", "r") as f:
    Jogador1 = f.read()
with open(r"Jogador2.txt", "r") as f:
    Jogador2 = f.read()

ESTADO = 'MENU'
VEZ = 'JOGADOR1'
ESCOLHA = 'X'
espaco = 0

marcaTabu = [
    0, 1, 2,
    3, 4, 5, 
    6, 7, 8
]

rect1 = Rect((0,0), (200,200))
rect2 = Rect((200,0), (200,200))
rect3 = Rect((400,0), (200,200))
rect4 = Rect((0,200), (200,200))
rect5 = Rect((200,200), (200,200))
rect6 = Rect((400,200), (200,200))
rect7 = Rect((0,400), (200,200))
rect8 = Rect((200,400), (200,200))
rect9 = Rect((400,400), (200,200))

rec = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
]

def desenharLinhas():
    pygame.draw.line(tela, (GREEN), (200, 0), (200, 600), 10)
    pygame.draw.line(tela, (GREEN), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (ROXO), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (ROXO), (0, 400), (600, 400), 10)

def desenharPeca(pos):
    global VEZ
    x, y = pos
    if VEZ == 'JOGADOR2':
        img = pygame.image.load(r'j.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))
    else:
        img = pygame.image.load(r'z.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

def cliques():
    for p in rec:
        if event.type == MOUSEBUTTONDOWN and p.collidepoint(mousePos):
            if p == rect1:
                confirmar(0, [100, 100])
            if p == rect2:
                confirmar(1, [300, 100])
            if p == rect3:
                confirmar(2, [500, 100])
            if p == rect4:
                confirmar(3, [100, 300])
            if p == rect5:
                confirmar(4, [300, 300])
            if p == rect6:
                confirmar(5, [500, 300])
            if p == rect7:
                confirmar(6, [100, 500])
            if p == rect8:
                confirmar(7, [300, 500])
            if p == rect9:
                confirmar(8, [500, 500])
                
def confirmar(indice, pos):
    global ESCOLHA, VEZ, espaco
    if marcaTabu[indice] == 'X':
        print('X')
    elif marcaTabu[indice] == 'O':
        print('O')
    else:
        marcaTabu[indice] = ESCOLHA
        desenharPeca(pos)
        print(marcaTabu)
        if VEZ == 'JOGADOR1':
            VEZ = 'JOGADOR2'
        else:
            VEZ = 'JOGADOR1'
        espaco += 1

def vitoria(l):
    return ((marcaTabu[0] == l and marcaTabu[1] == l and marcaTabu[2] == l) or
        (marcaTabu[3] == l and marcaTabu[4] == l and marcaTabu[5] == l) or
        (marcaTabu[6] == l and marcaTabu[7] == l and marcaTabu[8] == l) or
        (marcaTabu[0] == l and marcaTabu[3] == l and marcaTabu[6] == l) or
        (marcaTabu[1] == l and marcaTabu[4] == l and marcaTabu[7] == l) or
        (marcaTabu[2] == l and marcaTabu[5] == l and marcaTabu[8] == l) or
        (marcaTabu[0] == l and marcaTabu[4] == l and marcaTabu[8] == l) or
        (marcaTabu[2] == l and marcaTabu[4] == l and marcaTabu[6] == l))

def anuncioVitoria(v):
    arial = pygame.font.SysFont('arial', 70)
    mensagem = 'JOGADOR {} VENCEU'.format(v)

    if v == 'EMPATE':
        risadaEmpate = mixer.Sound(r'Untitled.ogg')
        risadaEmpate.play()
        mensVitoria = arial.render("DEU VELHA HAHAHAHA", True, (CINZA), 0)
        tela.blit(mensVitoria, (0, 265))
    else:
        risadaVitoria = mixer.Sound(r'Untitled2.ogg')
        risadaVitoria. set_volume(0.1)
        risadaVitoria.play()
        mensVitoria = arial.render(mensagem, True, (CINZA), 0)
        tela.blit(mensVitoria, (0, 265))

def reset():
    global ESCOLHA, ESTADO, VEZ, marcaTabu, espaco
    ESTADO = 'JOGANDO'
    VEZ = 'JOGADOR1'
    ESCOLHA = 'X'
    espaco = 0
    marcaTabu = [
    0, 1, 2,
    3, 4, 5, 
    6, 7, 8
    ]
    tela.fill(0)

# Novos detalhes e melhorias
def showName():
    #Criador
    nome = 'Vinícius Faria'
    arial = pygame.font.SysFont('arial', 20)

    textX = 10
    textY = 10
    name = arial.render("Criador :" + str(nome), True, (255,255,255))
    tela.blit(name, (430, 580))

def scoreJogadores(um, dois, pontos):
    #Mostra na tela os pontos dos jogadores
    arial = pygame.font.SysFont('arial', 20)
    textX = 10
    textY = 10
    pontosUm = arial.render("J1 Vitórias:" + str(um), True, (255,255,255))
    pontosDois = arial.render("J2 Vitórias:" + str(dois), True, (255,255,255))
    highscoreUm = arial.render("Maior Sequencia:" +str(Jogador1), True, (255,255,255))
    highscoreDois = arial.render("Maior Sequencia:" +str(Jogador2), True, (255,255,255))
    tela.blit(pontosUm, (0, 0))
    tela.blit(pontosDois, (500, 0))
    tela.blit(highscoreUm, (0,20))
    tela.blit(highscoreDois, (450,20))

click = False
def mainMenu(ESTADO):
    #Loop Menu Principal
    while ESTADO == 'MENU':
        tela.fill((0,0,0))
        tela.blit(jokerBack, (0,0))

        mx, my = pygame.mouse.get_pos()

        botao1 = pygame.Rect(370,400,100,50)
        botao2 = pygame.Rect(125,380,100,50)
        if botao1.collidepoint((mx, my)):
            if click:
                ESTADO = "JOGANDO"
        if botao2.collidepoint((mx, my)):
            if click:
                opcoes()
        #QUADRADOS UTILIZADOS PARA A VISUALIZACAO DOS BOTOES DO MENU
        pygame.draw.rect(tela, (255,0,0), botao1)
        pygame.draw.rect(tela, (255,0,0), botao2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

def opcoes():
    #Loop Instrucoes
    rodando = True
    while rodando:
        tela.fill((0,0,0))
        tela.blit(instruMenu, (0,0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rodando = False
        pygame.display.update()

            
mainMenu(ESTADO)
#Loop do jogo
rodando = True
while rodando == True:
    mousePos = pygame.mouse.get_pos()
    rodando = True
    if ESTADO == 'JOGANDO':
        showName()
        scoreJogadores(um, dois, Jogador1)
        desenharLinhas()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if VEZ == 'JOGADOR1':
                    ESCOLHA = 'X'
                    cliques()
                else:
                    ESCOLHA = 'O'
                    cliques()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()


        if vitoria('X'):
            print('X VENCEU')
            anuncioVitoria('X')
            um += 1
            if um>int(Jogador1):
                Jogador1 = um
                with open(r"Jogador1.txt", "w") as f:
                    f.write(str(Jogador1))
            ESTADO = 'RESET'

        elif vitoria('O'):
            print('O VENCEU')
            anuncioVitoria('O')
            dois += 1
            if dois>int(Jogador2):
                Jogador2 = dois
                with open(r"Jogador2.txt", "w") as f:
                    f.write(str(Jogador2))
            ESTADO = 'RESET'
        
        elif espaco >= 9:
            print('EMPATE')
            anuncioVitoria('EMPATE')
            ESTADO = 'RESET'

    else:
        for u in pygame.event.get():
            if u.type == QUIT:
                pygame.quit()
                exit()
            if u.type == MOUSEBUTTONDOWN:
                reset()
            if u.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    rodando == False
    pygame.display.flip()
