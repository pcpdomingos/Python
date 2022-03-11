inventario=[]
resposta='S'
while resposta=='S':
    inventario.append(input('Equipamento: ')) #append adiciona um novo valor a lista
    inventario.append(float(input('Valor: ')))
    inventario.append(int(input('Número Serial: ')))
    inventario.append(input('Departamento: '))
    resposta=input("Digite 'S' para continuar: ").upper()

for elemento in inventario: #a estrutura foreac nos permite definir um nome para cada elemento que ele encontrar na lista, no nosso caso chamamos de "elemento"
    print(elemento)