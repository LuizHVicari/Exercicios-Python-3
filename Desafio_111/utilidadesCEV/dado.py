def validarInput(txt):
    num = input(txt)

    if num.isnumeric():
        return float(num)

    else:
        num = validarInput(txt)
        return float(num)