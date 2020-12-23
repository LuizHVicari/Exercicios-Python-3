#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qua foi o maios e o menor
#valor digitado e as suas respectivas posições na lista;

lista = list()

for i in range(5):
    lista.append(int(input('Informe um número: ')))

    if i == 0:
        maior_pos = 0
        menor_pos = 0
    else:
        if lista[i] > lista[maior_pos]:
            maior_pos = i
        elif lista[i] < lista[menor_pos]:
            menor_pos = i

print(f'O maior número digitado foi {lista[maior_pos]}, e está na posição {maior_pos}')
print(f'O menor npumero digitado foi {lista[menor_pos]}, e está na posição {menor_pos}')