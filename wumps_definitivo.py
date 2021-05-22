import os #import para a limpa de tela
from random import randint #import para o randomização das posiçoes dos buracos, ouro e wumpus
numero_colunas = numero_linhas = 5 #numero de linhas e colunas padrão 5
valor = 0 #valor inicial para a matriz ser prenchida
posiçãoAgente = [numero_linhas-1,0] # posição do agente sempre iniciando no canto inferior esquerdo 
posiçãoOuro = list() #declaração das posiçoes em lista
posiçãoWumpus = list()
posiçãoBuraco = list()
bousa = w = b = 0 #iniciando a bousa pra quando capturar o ouro, w para quando vc entrar na casa do wumpus e b pra quando entrar na casa do buraco
os.system('cls') #comando pra limpar a tela
print('='*143) #intro do jogo
print(' '*30 + 'Bem vindo ao mundo de Wumpus!')
print(' '*30 + 'Encontre o ouro')
print(' '*30 + 'Tome cuidado para não cair nos buracos, eles emanam vento')
print(' '*30 + 'O Wumpus é fedorento, então fica a dica!\n')
print('='*143)
pausa = input(' '*30 + 'de enter para começar o jogo') # uma pausa para o usuario ter tempo para ler o enunciado
os.system('cls')
def crie_matriz(numero_linhas, numero_colunas, valor): #função para a criação da matriz
    matriz = list() 
    for i in range(numero_linhas):
        linha = list() 
        for j in range(numero_colunas):
            linha.append(valor) #preenchimento com o valor indicado no começo
        matriz.append(linha) # montando a matriz com as listas criada acima
    matriz[numero_linhas-1][0] = 1 #inicialização do Agente na posição indicada no começo
    while True: #processo de inicialização do Wumpus na matriz
        l = randint(0,numero_linhas-1)
        c = randint(0,numero_colunas-1)
        
        if matriz[l][c] == 0:
            matriz[l][c] = 2
            posiçãoWumpus.append(l) #armazenamento da posição a qual o wumpus se encontra
            posiçãoWumpus.append(c)
            break
            
    for z in range(numero_linhas-1): # processo de inicialização dos buracos na matriz, sendo que a quantidade sempre sera
        while True:             # o tamanho da matriz -1, tipo: tamanho 5x5, serão 4 buracos
            l = randint(0,numero_linhas-1)
            c = randint(0,numero_colunas-1)
            L = list()
            if matriz[l][c] == 0:
                matriz[l][c] = 3
                L.append(l)
                L.append(c)
                posiçãoBuraco.append(L) #armazenamento da posição a qual os buracos se encontra
                break 
    while True: # processo de inicialização do ouro na matriz
        l = randint(0,numero_linhas-1)
        c = randint(0,numero_colunas-1)
        if matriz[l][c] == 0:
            matriz[l][c] = 4    
            posiçãoOuro.append(l) #armazenamento da posição a qual o ouro se encontra
            posiçãoOuro.append(c)
            break
    return matriz
a = crie_matriz(numero_linhas, numero_colunas, valor)# chama a função para criar a matriz
while True:
    mov = 'z'
    while True:
        a[posiçãoAgente[0]][posiçãoAgente[1]] = 1
        for l in range(numero_linhas):
            for c in range(numero_colunas):
                if a[l][c] == 0 or a[l][c] == 2 or a[l][c] == 3 or a[l][c] == 4:
                    print('[ ]', end='')
                if a[l][c] == 1:
                    print('[A]', end='')
            print()
        if posiçãoAgente[0] != numero_linhas-1:
            if a[posiçãoAgente[0]+1][posiçãoAgente[1]] == 2:
                print('Você esta sentindo fedor')
        if posiçãoAgente[0] != 0:
            if a[posiçãoAgente[0]-1][posiçãoAgente[1]] == 2:
                print('Você esta sentindo fedor')
        if posiçãoAgente[1] != numero_colunas-1:
            if a[posiçãoAgente[0]][posiçãoAgente[1]+1] == 2:
                print('Você esta sentindo fedor')
        if posiçãoAgente[1] != 0:
            if a[posiçãoAgente[0]][posiçãoAgente[1]-1] == 2:
                print('Você esta sentindo fedor')
        
        if posiçãoAgente[0] != numero_linhas-1:
            if a[posiçãoAgente[0]+1][posiçãoAgente[1]] == 3:
                print('Você esta sentindo uma brisa')
        if posiçãoAgente[0] != 0:
            if a[posiçãoAgente[0]-1][posiçãoAgente[1]] == 3:
                print('Você esta sentindo uma brisa')
        if posiçãoAgente[1] != numero_colunas-1:
            if a[posiçãoAgente[0]][posiçãoAgente[1]+1] == 3:
                print('Você esta sentindo uma brisa')
        if posiçãoAgente[1] != 0:
            if a[posiçãoAgente[0]][posiçãoAgente[1]-1] == 3:
                print('Você esta sentindo uma brisa')
        
        if posiçãoAgente == posiçãoOuro:
            bousa = 1
        
    
        if bousa == 1:
            print('Você esta com o ouro volte para o inicio!')
        print('use W-para subir, A-para ir a esquerda, S-para descer, D- para ir a direita')
        mov = input('qual o seu movimento: ').lower().strip()[0]
        os.system('cls')
        if mov == 'w' and posiçãoAgente[0] != 0:
            break
        if mov == 's' and posiçãoAgente[0] != (numero_linhas -1):
            break
        if mov == 'a' and posiçãoAgente[1] != 0:
            break
        if mov == 'd' and posiçãoAgente[1] != (numero_colunas - 1):
            break
    if mov == 'w':
        a[posiçãoAgente[0]][posiçãoAgente[1]] = 0
        posiçãoAgente[0] = posiçãoAgente[0] -1
    if mov == 's':
        a[posiçãoAgente[0]][posiçãoAgente[1]] = 0
        posiçãoAgente[0] = posiçãoAgente[0] +1
    if mov == 'd':
        a[posiçãoAgente[0]][posiçãoAgente[1]] = 0
        posiçãoAgente[1] = posiçãoAgente[1] +1
    if mov == 'a':
        a[posiçãoAgente[0]][posiçãoAgente[1]] = 0
        posiçãoAgente[1] = posiçãoAgente[1] -1
    if bousa != 0 and posiçãoAgente[0] == numero_linhas-1 and posiçãoAgente[1] == 0:
        break
    if posiçãoAgente == posiçãoWumpus:
        w = 1
        break
    if posiçãoAgente == posiçãoBuraco[0] or posiçãoAgente == posiçãoBuraco[1] or posiçãoAgente == posiçãoBuraco[2] or posiçãoAgente == posiçãoBuraco[3]:
        b = 1
        break
if w == 1:
    print('O Wumpus te pegou!')
elif b == 1:
    print('Você caiu no buraco!')
elif bousa == 1:
    print('Parabens, vc ganhou!')