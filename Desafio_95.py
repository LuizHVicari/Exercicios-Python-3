# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de
# detalhes do aproveitamento de cada jogador.

jogador = dict()
time = list()
gols = list()

while True:

    n_gols = 0
    jogador['nome'] = input('Informe o nome do jogador: ')
    jogador['jogos'] = int(input(f'Informe quantas partidas {jogador["nome"]} jogou: '))

    for i in range(jogador['jogos']):
        gols.append(int(input(f'informe quantos gols {jogador["nome"]} fez na {i + 1}º partida: ')))
        n_gols += gols[i]

    jogador["gols"] = gols[:]
    gols.clear()
    jogador["n_gols"] = n_gols
    time.append(jogador.copy())
    jogador.clear()

    if input('Deseja informar um novo jogador?(s/n) ').lower() == 'n':
        break
i = 0

for player in time:
    print(f'{i}: {player["nome"]}, gols: {player["gols"]}, total: {player["n_gols"]}')
    i += 1

while True:
    if input('Deseja ver os dados detalhados de algum jogador? (s/n) ') == 'n':
        break

    i = int(input('Informe o número do jogador que deseja ver: '))

    player = time[i]
    gols_ = player['gols']

    for j in range(player['jogos']):
        print(f'No jogo {j + 1}, marcou {gols_[j]} gol(s)')
