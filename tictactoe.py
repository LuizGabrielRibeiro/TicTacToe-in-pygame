import pygame

#primeiro criamos um classe janela onde iremos configurar nossa tela de exibição
class Window:
    __width = 0 #a definir
    __height = 0 #a definir
    __color = (255,255,255) #branco

    def __init__(self, largura, altura): #construtor
        self.__width = largura
        self.__height = altura

    def returnWinSize(self): #retorna tamanho da tela
        return (self.__width, self.__height)

    def returnColor(self): #retorna a cor da janela
        return self.__color

#agora vamos definir as funções que irão fazer o jogo funcionar

#aqui desenhamos nosso tabuleiro com linhas representando suas divisórias
def draw_board():
    pygame.draw.line(tela, (0, 0, 0), (200, 0), (200, 600), 10) 
    pygame.draw.line(tela, (0, 0, 0), (400, 0), (400, 600), 10)
    pygame.draw.line(tela, (0, 0, 0), (0, 200), (600, 200), 10)
    pygame.draw.line(tela, (0, 0, 0), (0, 400), (600, 400), 10)


#função para desenhar os simbolos no tabuleiro
def draw_symbol(position):
    global TURN
    x, y = position
    if TURN == 'PLAYER1':
        img = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))
        
    elif TURN == 'PLAYER2':
        img = pygame.image.load('o.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))

#funcao para verificar a posição do click
def test_position():
    for rect in big_board:
        if e.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(mouse_pos):
            if rect == rect1:
                confirm(0, [100, 100])
            if rect == rect2:
                confirm(1, [300, 100])
            if rect == rect3:
                confirm(2, [500, 100])
            if rect == rect4:
                confirm(3, [100, 300])
            if rect == rect5:
                confirm(4, [300, 300])
            if rect == rect6:
                confirm(5, [500, 300])
            if rect == rect7:
                confirm(6, [100, 500])
            if rect == rect8:
                confirm(7, [300, 500])
            if rect == rect9:
                confirm(8, [500, 500])

#função que verifica se a casa do tabuleiro está apta a ser escolhida ou não
def confirm(index, position):
    global TURN, SYMBOL, COUNT
    
    if BOARD[index] == '-':
        
        BOARD[index] = SYMBOL
        draw_symbol(position)
        
        if TURN == 'PLAYER1':
            TURN = 'PLAYER2'
        else:
            TURN = 'PLAYER1'

        COUNT += 1

#função para verificar condições de vitória
def test_victory(symbol):
    return ((BOARD[0] == symbol and BOARD[1] == symbol and BOARD[2] == symbol) or
        (BOARD[3] == symbol and BOARD[4] == symbol and BOARD[5] == symbol) or
        (BOARD[6] == symbol and BOARD[7] == symbol and BOARD[8] == symbol) or
        (BOARD[0] == symbol and BOARD[3] == symbol and BOARD[6] == symbol) or
        (BOARD[1] == symbol and BOARD[4] == symbol and BOARD[7] == symbol) or
        (BOARD[2] == symbol and BOARD[5] == symbol and BOARD[8] == symbol) or
        (BOARD[0] == symbol and BOARD[4] == symbol and BOARD[8] == symbol) or
        (BOARD[2] == symbol and BOARD[4] == symbol and BOARD[6] == symbol))   

#função para escrever o resultado da partida na tela
def text_victory(symbol):
    arial = pygame.font.SysFont('arial', 50)
    msg = 'JOGADOR {} VENCEU'.format(symbol)

    if symbol == 'EMPATE':
        msg_victory = arial.render('DEU VELHA!', True, (255, 0, 128), 0)
        tela.blit(msg_victory, (155, 265))
    else:
        msg_victory = arial.render(msg, True, (0, 255, 0), 0)
        tela.blit(msg_victory, (40, 265))

#função para resetar o jogo
def reset():
    global BOARD, STATE, TURN, SYMBOL, COUNT
    BOARD = [
        '-', '-', '-',
        '-', '-', '-',
        '-', '-', '-'
    ]
    STATE = 'PLAYING' 
    TURN = 'PLAYER1' 
    SYMBOL = 'X' 
    COUNT = 0 
    tela.fill((255,255,255))

#incializamos o módulo pygame
pygame.init()

#agora definimos algumas variáveis globais que serão responsáveis pelo funcionamento do jogo       

BOARD = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
] #tabuleiro do jogo para verificação
STATE = 'PLAYING' #estado do jogo
TURN = 'PLAYER1' #vez de cada jogador
SYMBOL = 'X' #simbolo de cada jogador
COUNT = 0 #contador de jogadas

#definimos 9 retângulos que servirão de base para o tabuleiro

rect1 = pygame.Rect((0, 0), (200, 200))
rect2 = pygame.Rect((200, 0), (200, 200))
rect3 = pygame.Rect((400, 0), (200, 200))
rect4 = pygame.Rect((0, 200), (200, 200))
rect5 = pygame.Rect((200, 200), (200, 200))
rect6 = pygame.Rect((400, 200), (200, 200))
rect7 = pygame.Rect((0, 400), (200, 200))
rect8 = pygame.Rect((200, 400), (200, 200))
rect9 = pygame.Rect((400, 400), (200, 200))

#definimos aqui, um tabuleiro com os retângulos criados acima

big_board = [
    rect1,rect2,rect3,rect4,
    rect5,rect6,rect7,rect8,rect9,
] 

#definimos aqui nossa tela de exibição

janela = Window(600,600) #criamos nosso objeto janela (600x600)
tela = pygame.display.set_mode(janela.returnWinSize()) #inicializamos nossa janela
tela.fill(janela.returnColor()) #definimos a cor da janela 
pygame.display.set_caption('TicTacToe') #definimos o titulo da janela

#aqui iniciamos noss game loop

while True:

    mouse_pos = pygame.mouse.get_pos() #pega a posição do mouse
    
    if STATE == 'PLAYING':
        
        draw_board() #desenha o tabuleiro

        for e in pygame.event.get(): #pega os eventos numa fila de eventos
            
            if e.type == pygame.QUIT:
                pygame.quit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if TURN == 'PLAYER1':
                    SYMBOL = 'X'
                    test_position()
                else:
                    SYMBOL = 'O'
                    test_position()    
            
            if test_victory('X'):
                text_victory('X')
                STATE = 'RESET'

            elif test_victory('O'):
                text_victory('O')
                STATE = 'RESET'

            elif COUNT >= 9:
                text_victory('EMPATE')    
                STATE = 'RESET'

    else:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                reset()
                draw_board()

    pygame.display.flip()                   