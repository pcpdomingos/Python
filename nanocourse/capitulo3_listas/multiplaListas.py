resposta = 'S'
list_equipamento = []
list_valor = []
list_numserial = []
list_departamento = []

while resposta == 'S':
    list_departamento.append(input('Digite o departamento: '))
    list_equipamento.append(input('Digite o equipamento: '))
    list_numserial.append(int(input('Digite o número serial: ')))
    list_valor.append(float(input('Digite o valor: ')))
    resposta = input('Digite "S" p/ continuar: ').upper()


for indice in range(0,len(list_equipamento)):
    print('Equipamento..:', (indice+1))
    print('Nome............: ', list_equipamento[indice])
    print('Valor...........: ', list_valor[indice])
    print('Serial..........: ', list_numserial[indice])
    print('Departamento....: ', list_departamento[indice])
    print(' ')

    '''A função range() retorna uma série numérica no intervalo enviado como argumento.
    No código, o parâmetro se inicia no zero e o 'len' informa que só acabara quando a lista terminar'''

busca = input('Digite o nome do equipamento que deseja buscar: ')
for indice in range(0,len(list_equipamento)):

    if busca == list_equipamento[indice]:
        print('Serial...............: ', list_numserial[indice])
        print('Valor................: ', list_valor[indice])
        print(' ')

depreciacao = input('Digite o nome do produto que será depreciado: ')
for indice in range(0,len(list_equipamento)):
    if depreciacao == list_equipamento[indice]:
        print('Valor: ', list_valor[indice])
        print('')
        valorDividido = list_valor[indice] / 10
        valorDepreciado = list_valor[indice] - valorDividido
        print('Valor com depreciação: ',valorDepreciado)

danificacao = int(input('Digite o serial do equipamento danificado: '))
for indice in range(0,len(list_numserial)):
    if danificacao == list_numserial[indice]:
        del list_numserial[indice]
        del list_equipamento[indice]
        del list_valor[indice]
        del list_departamento[indice]
        break

for indice in range(0,len(list_equipamento)):
    print('Equipamento: ',(indice+1))
    print('Equipamentos:......: ', list_equipamento[indice])
    print('Departamento:......: ', list_departamento[indice])
    print('Serial.............: ', list_numserial[indice])
    print('Valor..............: ', list_valor[indice])

