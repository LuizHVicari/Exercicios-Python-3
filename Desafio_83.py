#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#se a expressão passada está com os parenteses abertos e fechados na ordem correta

expressao = input('Digite uma expressão matemática: ')
cont = 0

for i in range(len(expressao)):
    if expressao[i] == '(':
        cont += 1
    elif expressao[i] == ')':
        cont -= 1

    if cont < 0:
        break

if cont != 0:
    print('Os parênteses não estão corretos')
else:
    print('Os parênteses estão corretos')