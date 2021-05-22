sexo = input('digite F pra feminino e M pra Masculinio: ').upper()

while sexo not in 'FM':

    if sexo != 'F':
        if sexo != 'M':
            print('tente novamente: ' )
            sexo = input('digite F pra feminino e M pra Masculinio: ').upper()
    if sexo == 'F':
            print('pessoa do sexo Feminino {sexo}')
    if sexo == 'M':
            print('pessoa do sexo Masculino {sexo}')