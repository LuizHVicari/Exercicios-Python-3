#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A-) Quantas vezes apareceu o valor 9
#B-) Em que posição foi digitado o primeiro valor 3
#C-) Quais fora os números pares

a = int(input('Informe um número: '))
b = int(input('Informe um número: '))
c = int(input('Informe um número: '))
d = int(input('Informe um número: '))

numeros = (a, b, c, d)

print(f'O número 9 apareceu {numeros.count(9)} vezes')
print(f'O número 3 foi encontrado pela primeira vez na posição {numeros.index(3)}')
print(f'Os números pares são: ')

for n in numeros:
    if n % 2 == 0:
        print(n)
