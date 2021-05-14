#01

# tabuada = int(input('qual a tabuada que vc quer ver? '))
# n1 = tabuada * 10
# for c in range(tabuada,n1+1,tabuada):
#     print(c)

#02

# for c in range(10,0,-1):
#     print(c)

#03

# status = list()
# for c in range(15):
#     status.append(input('qual o seu estado civil (Solteiro / Casado)? ').lower())
# casado = status.count('casado')
# solteiro = status.count('solteiro')
# print(f'tem {casado} casados!')
# print(f'tem {solteiro} souteiros!')

#04

# for c in range(10):
#     print('Go Blue')

#05

# for c in range(0,21):
#     if c % 2 != 0:
#         print(c)

#06

# preçoUnico = float(input('qual  valor de 1 pão: ').replace(',','.'))
# for c in range(50):
#     preço = (c+1)*preçoUnico
#     print(f'preço de {c+1} pães é R${preço:.2f}')

#07

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

#09

# import itertools
# lista = []
# for i in range(1,61):
#     lista.append(i)


# for subset in itertools.combinations(lista, 6):
#     print(subset)

#desafio01

# centezimo = 0
# decimo = 0
# total = 0
# for c in range(1000,10000):
#     centezimoI = c // 100
#     centezimo = centezimoI*100
#     decimo = c - centezimo
#     total = centezimoI + decimo
#     i = total**2
#     if i == c:
#         print(i)

#desafio 2

# i = int(input('quantas materias tem sua aula: '))
# notas = list()
# for c in range(i):
#     notas.append(float(input('qual a nota: ').replace(',','.')))
# soma = sum(notas)
# media = soma/i
# print(f'a media geral é: {media}')