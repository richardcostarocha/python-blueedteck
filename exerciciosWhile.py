# NÃO PODE UTILIZAR LISTAS COMPOSTAS, NEM DICIONÁRIOS, APENAS WHILE:

#01 - Crie um programa que leia dois valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)
from os import system
from time import sleep
system('cls')
def soma(var1,var2):
   soma = var1 + var2
   return soma
def mult(var1,var2):
   mult = var1*var2
   return mult
def mudarVar():
   var1 = int(input('digite um valor: '))
   var2 = int(input('digite outro valor: '))
   return (var1,var2)
def maior(var1,var2):
   if var1 > var2:
      maior = var1
   else:
      maior = var2
   return maior
var1,var2 = mudarVar()
system('cls')
saida= 0

while saida != 5:
   saida2 = 0
   while saida2 != 1 and saida2 != 2 and saida2 != 3 and saida2 != 4 and saida2 != 5:
      saida2 = int(input('''
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa
      
      Escolha uma opção: '''))
      system('cls')
      if saida2 != 1 and saida2 != 2 and saida2 != 3 and saida2 != 4 and saida2 != 5:
         print('opção invalida! digite novamente!')
      else:
         saida = saida2
   if saida == 1:
      print(f'a soma do seus valores é: {soma(var1,var2)}')
   if saida == 2:
      print(f'a multiplicação do seus valores é: {mult(var1,var2)}')
   if saida == 3:
      print(f'o maior numero entre os seus valores é: {maior(var1,var2)}')
   if saida == 4:
      var1,var2 = mudarVar()
print('Obrigado, volte sempre!')
sleep(30)
system('cls')
#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, 
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.
total18 = TotalHomens = TotalMulheres20 = 0
while True:
   idade = int(input('idade: '))
   sexo = ' '
   while sexo not in 'MF':
      sexo = input('Sexo: [M/F]').strip().upper()[0]
   if idade >= 18:
      total18 += 1
   if sexo == 'M':
      TotalHomens += 1
   if sexo == 'F' and idade < 20:
      TotalMulheres20 += 1
   resp = ' '
   while resp not in 'SN':    
      resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
   if resp == 'N':
      break
   system('cls')

print(f'Total de pessoas maiores de 18 anos: {total18}')
print(f'Ao todo temos: {TotalHomens} cadastrados.')
print(f'Temos {TotalMulheres20} de mulheres com menos de 20 anos')
sleep(5)
system('cls')
#03 - Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
# continuar ou não. No final, mostre:
   # A) qual é o total gasto na compra.
   # B) quantos produtos custam mais de R$1000.
   # C) qual é o nome do produto mais barato.

