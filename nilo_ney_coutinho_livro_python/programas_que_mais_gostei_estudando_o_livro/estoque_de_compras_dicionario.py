estoque = {'CAMISA':[101,159.99],
           'BERMUDA':[74,199.00],
           'CALÇA':[203,319.99],
           'BLUSA':[89,399.99],
           'MEIA':[381,29.50],
           'TIARA':[193,15.89]}
total = 0
while True:
    escolha = str(input('Qual item deseja comprar [digite FIM para sair]: ')).upper().strip()
    if escolha == 'FIM':
        break
    elif escolha not in estoque:
        print('Comando inválido! Tente novamente.')
    elif estoque[escolha][0] == 0:
        print('Produto fora de estoque! Por favor, tente novamente.')
    else:
        while True:
            quantidade = int(input('Digite a quantidade desejada: '))
            if estoque[escolha][0] < quantidade:
                print(f'Infelizmente só temos {estoque[escolha][0]} em estoque.\nPor favor, escolha outra quantidade.')
            else:
                estoque[escolha][0] = estoque[escolha][0] - quantidade
                total += estoque[escolha][1] * quantidade
                print('Compra efetuada com sucesso!')
                break
print(f'O valor total de suas compras foi: {total:.2f}.')