from pacman import *
import time

def obtem_direecao(ponto1, ponto2):
    theta = math.atan2(ponto1[1] - ponto2[1], ponto1[0] - ponto2[0])
    dir_x = math.cos(theta)
    dir_y = math.sin(theta)
    return dir_x, dir_y


def pacman_cima(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (0, 5)
    return estado_jogo['pacman']['direcao_atual']




def pacman_baixo(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (0, -5)

    return estado_jogo['pacman']['direcao_atual']



def pacman_direita(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (5, 0)

    return estado_jogo['pacman']['direcao_atual']

    


def pacman_esquerda(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (-5, 0)
    return estado_jogo['pacman']['direcao_atual']






def movimenta_pinky(estado_jogo):
    pass


def calculate_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def movimenta_clyde(estado_jogo):
    scatter_distance_threshold = 3
    scatter_corner_index = 0
    pacman_pos = estado_jogo['pacman']['objeto'].pos()
    ghost_pos = estado_jogo['fantasmas'][PINKY_OBJECT]['objeto'].pos()
    
    return 


def movimenta_inky(estado_jogo):
    #direcaorandom = random.randint(0, 3)
    #FUNCOES_DIRECAO[5] = DIRECOES_POSSIVEIS[direcaorandom]
    
    #return FUNCOES_DIRECAO[5]
    pass

def movimenta_blinky(estado_jogo):
    pass

def perdeu_jogo(estado_jogo):
    pass

def atualiza_pontos(estado_jogo):
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    index = offset((x,y))
    if estado_jogo['mapa'][index] == 1:
        estado_jogo['score'] += 1
        estado_jogo['mapa'][index] = 7
        x, y = calcula_x_y_from_index(index)
        estado_jogo['marcador'].goto(x + 10,y + 10)
        estado_jogo['marcador'].dot(2,'blue')
        update_board(estado_jogo)


def atualiza_mapa(estado_jogo, x, y, elemento):
    index = offset((x,y))
    while estado_jogo['mapa'][index] in [BLINKY_OBJECT, PINKY_OBJECT, INKY_OBJECT, CLYDE_OBJECT]:
        index += 1
    estado_jogo['mapa'][index] = elemento

def actualiza_posicao_pacman_fantasma(estado_jogo):
    x = estado_jogo['pacman']['objeto'].xcor() 
    y = estado_jogo['pacman']['objeto'].ycor()
    atualiza_mapa(estado_jogo, x, y, PACMAN_OBJECT)
    for ghost_id, ghost in estado_jogo['fantasmas'].items():
        x = ghost['objeto'].xcor()
        y = ghost['objeto'].ycor()
        atualiza_mapa(estado_jogo, x, y, ghost_id)


def guarda_jogo(estado_jogo):
    actualiza_posicao_pacman_fantasma(estado_jogo)
    str_mapa = ''
    pass

def carrega_jogo(estado_jogo, nome_ficheiro):
    # Abrir e ler o arquivo
    with open(rf"C:\\Users\\Utilizador\\Desktop\\Codigo-Alunos\\Codigo-Alunos\\{nome_ficheiro}", 'r') as file:
        data = file.read()

    data = data.replace('\n', '').replace(' ', '')

    elementos = data.split(',')
    elementos = [int(x) for x in elementos if x]

    estado_jogo['mapa'] = elementos

    return estado_jogo['mapa']

if __name__ == '__main__':
    try:
        funcoes_jogador = {'pacman_cima': pacman_cima, 'pacman_baixo': pacman_baixo, 'pacman_esquerda': pacman_esquerda, 'pacman_direita': pacman_direita, 'guarda_jogo' : guarda_jogo, 'carrega_jogo' : carrega_jogo}    
        funcoes_fantasmas = {BLINKY_OBJECT : movimenta_blinky, PINKY_OBJECT : movimenta_pinky, INKY_OBJECT : movimenta_inky, CLYDE_OBJECT : movimenta_clyde}


        nome_ficheiro = input('Pretende carregar um mapa (Enter para carregar o mapa default): ')
        if nome_ficheiro == '':
            nome_ficheiro = 'mapa_inicial.txt'
        ##dicionario com as funcoes de movimento dos jogadores
        
        #funções de inicio do jogo
        estado_jogo = init_state()
        carrega_jogo(estado_jogo, nome_ficheiro)    
        setup(estado_jogo, True, funcoes_jogador,funcoes_fantasmas)
        
        #inicia_jogo(estado_jogo)
        while not perdeu_jogo(estado_jogo):
            if estado_jogo['mapa'] is not None:
                estado_jogo['janela'].update() #actualiza a janela
                movimenta_objectos(estado_jogo)
                atualiza_pontos(estado_jogo)
                time.sleep(0.05)
    except TclError:
        pass
