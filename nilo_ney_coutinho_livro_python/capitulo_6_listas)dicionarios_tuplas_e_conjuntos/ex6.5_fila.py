último = 10
fila = list(range(1, último + 1))
fim = ''
while True and fim != 'S':
    operaçãol = []
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operação = input('Operação (F, A ou S): ').upper().strip()
    operaçãol.extend(operação)
    c = 0
    while True and fim != 'S':
        if operaçãol[0] == 'A':
            if len(fila) > 0:
                atendido = fila.pop(0)
                del operaçãol[0]
                print(f'Cliente {atendido} atendido.')
            else:
                print('Todos os clientes foram atendidos.')
                del operaçãol[0]
        elif operaçãol[0] == 'F':
            último += 1
            fila.append(último)
            del operaçãol[0]
        elif operaçãol[0] == 'S':
            fim = 'S'
        else:
            print('Operação inválida! Digite apenas F, A ou S!')
            del operaçãol[0]
        c += 1
        if len(operaçãol) == 0:
            break