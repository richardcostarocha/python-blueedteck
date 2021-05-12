#01
'''
import time
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)

'''
#02
'''
frase = input('digite uma frase: ').lower()
a = 0
e = 0
i = 0
o = 0
u = 0
for c in frase:
    if c == 'a':
        a += 1
    elif c == 'e':
        e += 1
    elif c == 'i':
        i += 1
    elif c == "o":
        o += 1
    elif c == "u":
        u += 1
    
print(f'tem {a} vogais a')
print(f'tem {e} vogais e')
print(f'tem {i} vogais i')
print(f'tem {o} vogais o')
print(f'tem {u} vogais u')

'''
#03
'''
n = int(input('digite o num ao qual vc quer saber o divisor: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'{c} é um divisor de {n}')
'''
#04
frase = input('digite uma frase: ')
for c in 'aeiou':
    frase = frase.replace(c,'')
print(frase)