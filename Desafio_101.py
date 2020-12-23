# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma
# pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(idade):
    if idade < 16:
        return 'NEGADO'
    elif idade < 18 or idade >= 70:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


ano = int(input('Informe o ano de nascimento: '))
i = 2020 - ano
print(f'O voto para {i} ano(s) é {voto(i)}')