# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

preco = float(input('Informe o preço: '))
aumento = float(input('Informe o aumento: '))
desconto = float(input('Informe o desconto: '))
print(f'{preco} / 2 = {moeda.metade(preco)}')
print(f'{preco} * 2 = {moeda.dobro(preco)}')
print(f'{preco} com {aumento} % de aumento é {moeda.aumentar(preco, aumento)}')
print(f'{preco} com {desconto} % de desconto é {moeda.diminuir(preco, desconto)}')