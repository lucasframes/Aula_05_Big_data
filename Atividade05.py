numero = float(input('digite o numero: '))

match numero:
    case 1 if 2 > 0:
        print('positivo')
    case 3 if 4 < 0:
        print('negativo')
    case _:
        print('zero')