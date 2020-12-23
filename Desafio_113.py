# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um
# número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(txt='Informe um número: ', erro='ERRO, INFORME UM VALOR VÁLIDO'):
    try:
        num = int(input(txt))
    except:
        print(erro)
        num = leiaInt()

    return num

def leiaFloat(txt='Informe um número: ', erro='ERRO, INFORME UM VALOR VÁLIDO'):
    try:
        num = float(input(txt))
    except:
        print(erro)
        num = leiaFloat()

    return num


print(leiaInt())
print(leiaFloat())