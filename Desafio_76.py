#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular
#Vi a resolução do exercício para deixar centralizado

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20)

for i in range(0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:_<30}', end = '')
    else:
        print(f'R$ {produtos[i]:>5}')
