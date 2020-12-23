#Crie um programa que vai ler vários número e colocar em uma lista. Deposi disso, mostre:
#A-) Quantos números foram digitados
#B-) A lista de valores, ordenada de forma decrescente
#C-) Se o valor 5 foi digitado e está ou não na lista

lista = list()

while True:
    lista.append(int(input('Informe um número: ')))

    keep = input('Deseja inserir novos números? (s/n) ')
    keep = keep.lower()

    if keep == 'n':
        break

print(f'Foram digitados {len(lista)} valores')
print(f'A lista ordenada de forma decrescente: ', end='')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('5 está na lista')
else:
    print('5 não está na lista')