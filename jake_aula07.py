#Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. 
# Se eles forem iguais, imprima que são valores idênticos.

# def menor(n1,n2):
#     if n1 < n2:
#         print(n1)
#     elif n2 < n1:
#         print(n2)
#     else:
#         print(n1,n2)

# n1 = int(input('digite o primeiro valor: '))
# n2 = int(input('digite o segundo valor: '))

# menor(n1,n2)

#Escreva uma função que recebe dois números (a e b) como parâmetro 
#e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.

# def somaMaior(n1,n2,limite):
#     soma = n1 + n2
#     if soma > limite:
#         return True
#     else:
#         return False
# n1 = int(input('digite o primeiro valor: '))
# n2 = int(input('digite o segundo valor: '))
# limite = int(input('digite um limite: '))
# print(somaMaior(n1,n2,limite))

#Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. 
#Faça uma chamada à função, passando como parâmetro uma string.

# def maiuscula(frase):
#     fraseMaiuscula = frase.upper()
#     return fraseMaiuscula
# print(maiuscula(input('digite uma frase para por em Maiuscula: ')))

#Crie um programa que tenha uma função chamada voto () que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. 
#Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.

# import datetime
# def voto(anoDeNascimento):
#     anoAtual = datetime.datetime.today().year
#     idade = anoAtual - anoDeNascimento
#     if idade < 16:
#         print('VOTO NEGADO')
#     elif idade >=16 and idade < 18:
#         print('VOTO OPCIONAL')
#     else:
#         print('VOTO OBRIGATORIO')

# anoDeNascimento = int(input('digite o ano noque vc nasceu: '))
# voto(anoDeNascimento)

# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: 
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

# def ficha(jogador,gols):
#     print(f'nome do jogador: {jogador}')
#     print(f'quantos gols o jogador marcou: {gols}')
# jogador = input('qual o nome do jogador: ')
# gols = int(input('quantos gols foi marcado: '))
# ficha(jogador,gols)

#Um professor, muito legal, fez 3 provas durante um semestre,
# mas só vai levar em conta as duas notas mais altas para calcular a média.
# Faça uma aplicação que peça o valor das 3  notas
# , mostre como seria a média com essas 3 provas, a média com as 2 notas mais altas,
# bem como sua nota mais alta e sua nota mais baixa.

# def notas(a, b, c):
#     med = (a + b + c) / 3 
#     print(f'A média das três notas seria: {med}')
#     lista = [a, b, c]
#     med_altas = ((a + b + c) - (min(lista))) / 2
#     print(f'A nota mais alta foi: {max(lista)}')
#     print(f'A média com as duas notas mais altas é: {med_altas}')
#     print(f'Sua nota mais baixa foi: {min(lista)}')


# a = float(input('Digite a nota 1: '))
# b = float(input('Digite a nota 2: '))
# c = float(input('Digite a nota 3: '))

# notas(a, b, c)

# def gastoViagem(noites,custo_aviao,custo_carro,gastos_extras):
