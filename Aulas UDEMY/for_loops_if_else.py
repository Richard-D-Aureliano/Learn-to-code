import sleep 
compra_cofirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3):
    if compra_cofirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break
    else:
        print('Falha na compra')
        sleep (3)