#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A-) Quantas pessoas foram cadastradas
#B-) Uma listagem com as pessoas mais pesadas
#C-) Uma listagem com as pessoas mais leves
#Vi o vídeo da resolução para corrigir alguns erros no programa

lista = list()
aux = list()
maior = 0
menor = 0
maior_nome = list()
menor_nome = list()
i = 0

while True:
    aux.append(input('Informe o nome da pessoa: '))
    aux.append(int(input(f'Informe o peso de {aux[-1]}: ')))
    lista.append(aux[:])

    if i == 0:
        maior = aux[1]
        menor = aux[1]

    else:
        if maior < aux[1]:
            maior = aux[1]

        elif menor > aux[1]:
            menor = aux[1]

    if input('Deseja continuar? (s/n) ').lower() == 'n':
        break

    aux.clear()
    i += 1

for j in lista:
    if j[1] == maior:
        maior_nome.append(j[0])
    elif j[1] == menor:
        menor_nome.append(j[0])

print(f'Você cadastrou {len(lista)} pessoas')
print(f'O maior peso é {maior}kg, pertecendo a: {maior_nome}')
print(f'O menor peso é {menor}kg, pertecendo a: {menor_nome}')
