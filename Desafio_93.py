# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total

jogador = dict()
gols = list()
n_gols = 0
jogador['nome'] = input('Informe o nome do jogador: ')
num = int(input(f'Informe quantas partidas {jogador["nome"]} jogou: '))

for i in range(num):
    gols.append(int(input(f'informe quantos gols {jogador["nome"]} fez na {i + 1}º partida: ')))
    n_gols += gols[i]

jogador["gols"] = gols
jogador["n_gols"] = n_gols

print(f'Nome do jogador: {jogador["nome"]}\n'
      f'Seus gols nas partidas foram: {jogador["gols"]}\n'
      f'No total, ele marcou {jogador["n_gols"]} gols')
j = 1
for i in jogador["gols"]:
    print(f'Na {j}ª partida, ele marcou {i} gols')
