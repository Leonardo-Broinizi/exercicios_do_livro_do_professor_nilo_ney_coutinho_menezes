n = int(input('Digite um número inteiro: '))
m = 1
c = n
while m != 0 and c != 2:
    c -= 1
    m = n % c
    if m == 0:
        print(f'{n} não é um número primo!')
    if c == 2:
        print(f'{n} é um número primo!')