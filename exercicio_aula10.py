#01

import os
from random import randint
# senha = 'python'
# n = 0 
# while n == 0:

#     print('dica: programação')
#     teste = input('qual é a sua senha:')
#     if teste == senha:
#         n = 1
#     os.system('cls')
#     print('senha incorreta!')
# os.system('cls') 
# print('Bem vindo!')

#02

# n = 0
# while n == 0:
#     sexo = input('qual o seu sexo? [F|M] ').strip().upper()
#     os.system('cls')
#     if sexo == 'F' or sexo == 'M':
#         n = 1
# if sexo == 'F':
#     print(f'você afirmou que é {sexo} de Feminino')
# if sexo == 'M':
#     print(f'você afirmou que é {sexo} de Masculino')

#03

# from random import randint
# n1 = randint(0,10)
# n2 = -1
# c = 0
# while n1 != n2:
#     print('Ola, vamos brincar')
#     print('Eu pensei num numero de 0 a 10, consegue descobrir qual foi?')
#     n2 = int(input('qual o numero que o computador pensou? '))
#     c += 1
#     os.system('cls')
# print(f'você precisou de {c} chances pra descobrir o valor')

#desafio
c = 0
c1 = 'sim'
v = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
vn = 0
vb = 0
while c == 0:
    while v < 1 or v > 6:
        print('-----------------------') 
        print('| 1 - Rafael          |')
        print('| 2 - Vanessa         |')
        print('| 3 - David           |')
        print('| 4 - Richard         |')
        print('| 5 - Voto nulo       |')
        print('| 6 - Voto em branco  |')
        print('-----------------------')
        v = int(input('qual o seu voto: [1-6] '))
        os.system('cls')
    if v == 1:
        c1 += 1
    if v == 2:
        c2 += 1
    if v == 3:
        c3 += 1
    if v == 4:
        c4 += 1
    if v == 5:
        vn += 1
    if v == 6:
        vb += 1
    while c1 == 'sim':
        c1 = input('deseja continuar com a votação? [sim ou não]').lower().strip().replace('a','ã')
    if c1 == 'não':
        c = 1
