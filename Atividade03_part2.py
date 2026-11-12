venda = float(input('valor da venda: '))

match venda:
    case venda if venda < 100:
        print('venda pequena')
        
    case venda if venda < 500:
        print('venda media')
    case _:
        print('venda grande')
        
        