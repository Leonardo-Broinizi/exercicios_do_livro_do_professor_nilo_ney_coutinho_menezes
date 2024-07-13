c = 0
A1 = []
while True:
    A = (input('\n033[1mDigite o nome do participante do grupo A ou [SAIR] para encerrar: '))
    if A.strip().upper() == 'SAIR':
        break
    A1.append(A)
    c += 1
c = 0
B1 = []
while True:
    B = (input('\n033[1mDigite o nome do participante do grupo B ou [SAIR] para encerrar: '))
    if B.strip().upper() == 'SAIR':
        break
    B1.append(B)
    c += 1
l3 = A1 + B1
print(f'A lista com a junção dos participantes dos grupos A e B é: {l3}.')
