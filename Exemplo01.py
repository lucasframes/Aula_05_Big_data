valor_pedido = float(input('digite o valor: '))
distancia = float(input('distancia: '))
frete = 8

if valor_pedido > 50 and distancia <= 3:
    valor_final = valor_pedido
    mensagem = 'frete gratis'


else:
    frete = 8
    valor_final = valor_pedido + frete
    mensagem = f'frete de R$ {frete}'

    print(mensagem)
    print(f'valor final: R$ (valor_final:.2f)')