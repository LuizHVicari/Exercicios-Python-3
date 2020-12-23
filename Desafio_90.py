# Faça um programa qe leia o nome e média de um aluno, guardando também a situação em um dicionário. No final, mostro o
# conteúdo da estrutura na tela

aluno = dict()
aluno['nome'] = input('Informe o nome do aluno: ')
aluno['nota'] = int(input('Informe a nota do aluno: '))
if aluno['nota'] >= 7:
    aluno['situacao'] = 'aprovado'
else:
    aluno['situacao'] = 'reprovado'

print(aluno)