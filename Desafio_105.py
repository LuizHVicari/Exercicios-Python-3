# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
# dicionário com as seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação (opcional)

def notas(*notas, sit=False):
    dic = dict()
    dic['quantidade'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    soma = 0
    for i in notas:
        soma += i
    dic['média'] = soma / len(notas)

    if sit:
        if dic['média'] > 7:
            dic['situação'] = 'boa'

        elif dic['média'] >= 6:
            dic['situação'] = 'razoável'

        else:
            dic['situação'] = 'ruim'


    return dic


resp = notas(4, 3, 10, 10, 10, 7, sit=True)
print(resp)