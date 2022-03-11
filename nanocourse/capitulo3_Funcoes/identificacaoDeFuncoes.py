def preencherIventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento=[input('Equipamentos: '),
                     float(input('Valor: ')),
                     int(input('Número Serial: ')),
                     input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite "S" para continuar: ').upper()

def exibirInventario(lista):
    for elemento in lista:
        print('Nome..........: ',  elemento[0])
        print('Valor.........: ', elemento[1])
        print('Serial........: ', elemento[2])
        print('Departamento..:', elemento[3])

def localizarPorNome(lista):
    busca = input('Digite o nome do que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print('Valor....:', elemento[1])
            print('Serial.........:', elemento[2])

def depreciarPorNome(lista, porc):
    depreciar = input('Digite o nome do que deseja depreciar: ')
    for elemento in lista:
        if depreciar == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print('Valor atual: ', elemento[1])

def excluirPorSerial(lista):
    excluir = int(input('Digite o serial do produto que você deseja excluir: '))
    for elemento in lista:
        if excluir == elemento[2]:
            lista.remove(elemento)
    return 'Itens excuídos.'

def resumirValores(lista):
    valores=[]
    for elemento in lista:
        valores.append(elemento[1])
        print('O equipamento mais caro custa: ', max(valores))
        print('O equipamento mais barato custa: ', min(valores))
        print('O total de equipamentos é de: ', sum(valores))


