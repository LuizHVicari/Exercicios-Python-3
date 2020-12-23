#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os numa lista. Caso o número já
#exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em
#ordem crescente

lista = list()

while True:
    lista.append(int(input('Informe um número: ')))

    keep = input('Deseja continuar? (s/n) ')
    keep = keep.lower()

    if keep == 'n':
        break

lista = lista.sort()

i = 0

while i < len(lista):
    if lista[i] == lista[i + 1]:
        del lista[i + 1]
    else:
        i =+ 1

print(lista)