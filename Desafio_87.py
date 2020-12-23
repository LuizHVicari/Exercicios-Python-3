# Aprimore o desafio anterior, mostrando no final:
# A-) A soma de todos os valores pares digitados
# B-) A soma dos valores da terceira coluna
# C-) O maior valor da segunda linha

lista = list()
aux = list()
maior_segunda = 0
soma_pares = 0
soma_terceira = 0

for i in range(3):
    for j in range(3):
        a = int(input(f'Informe um valor para a posição [{i},{j}]: '))

        if i == 1:
            if a > maior_segunda:
                maior_segunda = a

        if a % 2 == 0:
            soma_pares += a

        if j == 2:
            soma_terceira += a

        aux.append(a)

    lista.append(aux[:])
    aux.clear()

for i in range(3):
    for j in range(3):
        if j != 2:
            print(f'[ {lista[i][j]} ] ', end=' ')

        else:
            print(f'[ {lista[i][j]} ] ')

print(f'A soma dos valores pares é: {soma_pares}')
print(f'A soma dos valores da terceira coluna é: {soma_terceira}')
print(f'O maior valor da segunda linha é: {maior_segunda}')