
n_linhas = int(input('quantas linhas tem a matriz: '))# recebe numero de linhas
n_colunas = int(input('quantas colunas tem a matriz: '))# recebe o numero de colunas 
valor = int(input('qual o valor a ser preenchido: '))

def crie_matriz(n_linhas, n_colunas, valor):
    matriz = list()
    for i in range(n_linhas):
        linha = list()
        for j in range(n_colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz

a = crie_matriz(n_linhas, n_colunas, valor)
for l in range(n_linhas):
    for c in range(n_colunas):
        print(f'[{a[l][c]}]', end='')
    print()
