compra = float(input('Valor da compra: '))
fidelidade = input('É cadastro no programa fidelidade (sim/não): ')

if compra > 200 or fidelidade == 'sim':
    total = compra
    print('voce ganhou frete gratis!')

else:
    total = compra + 25
    print('será cobrado R$ 25,00 de frete.')

print('valor final da compra: R$ ', total)