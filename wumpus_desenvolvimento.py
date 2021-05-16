import os
from random import randint
global po
# n_linhas = int(input('qual o tamanho da matriz: (exp.: 3 para 3x3 ou 5 pra 5x5) '))# recebe numero de linhas
n_colunas = n_linhas = 5 # recebe o numero de colunas 
valor = 0 #int(input('qual o valor a ser preenchido: '))
pa = [n_linhas-1,0]
po = list()
pw = list()
pb = list()
bousa = w = b = 0
os.system('cls')
print('='*143)
print(' '*30 + 'Bem vindo ao mundo de Wumpus!')
print(' '*30 + 'encontre o ouro')
print(' '*30 + 'tome cuidado para não cair nos buracos, eles emanam vento')
print(' '*30 + 'o Wumpus é fedorento, então muito cuidado!\n')
print('='*143)
pausa = input(' '*30 + 'de enter para começar o jogo')
os.system('cls')
def crie_matriz(n_linhas, n_colunas, valor):
    matriz = list() # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = list() # lista vazia
        for j in range(n_colunas):
            linha.append(valor)
        # coloque linha na matriz
        matriz.append(linha)
    matriz[n_linhas-1][0] = 1
    while True:
        l = randint(0,n_linhas-1)
        c = randint(0,n_colunas-1)
        
        if matriz[l][c] == 0:
            matriz[l][c] = 2
            pw.append(l)
            pw.append(c)
            #print(f'wumpus na:[{l}][{c}]')
            break
            
    for z in range(n_linhas-1):
        while True:
            l = randint(0,n_linhas-1)
            c = randint(0,n_colunas-1)
            L = list()
            if matriz[l][c] == 0:
                matriz[l][c] = 3
                #print(f'buraco na:[{l}][{c}]')
                L.append(l)
                L.append(c)
                pb.append(L)
                break 
    while True:
        l = randint(0,n_linhas-1)
        c = randint(0,n_colunas-1)
        if matriz[l][c] == 0:
            matriz[l][c] = 4    
            po.append(l)
            po.append(c)
            #print(f'ouro na:  [{l}][{c}]')
            break
    return matriz

a = crie_matriz(n_linhas, n_colunas, valor)# chama a função para criar a matriz

while True:
    #movimentação do agente
    mov = 'z'
    while True:
        a[pa[0]][pa[1]] = 1
        #laços para printar a matriz
        for l in range(n_linhas):
            for c in range(n_colunas):
                if a[l][c] == 0 or a[l][c] == 2 or a[l][c] == 3 or a[l][c] == 4:
                    print('[ ]', end='')
                if a[l][c] == 1:
                    print('[A]', end='')
                # if a[l][c] == 2:
                #     print('[W]', end='')
                # if a[l][c] == 3:
                #     print('[B]', end='')
                # if a[l][c] == 4:
                #     print('[O]', end='')
            print()
        if pa[0] != n_linhas-1:
            if a[pa[0]+1][pa[1]] == 2:
                print('Você esta sentindo fedor')
        if pa[0] != 0:
            if a[pa[0]-1][pa[1]] == 2:
                print('Você esta sentindo fedor')
        if pa[1] != n_colunas-1:
            if a[pa[0]][pa[1]+1] == 2:
                print('Você esta sentindo fedor')
        if pa[1] != 0:
            if a[pa[0]][pa[1]-1] == 2:
                print('Você esta sentindo fedor')
        
        if pa[0] != n_linhas-1:
            if a[pa[0]+1][pa[1]] == 3:
                print('Você esta sentindo uma brisa')
        if pa[0] != 0:
            if a[pa[0]-1][pa[1]] == 3:
                print('Você esta sentindo uma brisa')
        if pa[1] != n_colunas-1:
            if a[pa[0]][pa[1]+1] == 3:
                print('Você esta sentindo uma brisa')
        if pa[1] != 0:
            if a[pa[0]][pa[1]-1] == 3:
                print('Você esta sentindo uma brisa')
        
        if pa == po:
            bousa = 1
        
    
        if bousa == 1:
            print('Você esta com o ouro volte para o inicio!')
        print('use W-para subir, A-para ir a esquerda, S-para descer, D- para ir a direita')
        mov = input('qual o seu movimento: ').lower().strip()[0]
        os.system('cls')
        if mov == 'w' and pa[0] != 0:
            break
        if mov == 's' and pa[0] != (n_linhas -1):
            break
        if mov == 'a' and pa[1] != 0:
            break
        if mov == 'd' and pa[1] != (n_colunas - 1):
            break
    if mov == 'w':
        a[pa[0]][pa[1]] = 0
        pa[0] = pa[0] -1
    if mov == 's':
        a[pa[0]][pa[1]] = 0
        pa[0] = pa[0] +1
    if mov == 'd':
        a[pa[0]][pa[1]] = 0
        pa[1] = pa[1] +1
    if mov == 'a':
        a[pa[0]][pa[1]] = 0
        pa[1] = pa[1] -1

    if bousa != 0 and pa[0] == n_linhas-1 and pa[1] == 0:
        break
    if pa == pw:
        w = 1
        break
    if pa == pb[0] or pa == pb[1] or pa == pb[2] or pa == pb[3]:
        b = 1
        break
if w == 1:
    print('O Wumpus te pegou!')
elif b == 1:
    print('Você caiu no buraco!')
elif bousa == 1:
    print('Parabens, vc ganhou!')
