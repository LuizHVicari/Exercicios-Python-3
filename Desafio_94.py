# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um
# dicionário e todos os dicionários em uma lista. No final, mostre:
# A-) Quantas pessoas foram cadastradas
# B-) A média de idade
# C-) Uma lista com as mulheres
# D-) Uma lista de pessoas com idade acima da média

pessoa = dict()
lista = list()
acima = list()
mulheres = list()

soma_idade = 0

while True:
    pessoa['nome'] = input('Informe o nome da pessoa: ')
    pessoa['sexo'] = input(f'Informe o sexo de {pessoa["nome"]} (H/M): ').lower()
    pessoa['idade'] = int(input(f'Infome a idade de {pessoa["nome"]}: '))

    soma_idade += pessoa['idade']

    lista.append(pessoa.copy())
    pessoa.clear()

    if input('Deseja continuar? (s/n)').lower() == 'n':
        break

media = (soma_idade / len(lista))

for individuo in lista:
    if individuo['idade'] > media:
        acima.append(individuo.copy())

    if individuo['sexo'] == 'm':
        mulheres.append(individuo.copy())


print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A lista de mulheres é: {mulheres}')
print(f'As pessoas com idade acima da média é: {acima}')
print(f'A média das idades é: {media}')
