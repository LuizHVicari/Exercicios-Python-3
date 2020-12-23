def aumentar(p, a):
    return p + p * (a / 100)


def diminuir(p, d):
    return p - p * (d / 100)


def dobro(p):
    return p * 2


def metade(p):
    return p / 2

def moeda(p):
    inteira = int(p)
    decimal = int((inteira - p) * 10)

    if decimal < 0:
        decimal *= -1

    if decimal < 10:
        string = 'R$' + str(inteira) + ',' + str(decimal) + '0'
    else:
        string = 'R$' + str(inteira) + ',' + str(decimal)
    return string