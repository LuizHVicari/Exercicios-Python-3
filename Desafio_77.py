#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, mostrar para cada palavra
#quais são suas vogais

lista = ('Pudim', 'Hambuguer', 'Suco', 'Refrigerante')

for comida in lista:

    if comida == lista[0]:
        print(f'Na palavra {comida}, as vogais são:', end=' ')
    else:
        print(f'\nNa palavra {comida}, as vogais são:', end=' ')

    for i in range(len(comida)):
        if comida[i] == 'a' or comida[i] == 'e' or comida[i] == 'i' or comida[i] == 'o' or comida[i] == 'u':
            print(f'{comida[i]}', end=' ')