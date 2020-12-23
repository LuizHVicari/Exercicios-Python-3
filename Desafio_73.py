#Crie uma tupla preenchida com os 20 primeiros colocados da Tabea do Campeonato Brasileiro de Futebol, na ordem de
#colocação. Depois mostre:
#A-) Apenas os 5 primeiros colocados
#B-) Os últimos 4 colocados na tabela
#C-) Uma lista com os times em ordem alfabética
#D-) Em que posição da lista está o time Chapecoense
#obs: Chapecoense não estava na série A, então vou usar o Fortaleza no lugar

brasileirao = ('São Paulo', 'Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Internacional', 'Grêmio', 'Fluminense', 'Santos', 'Corintians', 'Ceará - SC', 'Bragantino', 'Atlético-GO', 'Fortaleza', 'Athletico Paranaense', 'Sport Recife', 'Bahia', 'Vasco da Gama', 'Coritiba', 'Goiás', 'Botafogo')
print('5 primeiros colocados')
print(brasileirao[0:5])
print('4 últimos colocados:')
print(brasileirao[-4:-1])
print('Em ordem alfabética: ')
print(sorted(brasileirao))
print('O Fortaleza está na posição: ')
print(brasileirao.index('Fortaleza'))