#Crie um programa que tenha uma tupla totalmentente preenchida com uma contagem por exetneso, de zero até 20. Seu
#programa deverá ler um númeropelo teclado (entre 0 e 20) e mostrá-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Informe um número entre 0 e dezesseis: '))

    if num >= 0 and num <= 20:
        break

    print('Você digitou um número errado')

print("Você informou o número {}".format(numeros[num]))