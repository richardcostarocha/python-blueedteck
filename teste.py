
'''
a = [[]]

for l in range(0,3):
    for c in range(0,3):
        a[l][c] = int(input(f'digite um valor para [{l},{c}]: '))

print('='*166)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{a[l][c]}]', end='')
    print()
'''

# n_linhas = int(input('quantas linhas tem a matriz: '))
# n_colunas = int(input('quantas colunas tem a matriz: '))
# valor = int(input('qual o valor a ser preenchido: '))

# def crie_matriz(n_linhas, n_colunas, valor):
#     matriz = [] # lista vazia
#     for i in range(n_linhas):
#         # cria a linha i
#         linha = [] # lista vazia
#         for j in range(n_colunas):
#             linha.append(valor)

#         # coloque linha na matriz
#         matriz.append(linha)

#     return matriz
# a = crie_matriz(n_linhas, n_colunas, valor)
# for l in range(n_linhas):
#     for c in range(n_colunas):
#         print(f'[{a[l][c]}]', end='')
#     print()

# for c in range(0,5):
#     print('ola')

n = 0
    


def breakq():
    breakq = input('deseja continuar? [sim ou não] ')
    if breakq == 'sim':
         n = 0
    
    else:
         n = 1
    return n

while n == 0:
   print('ola')
   breakq()
