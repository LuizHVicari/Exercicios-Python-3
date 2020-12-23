# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números
# como um valor monetário formatado.

import moeda

preco = float(input('Informe o preço: '))
aumento = float(input('Informe o aumento: '))
desconto = float(input('Informe o desconto: '))
print(f'{preco} / 2 = {moeda.moeda(moeda.metade(preco))}')
print(f'{preco} * 2 = {moeda.moeda(moeda.dobro(preco))}')
print(f'{preco} com {aumento} % de aumento é {moeda.moeda(moeda.aumentar(preco, aumento))}')
print(f'{preco} com {desconto} % de desconto é {moeda.moeda(moeda.diminuir(preco, desconto))}')
print(moeda.moeda(preco))