# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

cadastro = {'nome': input('Informe o nome: '),
            'nascimento': int(input('Informe o ano de nascimento: ')),
            'carteira': int(input('Informe o número da carteira de trabalho dele(a): '))}
cadastro['idade'] = 2020 - cadastro['nascimento']

if cadastro['carteira'] == 0:
    print(f'Nome {cadastro["nome"].title()}\n'
          f'Ano de Nascimento: {cadastro["nascimento"]}\n'
          f'Idade: {cadastro["idade"]}\n'
          f'{cadastro["nome"].title()} não tem cateria de trabalho')
else:
    cadastro['contratação'] = int(input('Informe o ano de contratação: '))
    cadastro['salario'] = int(input(f'Informe é o salário de {cadastro["nome"]}: '))

    print(f'Nome {cadastro["nome"].title()}\n'
          f'Ano de Nascimento: {cadastro["nascimento"]}\n'
          f'Idade: {cadastro["idade"]}\n'
          f'Carteira de trabalho: {cadastro["carteira"]}\n'
          f'Salário: {cadastro["salario"]}\n'
          f'{cadastro["nome"].title()} vai se aposentar em {cadastro["contratação"] - 2020 + 35} anos')