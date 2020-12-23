# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem decrescente

lista = list()
aux = list()

for i in range(7):

    a = int(input('Informe um número: '))
    aux.append(a)

    if a % 2 == 0:
        aux.append('par')

    else:
        aux.append('impar')

    lista.append(aux[:])
    aux.clear()

lista.sort()

print('Pares: ', end='')

for i in range(7):
    if lista[i][1] == 'par':
        print(lista[i][0], end=' ')

print('\nImpares: ', end='')
for i in range(7):
    if lista[i][1] == 'impar':
        print(lista[i][0], end=' ')