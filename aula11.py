# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, 
# pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso
import os
dados = list()
termino = ''
pessoa = list()
os.system('cls')
while True:
    pessoa.append(str(input('nome: ')))
    pessoa.append(str(input('peso: ')))
    dados.append(pessoa)
    while True:
        termino = input('deseja continuar? [sim ou não] ').lower().strip()[0]
        os.system('cls')
        if termino in 'sn':
            break 
    if termino == 'n':
        break   
    
print(f'{len(dados)} pessoas ja cadastradas!')