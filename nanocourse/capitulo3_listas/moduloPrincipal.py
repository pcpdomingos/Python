from capitulo3_Funcoes.identificacaoDeFuncoes import *

minhaLista=[]
print('Preenchendo')
preencherIventario(minhaLista)
print('Exibindo')
exibirInventario(minhaLista)

print('Pesquisando')
localizarPorNome(minhaLista)
print('Alterando')
depreciarPorNome(minhaLista, 20)

print('Excluindo')
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print('Resumindo')
resumirValores(minhaLista)