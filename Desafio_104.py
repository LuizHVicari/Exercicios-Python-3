# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do
# Python, só que fazendo a validação para aceitar apenas um valor numérico.

def leiaInt():
    n = input('Informe um número: ')
    if not n.isnumeric():
        print('Erro!')
        n = leiaInt()

    return int(n)


c = leiaInt()
print(c)