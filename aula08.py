from datetime import date
def voto(AnoDeNascimento): 
    anoAtual = date.today().year
    idade = anoAtual - AnoDeNascimento
    voto = ''
    if idade < 0:
        voto = 'data de nascimento invalido'
    else:
        if idade < 16:
            voto = 'VOTO NEGADO'
        elif idade < 18:
            voto = 'VOTO OPCIONAL'
        else:
            voto = 'VOTO OBRIGATORIO'

    return voto

anoDeNascimento = int(input('quando foi que vc nasceu: '))
voto = voto(anoDeNascimento)
print(f'{voto}')

print(f'----------------------------------------------------------------------')

