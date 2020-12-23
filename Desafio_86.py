#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores do teclado

lista = list()
aux = list()

for i in range(3):
    for j in range(3):
        aux.append(int(input(f'Informe um valor para a posição [{i},{j}]: ')))

    lista.append(aux[:])
    aux.clear()

for i in range(3):
    for j in range(3):
        if j != 2:
            print(f'[ {lista[i][j]} ] ', end=' ')

        else:
            print(f'[ {lista[i][j]} ] ')