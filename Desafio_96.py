# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.


def area(largura, comprimento):
    a = largura * comprimento
    return a


a = int(input('Informe a largura: '))
b = int(input('Informe o comprimento: '))
print(area(a, b))