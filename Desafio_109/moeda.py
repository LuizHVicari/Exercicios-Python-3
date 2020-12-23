def aumentar(p, a, format=True):
    if format:
        return moeda(p + p * (a / 100))
    return p + p * (a / 100)


def diminuir(p, d, format=True):
    if format:
        return moeda(p - p * (d / 100))
    return p - p * (d / 100)


def dobro(p, format=True):
    if format:
        return (moeda(p * 2))
    return p * 2


def metade(p, format=True):
    if format:
        return moeda(p / 2)
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