# Crie um programa onde 4 jogadroes joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em orde, sabendo que o vencedor tirou o maior número no dado
# Assisti o vídeo de resolução para fazer esse exercício

from random import randint
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print(jogadores)

ordenado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

k = 0

for i, j in ordenado:
    k += 1
    print(f'{k}º Lugar: {i} com {j} pontos')
