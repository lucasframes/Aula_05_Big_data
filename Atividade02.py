nota = float(input('nota final: '))
frequencia = float(input('frenquencia (%): '))
mensalidade = float(input('valor da mensalida R$: '))

if nota >=7 and frequencia >=75:
    bolsa = mensalidade * 0.20
    print('aluno tem direito bolsa!')
    print('valor da bolsa: R$', bolsa)

else:
    print('aluno nao tem direito a bolsa')
