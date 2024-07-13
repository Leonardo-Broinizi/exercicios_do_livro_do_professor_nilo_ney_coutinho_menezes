'''c = 1
linha = 1
while c <= 10:
    while linha <= 10:
        print(f'\033[33m{c:3}\033[m \033[7mx\033[m\033[34m {linha:3} \033[m\033[7m=\033[m\033[32m {c * linha:3}\033[m')
        linha += 1
    c += 1
    linha = 1

preco = 5.75
print(f'{preco:_^15.3f}')
'''

'''n = []
c = 0
while True:
    n1 = int(input('Digite um número, ou 0 para sair: '))
    if n1 == 0:
        break
    n.append(n1)
print(n)'''

l = []
l.append('a')
l.append('b')
l.append(['c','d'])
l = l + ['e']
l = l + ['f','g']
l.extend('h')
print(l)