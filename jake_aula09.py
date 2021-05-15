# 1. Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.

# tabuada = int(input('qual a tabuada que vc quer ver? '))
# n1 = tabuada * 10
# for c in range(tabuada,n1+1,tabuada):
#     print(c)

# 2. Elaborar um programa para imprimir os números de 1 (inclusive) até 10 (inclusive) em ordem decrescente. 

# for c in range(10,0,-1):
#     print(c)

# 3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) 
# e mostre ao final a quantidade de pessoas de cada estado civil. 

# status = list()
# for c in range(15):
#     status.append(input('qual o seu estado civil (Solteiro / Casado)? ').lower())
# casado = status.count('casado')
# solteiro = status.count('solteiro')
# print(f'tem {casado} casados!')
# print(f'tem {solteiro} souteiros!')

# 4. Faça um algoritmo que imprima 10 vezes a frase: “Go Blue”. 

# for c in range(10):
#     print('Go Blue')

# 5. Faça um programa que mostre os valores numéricos inteiros ímpares situados na faixa de 0 a 20. 

# for c in range(0,21):
#     if c % 2 != 0:
#         print(c)

# 6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha,
# que já é um sucesso na sua loja de 1,99.
# Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães,
# a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo: 
 
# preçoUnico = float(input('qual  valor de 1 pão: ').replace(',','.'))
# for c in range(50):
#     preço = (c+1)*preçoUnico
#     print(f'preço de {c+1} pães é R${preço:.2f}')

# 7. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar.
# O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
# para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
# para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo: 

# import os
# while True:
#     pausa = ''
#     preço = avista = troco = 1
#     compras = list()
#     while preço != 0:
#         preço = float(input('qual o valor da mercadoria: '))
#         compras.append(preço)
#     print(f'o total da compra é {sum(compras)}')
#     avista = float(input('quanto o cliente deu para pagamento: '))
#     troco = avista - sum(compras) 
#     print(f'troco: {troco}')
#     pausa = input('de um enter para continuar!')
#     os.system('cls')

# 8. Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# ○ “Telefonou para a vítima?”
# ○ “Esteve no local do crime?”
# ○ “Mora perto da vítima?”
# ○ “Devia para a vítima?”
# ○ “Já trabalhou com a vítima?”
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como “Suspeita”,
#  entre 3 e 4 como “Cúmplice” e 5 como “Assassino”. Caso contrário, ele será classificado como “Inocente”.

# resporta = list()
# resporta.append(input('Telefonou para a vítima? ').lower())
# resporta.append(input('Esteve no local do crime? ').lower())
# resporta.append(input('Mora perto da vítima? ').lower())
# resporta.append(input('Devia para a vítima? ').lower())
# resporta.append(input('Já trabalhou com a vítima? ').lower())

# if resporta.count('sim') == 2:
#     print('Suspeita')
# elif resporta.count('sim') == 3 or resporta.count('sim') == 4:
#     print('Cúmplice')
# elif resporta.count('sim') == 5:
#     print('Assassino')
# else:
#     print('Inocente')

# 9. Faça um script em Python que exiba todos os possíveis palpites da Mega-Sena.
# ⦁	#Dados:
# ⦁	#Cada palpite possui 6 dezenas
# ⦁	#As dezenas variam de 1 até 60
# ⦁	#Não pode repetir dezena

# import itertools
# lista = []
# for i in range(1,61):
#     lista.append(i)
# for subset in itertools.combinations(lista, 6):
#     print(subset)

# Desafio 1 - Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números
# de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.
# Exemplo: 3025 = 55 e 55**2 é igual á 3025

# i = 0
# for c in range(1000,10000):
#     i = (c // 100 + c % 100)**2
#     if i == c:
#         print(i)

# Desafio 2 - Faça um script que peça ao usuário o número de matérias da escola, ou seja, um inteiro positivo.
# Em seguida, ele vai digitando o valor de cada nota, de cada matéria e isso será armazenado numa lista.
# Ao final, seu script deverá fornecer a média geral do aluno.

# i = int(input('quantas materias tem sua aula: '))
# notas = list()
# for c in range(i):
#     notas.append(float(input('qual a nota: ').replace(',','.')))
# soma = sum(notas)
# media = soma/i
# print(f'a media geral é: {media}')