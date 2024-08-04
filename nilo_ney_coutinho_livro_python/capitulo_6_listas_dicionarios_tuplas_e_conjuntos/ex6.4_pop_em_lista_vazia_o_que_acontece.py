último = 10
fila = list(range(1, último + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operação = input('Operação (F, A ou S): ').upper().strip()
    if operação == 'A':
        atendido = fila.pop(0)
        print(f'Cliente {atendido} atendido.')
    elif operação == 'F':
        último += 1
        fila.append(último)
    elif operação == 'S':
        break
    else:
        print('Operção inválida! Digite apenas F, A ou S!')
# Quando os elementos da lista acabarem e o programa tentar extrair mais um acontecerá o erro: pop from empty list