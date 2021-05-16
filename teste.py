""" Exercício

Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. """

esc = 1
contIdade = 0
contM = 0
M20 = 0
while esc == 1:
    print('\033[04;37m-=-'*20)
    sexo = int(input('''Escolha o seu gênero
    [ 0 ] para FEMININO
    [ 1 ] para MASCULINO
    ->:  '''))
    print('-=-'*20)
    if sexo == 1:
        contM+=1
    idade = int(input('Digite sua idade: '))
    print('-=-'*20)
    if idade > 18:
        contIdade+=1
    if sexo == 0 and idade < 20:
        M20+=1
    fim = int(input('''\033[04;31mDeseja continuar?
    [ 1 ] para CONTINUAR
    [ 0 ] para ENCERRAR
    ->:  '''))
    esc = fim*esc
print('\033[04;37m-=-'*20)
print('''Foram cadastrados {} homens
{} pessoas com mais de 18 anos
e {} mulheres com menos de 20 anos.'''.format(contM, contIdade, M20))
print('-=-'*20)