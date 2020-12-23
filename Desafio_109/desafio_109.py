# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import moeda

preco = float(input('Informe o preço: '))
aumento = float(input('Informe o aumento: '))
desconto = float(input('Informe o desconto: '))
if input('Deseja formatar? (s/n) ') == 'n':
    formatar = False
else:
    formatar = True
print(f'{preco} / 2 = {moeda.metade(preco, formatar)}')
print(f'{preco} * 2 = {moeda.dobro(preco, formatar)}')
print(f'{preco} com {aumento} % de aumento é {moeda.aumentar(preco, aumento, formatar)}')
print(f'{preco} com {desconto} % de desconto é {moeda.diminuir(preco, desconto, formatar)}')