#   Fim com um pouco menos de detalhes do que costumo porque acabei de criar outro programa
# completo com essa mesma finalidade.

estoque = {'tomate': [1000, 2.30],
           'alface': [500, 0.45],
           'batata': [2001, 1.20],
           'feijão': [100, 1.50]}
total = 0
print('Vendas:\n')
while True:
    produto = ' '
    while produto not in estoque.keys() and produto.upper() not in 'FIM':
        produto = str(input('Digite o nome do produto ou FIM para sair: ')).strip()
    if produto.upper() == 'FIM':
        break
    quantidade = int(input('Digite a quantidade: '))
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f'{produto:12s}:{quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: {total:21.2f}\n')
print('Estoque:\n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')