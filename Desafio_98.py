# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# A-) De 1 até 10, de 1 em 1
# B-) De 10 até 0, de 2 em 2
# C-) Uma contagem personalizada

def contador(inicio, fim, passo, reverso):
    for i in range(1, 11):
        print(i, end=' ')
    print()

    for i in range(10, 0, -2):
        print(i, end=' ')
    print()

    if reverso:
        passo *= -1

        for i in range(inicio, fim - 1, passo):
            print(i, end=' ')
        print()

    else:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
        print()


inicio = int(input('Informe o inicio: '))
fim = int(input('Informe o fim: '))
passo = int(input('Informe o passo: '))
if passo == 0:
    passo = 1
if inicio > fim:
    reverso = True
else:
    reverso = False
contador(inicio, fim, passo, reverso)