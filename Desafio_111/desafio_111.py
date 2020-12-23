# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as
# funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCEV import dado
from utilidadesCEV import moeda

preco = dado.validarInput('Informe o preço: ')
moeda.resumo(preco, 110, 50)