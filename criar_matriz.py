
n_linhas = int(input('quantas linhas tem a matriz: '))
n_colunas = int(input('quantas colunas tem a matriz: '))
valor = int(input('qual o valor a ser preenchido: '))

def crie_matriz(n_linhas, n_colunas, valor):
    matriz = [] # lista vazia
    for i in range(n_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(n_colunas):
            linha.append(valor)

        # coloque linha na matriz
        matriz.append(linha)

    return matriz
a = crie_matriz(n_linhas, n_colunas, valor)
for l in range(n_linhas):
    for c in range(n_colunas):
        print(f'[{a[l][c]}]', end='')
    print()
