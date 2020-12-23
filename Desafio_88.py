# Faça um programa que ajude um jogador da tele sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint

jogos = list()
aux = list()

num = int(input('Quantos jogos deseja gerar? '))

for i in range(num):
    for j in range(6):
        aux.append(randint(0, 60))
        control = 0

        while control < j:
            if aux[j] == aux[control]:
                aux.pop(j)
                aux.insert(j, randint(0, 60))
                control = 0

            else:
                print('e')
                control += 1

    aux.sort()
    jogos.append(aux[:])
    aux.clear()

print('Jogos criados: ')

for i in range(num):
    print(jogos[i])