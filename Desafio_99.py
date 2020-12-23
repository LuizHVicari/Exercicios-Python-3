# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.

from random import randint


def maior(lst):

    print(lst)
    maior = lst[0]

    for n in lst:
        if n > maior:
            maior = n


    print(f'O maior número é {maior}')


lista = list()
while input('Deseja executar o programa? (s/n) ').lower() == 's':
    tamanho = int(input('Qual o número de valores que deseja informar? '))

    for i in range(tamanho):
        lista.append(randint(1, 50))

    maior(lista)