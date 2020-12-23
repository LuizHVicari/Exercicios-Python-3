#Crie um programa que vai gerar cinco npumeros alatórios e colocar em uma tupla. depois disso, mostre a listagem de
#números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

a = randint(1,10)
b = randint(1,10)
c = randint(1,10)
d = randint(1,10)
e = randint(1,10)

numeros = (a, b, c, d, e)
ordenada = sorted(numeros)

print(f'Tupla {numeros}')
print(f'Maior número na tupla é: {ordenada[-1]} e o menor é {ordenada[0]}')