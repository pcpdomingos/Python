nome =  input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infectogiosa? ').upper()

if idade>=65 and doenca_infectocontagiosa=='SIM':
    print('O paciente '+nome+' será direcionado para sala AMARELA - COM prioridade.')
elif idade<65 and doenca_infectocontagiosa=='SIM':
    print('O paciente '+nome+' será direcionado para sala AMARELA - SEM prioridade.')
                                                                                        #SALA AMARELA: infectocontagiosa
                                                                                        #SALA BRANCA: sem doenças
elif idade >= 65 and doenca_infectocontagiosa == 'NAO':
    print('O paciente será direcionado para sala BRANCA - SEM proridade.')
elif idade < 65 and doenca_infectocontagiosa == 'NAO':
    print('O paciente será direcionaa=do para sala Branca - SEM prioridade.')
else:
    print('Responda a seuspeita de doença infectocontagiosa com SIM ou NAO')