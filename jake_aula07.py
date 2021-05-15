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

# Escrever uma aplicação utilizando funções que calcule os gastos com passagem, hospedagem,
# aluguel de carro e gastos extras de uma viagem para uma determinada cidade.

# def gastoViagem():
#     noites = int(input('quantas noites vai passar no hotel: '))
#     def custo_hotel(noites):
#         custo_hotel = noites*140
#         return custo_hotel
#     print('Preço das passagens de avião:')
#     print('São Paulo custa R$ 312,00')
#     print('Porto Alegre custa R$ 447,00')
#     print('Recife custa R$ 831,00')
#     print('Manaus custa R$ 986,00')
#     cidade = input('para qual cidade você vai viajar? ').lower().strip()
#     def custo_aviao(cidade):
#         if cidade == 'são paulo':
#             custo_aviao = 312
#         elif cidade == 'porto alegre':
#             custo_aviao = 447
#         elif cidade == 'recife':
#             custo_aviao = 831
#         elif cidade == 'manaus':
#             custo_aviao = 986
#         return custo_aviao
#     dias = int(input('por quantos dias vc deseja alugar um carro? '))
#     def custo_carro(dias):
#         aluguel_carro = 0
#         aluguel_carro = aluguel_carro * 40
#         if dias >= 3 and dias < 7:
#             aluguel_carro -= 20
#         elif dias >= 7:
#             aluguel_carro -= 50
#         return aluguel_carro
#     gastos_extras = float(input('quanto dee gastos extras teve na viajem? '))
#     valor_total = custo_aviao(cidade) + custo_carro(dias) + custo_hotel(noites) + gastos_extras
#     return valor_total

# print(f'o valor total da viagem é de {gastoViagem()}')
