#01 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
#  que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
import os
from time import sleep
os.system('cls')
valor = [list(),list()]
for i in range(7):
   alx = 0
   alx =int(input('digite um valor: '))
   if alx % 2 == 0:
      valor[0].append(alx)
   else:
      valor[1].append(alx)
valor[0].sort()
valor[1].sort()
print(f'os numers pares em ordem crescente é: {valor[0]}')
print(f'os numers inpares em ordem crescente é: {valor[1]}')
sleep(5)
os.system('cls')
   # - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
   #  No final, mostre a matriz na tela, com essa formatação:
"""  
[  1  ][  2  ][  3  ]
[  4  ][  5  ][  6  ]
[  7  ][  8  ][  9  ] 

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[coluna][linha]) 
 """
matriz = list()
for i in range(3):
   linha = list()
   for j in range(3):
      linha.append(int(input('digite um valor: ')))
   matriz.append(linha)

for l in range(3):
   for c in range(3):
      print(f'[{matriz[l][c]}]', end='')
   print()
sleep(5)
os.system('cls')
#03 - Aprimore o desafio anterior, mostrando no final:
   # A) A soma de todos os valores pares digitados.
   # B) A soma dos valores da terceira coluna. 
   # C) O maior valor da segunda linha.
matriz = list()
SomaPar = SomaTerceira = Maior = alx = 0
for i in range(3):
   linha = list()
   for j in range(3):
      alx = int(input('digite um valor: '))
      if alx%2 == 0:
         SomaPar += alx
      if j == 2:
         SomaTerceira += alx
      linha.append(alx)

   matriz.append(linha)
for i in range(3):
   if i == 0:
      Maior = matriz[1][i]
   elif matriz[1][i] > Maior:
      Maior = matriz[1][i]
for l in range(3):
   for c in range(3):
      print(f'[{matriz[l][c]}]', end='')
   print()
print(f'A soma de todos os valores pares digitados: {SomaPar}')
print(f'A soma dos valores da terceira coluna: {SomaTerceira}')
print(f'O maior valor da segunda linha:{Maior}')
sleep(5)
os.system('cls')
#04 - Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
jogos = int(input('quantos jogos vc deseja gerar: '))
for i in range(jogos):
   JogoGerado = list()
   alx = 0
   while True:
      alx = randint(1,60)
      if alx not in JogoGerado:
         JogoGerado.append(alx)
      if len(JogoGerado) == 6:
         break
      
            
   print(f'o jogo de numero {i+1} é = {JogoGerado}')
   sleep(1)

