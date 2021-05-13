#01
'''
from random import randint 
a = (randint(1,50),randint(1,50),randint(1,50),randint(1,50),randint(1,50))
print(a)
b = sorted(a)
print(f'o menor numero é {b[0]}')
print(f'o maior numero é {b[4]}')
#'''
#02
#'''
n1 = int(input('digite um valor: '))
n2 = int(input('digite um valor: '))
n3 = int(input('digite um valor: '))
n4 = int(input('digite um valor: '))
a = (n1,n2,n3,n4)
nove = 0
for c in range(0,4):
    if a[c] == 9:
        nove += 1
print(f'tem {nove} noves')
print(f'o primeiro 3 esta na posição {a.index(3)}')
