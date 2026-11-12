# estrtutura match case
print('''
[1] - marketing
[2] - financeiro
[3 a 5] - admintração
[6 a 9] - ti
[10 a 20] - serviços gerais
''')

opcao = int(input('escolha uma opção: '))

match opcao:
    case 1:
        print('marketing')

    case 2:
        print('financeiro')

    case 3 | 4 | 5:
        print('administração')

    case opcao if 6 <= opcao <= 9:
        print('ti')

    case opcao if 10 <= opcao <= 20:
        print('serviços gerais')

    case _:
        print('opção invalido')
