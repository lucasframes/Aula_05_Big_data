codigo = int(input('codigo origem de produto: '))

if codigo == 1:
    print('regiao sul')
elif codigo == 2:
    print('regiao norte')
elif codigo == 3:
    print('regiao leste')
elif codigo == 4:
    print('regiao oeste')
elif codigo == 5 or codigo == 6:
    print('regiao nordeste')
elif codigo == 7 or codigo == 8 or codigo == 9:
    print('regiao sudeste')
elif codigo == 10:
    print('regiao centro oeste')
elif codigo == 11:
    print('regiao noroeste')
else:
    print('produto importado')