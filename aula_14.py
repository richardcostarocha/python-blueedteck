""" Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 
(que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.​
{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  ​ """


""" Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e 
cada valor associado é o número ao quadrado.​
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}  """

""" Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. 
 Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
 """
# from os import system
# ficha = list()
# aluno = dict()
# tamanho = 0
# system('cls')
# while True:
#     resp = ''
#     aluno['nome'] = str(input('nome do aluno: '))
#     aluno['media'] = float(input('media do aluno: '))
#     if aluno['media'] >= 7:
#         aluno['situação'] = 'aprovado'
#     if 5 <= aluno['media'] < 7:
#         aluno['situação'] = 'recuperação'
#     if aluno['media'] < 5:
#         aluno['situação'] = 'reprovado'
#     ficha.append(aluno.copy())
#     tamanho += 1
#     while resp != 'S' and resp != 'N':
#         resp = str(input('deseja continuar cadastrando: [S/N] ')).upper().strip()[0]
#         system('cls')
#     if resp == 'N':
#         break
# for c in range(tamanho):
#     print(f"aluno: {ficha[c]['nome']}\nmedia: {ficha[c]['media']}\nresultado: {ficha[c]['situação']}")

""" Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(),
 sleep() e itemgetter da bliblioteca operator.
 """
from os import system
# from operator import itemgetter
# from random import randint
# system('cls')
# rank = dict()
# jogadores = dict()
# jogadores['jogador1'] = randint(1,6)
# jogadores['jogador2'] = randint(1,6)
# jogadores['jogador3'] = randint(1,6)
# jogadores['jogador4'] = randint(1,6)
# rank = sorted(jogadores.items(), key=itemgetter(1),reverse=True)
# for i , v in enumerate(rank):
#     print(f'{i+1}º lugar:{v[0]} tirou {v[1]}')

""" Crie um programa que leia nome, ano de nascimento e carteira de trabalho 
  e cadastre-os (com idade) em um dicionário.
  Se por acaso a CTPS for diferente de 0, o dicionário receberá também 
  o ano de contratação e o salário.
  Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar.
  Considere que o trabalhador deve contribuir por 35 anos para se aposentar.​​
 """
system('cls')
from datetime import date
anoAtual = date.today().year
funcionario = dict()
funcionario['nome'] = str(input('nome: '))
nascimento = int(input('ano de nascimento: '))
idade = anoAtual - nascimento
funcionario['idade'] = idade
funcionario['CTPS'] = int(input('carteira de trabalho: '))
if funcionario['CTPS'] != 0:
    contratação = int(input('ano de contratação: '))
    anoDeContratação = anoAtual - contratação
    funcionario['anoDeContratação'] = anoDeContratação
    funcionario['salario'] = float(input('salario: '))
    aposentadoria = 35 - funcionario.get('anoDeContratação')
    aposentado = idade + aposentadoria
    funcionario['aposentadoria'] = aposentado
print(funcionario)


""" DESAFIO: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre:​
A) Quantas pessoas estão cadastradas.​
B) A média da idade.​
C) Uma lista com as mulheres.​
D) Uma lista com as idades que estão acima da média.​
OBS:O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário
 se deseja continuar a resposta seja somente sim ou não.​
 """