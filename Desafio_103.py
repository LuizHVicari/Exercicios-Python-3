# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
# jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum
# dado não tenha sido informado corretamente.

def ficha(nome='', gols=0):
    if nome != '':
        print(f'O jogador {nome.title()} ', end='')
    else:
        print(f'O jogador desconhecido ', end='')

    if gols > 0:
        print(f'marcou {gols} gols no campeonato')

    else:
        print('não marcou gols no campeonato')


n = input('Informe o nome do jogador: ')

g = input('Informe o número de gols que o jogador marcou: ')

if g != '':
    ficha(n, int(g))
else:
    ficha(n)