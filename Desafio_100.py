# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre
# todos os valores pares sorteados pela função anterior.

from random import randint


def sorteia(lis):
    for i in range(5):
        lista.append(randint(0, 100))


def soma_par(lis):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i

    print(soma)


lista = list()
sorteia(lista)
print(lista)
soma_par(lista)
