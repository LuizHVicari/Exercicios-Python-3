#  Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
#  manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def ajuda():
    função = input('\033[46:31m Bem vindo ao programa ajuda, informe qual função deseja buscar ajuda (sem os ()): \033[m')
    if função == 'FIM':
        print(f'\033[40:35m Programa encerrado \033[m')
    else:
        print('\033[41:36m')
        help(função)
        print('\033[41:36m')
        ajuda()


ajuda()