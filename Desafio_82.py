#Crie um programa que vai ler vários números e colocar em uma lista. Deposi disso, crie duas listas que vão conter
#apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
#listas geradas

lista_original = list()
lista_pares = list()
lista_impares = list()

while True:
    a = int(input('Informe um número (negativo para parar): '))
    if a < 0:
        break
    lista_original.append(a)
    if a % 2 == 0:
        lista_pares.append(a)
    else:
        lista_impares.append(a)
print('Lista:', lista_original)
print('Pares: ', lista_pares)
print('Impares: ', lista_impares)