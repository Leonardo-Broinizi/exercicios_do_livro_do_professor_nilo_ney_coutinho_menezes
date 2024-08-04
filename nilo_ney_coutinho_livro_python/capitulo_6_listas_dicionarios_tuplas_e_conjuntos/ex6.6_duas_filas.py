x = a = b = 10
fila1 = list(range(1, x +1))
fila2 = list(range(1, x +1))
sair = 'N'
while True:
    if len(fila1) > 1:
        print(f'\n\033[1mRestam os números {fila1} na primeira fila.')
    elif len(fila1) == 1:
        print(f'\n\033[1mResta o número {fila1}  na primeira fila.')
    else:
        print(f'\n\033[1mTodos os clientes da primeira fila foram atendidos.')
    if len(fila2) > 1:
        print(f'\033[1mRestam os números {fila2} na segunda fila.')
    elif len(fila2) == 1:
        print(f'\033[1mResta o número {fila2} na segunda fila.')
    else:
        print(f'\033[1mTodos os clientes da segunda fila foram atendidos.')
    if sair == 'S':
        break
    comando = input('Digite: \nA - para adicionar cliente(s) na primeira fila,\nB - para adicionar cliente(s) na segunda fila,\nY - para atender cliente(s) a primeira fila,\nZ - para atender cliente(s) na segunda fila ou \nS - para encerrar: ').strip().upper()
    x = 0
    while x < len(comando) and sair != 'S':
        if comando[x] == 'A':
            a += 1
            fila1.extend([a])
        elif comando[x] == 'B':
            b += 1
            fila2.extend([b])
        elif comando[x] == 'Y':
            if len(fila1) > 2:
                atendido = fila1.pop(0)
                print(f'Cliente número {atendido} atendido na primeira fila.\nRestam {len(fila1)} clientes nessa fila.\n')
            elif len(fila1) == 2:
                atendido = fila1.pop(0)
                print(f'Cliente número {atendido} atendido na primeira fila.\nResta {len(fila1)} cliente nessa fila.\n')
            elif len(fila1) == 1:
                atendido = fila1.pop(0)
                print(f'Cliente número {atendido} atendido na primeira fila.\nNão restam clientes nessa fila.\n')
            else:
                print('Esta fila está vazia!\n')
        elif comando[x] == 'Z':
            if len(fila2) > 2:
                atendido = fila2.pop(0)
                print(f'Ciente número {atendido} atendido na segunda fila.\nRestam {len(fila2)} clientes nessa fila.\n')
            elif len(fila2) > 1:
                atendido = fila2.pop(0)
                print(f'Cliente número {atendido} atendido na segunda fila.\nResta {len(fila2)} cliente nessa fila.\n')
            elif len(fila2) == 1:
                atendido = fila2.pop(0)
                print(f'Cliente número {atendido} atendido na segunda fila.\nNão restam clientes nessa fila.\n')
            else:
                print('Esta fila está vazia!\n')
        elif comando[x] == 'S':
            sair = 'S'
            break
        else:
            print('Comando inválido! Por favor, tente novamente.')
        x += 1
