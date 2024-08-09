cores = {'bold':'\033[1m',
         'vermelho':'\033[31m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'negativo':'\033[7m',
         'limpa':'\033[m'}
resp = 'S'
while resp == 'S':
    n = int(input(f'{cores['bold']}{cores['amarelo']}Digite um número para descobrir se ele é um palíndromo: '))
    n1e = n2d = n
    ne = nd = c = 0
    while 10 ** c < n:
        c += 1
    c1 = int(c/2)
    c -= 1
    #    print(f'c:  {c}\nc1: {c1}')  Obs.: Os prints que desativei como comentários serviram (e podem servir futuramente) para mapear o exercício.
    while ne == nd and c1 > 0:
        ne = n1e // 10 ** c
        nd = n2d % 10
    #    print(f'ne: {ne}\nnd: {nd}')
        n1e = n1e % 10 ** c
        n2d = n2d // 10
        c -= 1
        c1 -= 1
    #    print(f' n1e: {n1e}\n n2d: {n2d}')
    if ne == nd:
        print(f'{cores['azul']}O número {n} é um palíndromo!')
    else:
        print(f'{cores['vermelho']}O número {n} não é um palíndromo!')
    resp = input(f'{cores['azul']}Deseja verificar outro número? [S/N]: ').strip().upper()
