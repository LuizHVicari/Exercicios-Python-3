#Crie um programa onde o usuário possa digitar cinco valores numériocs e cadastre-os em uma lista, já na posição
#correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela
#Assiti a aula para resolver os problemas

lista = list()

for i in range(0, 5):
    a = int(input('Informe um número:  '))

    if i == 0 or a > lista[-1]:
        lista.append(a)

    else:
        j = 0
        while j < len(lista):
            if a <= lista[j]:
                lista.insert(j, a)
                break

            j += 1

print(lista)