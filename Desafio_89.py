# Crie um programa que leia o nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuários possa vizualizar as notas de cada aluno
# individualmente

boletim = list()
aux = list()

while True:
    aux.append(input('Informe o nome do aluno: '))
    nota1 = int(input(f'Informe a primeira nota de {aux[0]}: '))
    nota2 = int(input(f'Informe a primeira nota de {aux[0]}: '))

    aux.append(nota1)
    aux.append(nota2)
    aux.append((nota1 + nota2) / 2)

    # Dessa forma, o espaço 0 será nome, 1 e 2 serão as notas do aluno e 3 será a média
    boletim.append(aux[:])
    aux.clear()

    if input('Deseja continuar? (s/n) ') == 'n':
        break

print('Notas dos alunos: ')

for i in range(len(boletim)):
    print(f'{i} Nome: {boletim[i][0]}. Média: {boletim[i][3]}')

while True:
    if input('Desjea ver a nota de algum aluno? (s/n)') == 'n':
        break

    i = int(input('Deseja ver a nota de qual aluno? '))
    print(f'As notas de {boletim[i][0]} foram: {boletim[i][1]}, {boletim[i][2]}')