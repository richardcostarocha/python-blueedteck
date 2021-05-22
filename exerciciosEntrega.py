#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o 
   # resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
from os import system
""" n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
print(f'a soma é: {n1+n2}')
print(f'a divisão entre {n1} com {n2} é: {n1/n2}')
if n1>n2:
   print(f'{n1} é maior que {n2}')
else:
   print(f'{n2} é maior que {n1}')
if (n1+n2)%2 == 0:
   print(f'a soma de {n1} com {n2} é par')
else:
   print(f'a soma de {n1} com {n2} é impar')
if (n1*n2)>40:
   print(f'resultado: {(n1*n2)/(n1//n2)}')
else:
   print(f'a muliplicação entre {n1} com {n2} não é maior que 40')
system('cls') """
#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com 
# uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, 
# depois mostre na tela essa mesma frase sem nenhuma vogal.
""" frase = str(input('digite uma frase: ')).lower()
cont = 0
for i in frase:
   if i in 'aeiou':
      cont +=1
print(f'na frase tem {cont} vogais')
for i in 'aeiou':
   frase.replace(i,' ')
print(f' a frase sem as vogas fica: {frase}') """
#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar
#  seu processamento, só deixe o usuário continuar se a senha estiver correta,
#  após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação,
#  onde o computador vai “pensar” em um número entre 0 e 10.
#  O jogador vai tentar adivinhar qual número foi escolhido até acertar,
#  a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou,
#  no final mostre quantos palpites foram necessários para vencer.
""" from random import randint
senha = 'richard gostosão'
comp = randint(0,10)
erro = 0
senhateste = ''
senhateste = str(input('digite a senha: '))
while senhateste != senha:
   system('cls')
   senhateste = str(input('senha invalida!\ndica: "criador gostosão"\ndigite a senha: '))
print('\33[33;41m')
print('============')
print('|Bem Vindo!|')
print('============')
print('\33[m')
print('\33[7m')
usuario = int(input('tente adivinhar qual foi o numero que o pc escolheu(dica: foi um numero de 0 a 10): '))
while usuario != comp:
   erro += 1
   if usuario > comp:
      print('seu numero foi maior!')
   else:
      print('seu numero foi menor!')
   usuario = int(input('vc errou, tente novamente: '))
print(f'vc precisou de {erro} vezes para acertar o numero {comp}')
print('\33[m') """
#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string 
# no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja 
# inválida.

#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o
#  resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.

#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
#  mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) 
# em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação 
# e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar.
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
