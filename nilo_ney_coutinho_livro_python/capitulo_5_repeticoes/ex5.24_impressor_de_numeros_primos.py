n = int(input('''\033[1mVamos encontrar os números primos que estão entre o número 1 e o número que você digitar.
Digite um número inteiro: '''))
c = 1
p = 1
primo = False
while c < n:
    if primo == True:
        print(f'{c}, ',end='')
    primo = True
    p = 1
    c += 1
    m = 1
    while m < c-1:
        m += 1
        p = c % m
        if p == 0:
            primo = False