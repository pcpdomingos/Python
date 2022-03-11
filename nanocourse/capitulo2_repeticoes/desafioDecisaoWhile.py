genero = input('Digite o gênero: ').upper()
resposta='SIM'
while resposta == 'SIM':
    if genero == 'MASCULINO':
        nivel = input('Digite o nível: ').upper()
        if nivel == 'ADM':
            print('Olá Administrador.')
        elif nivel == 'USR':
            print('Olá Usuário.')
        elif nivel == 'GUEST':
            print('Olá Visitante.')
        else:
            print('Olá Desconhecido(a).')


    elif genero == 'FEMININO':
        nivel = input('Digite o nível: ').upper()
        if nivel == 'ADM':
            print('Olá Administradora.')
        elif nivel == 'USR':
            print('Olá Usária.')
        elif nivel == 'GUEST':
            print('Olá Visitante.')
        else:
            print('Olá Desconhecido(a).')

    else:
        print('Digite o gênero MASCULINO ou FEMININO.')
    resposta=input('Digite SIM para continuar: ').upper()

