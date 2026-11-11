# Notas

print("cálculo da média final")

# entrada das quatros notas

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
nota3 = float(input('terceira nota: '))
nota4 = float(input('quarta nota: '))

#calculo da média

media = (nota1 + nota2 + nota3 + nota4) / 4

print('média', media)

# veridficação do estudante

if media >=7:
    print('aprovado')

elif media >=5:
    print('recuperação')

else:
    print('reprovado')