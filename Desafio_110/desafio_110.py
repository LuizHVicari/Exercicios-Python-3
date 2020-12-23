# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela
# algumas informaões geradas pelas funções que já temos no módulo criado

import moeda
preco = float(input('Informe o preço: '))
aumento = float(input('Informe o aumento: '))
desconto = float(input('Informe o desconto: '))
if input('Deseja formatar? (s/n) ') == 'n':
    formatar = False
else:
    formatar = True

moeda.resumo(preco, aumento, desconto, formatar)