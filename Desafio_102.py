# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(num, show=False):

    fat = 1

    while num >= 1:
        fat = fat * num


        if show == True:

            if num != 1:
                print(num, end=' * ')

            else:
                print(num, end=' = ')

        num -= 1


    return fat


n = int(input('Informe o número que deseja mostrar o fatorial: '))
if input('Deseja ver o processo passo a passo? (s/n) ').lower() != 'n':
    print(fatorial(n, True))
else:
    print(f'{fatorial(n)} * 1 = ',fatorial(n))
