escolha = 'a'
while escolha != 'E':
    escolha = str(input('''Escolha a operação:
    \033[31m[-] SUBTRAÇÃO\033[m
    \033[32m[+] ADIÇÃO\033[m
    \033[33m[x] MULTIPLICAÇÃO\033[m
    \033[34m[:] DIVISÃO\033[m 
    \033[35m[e] ENCERRAR\033[m''')).upper().strip()
    c = 1
    l = 1
    if escolha == '-':
        while c <= 10:
            while l <= 10:
                print(f'{c:2} - {l:2} = {c-l:2}')
                l += 1
            l = 1
            c += 1
    elif escolha == '+':
        while c <= 10:
            while l <= 10:
                print(f'{c:2} + {l:2} = {c + l:2}')
                l += 1
            l = 1
            c += 1
    elif escolha == 'X':
        while c <= 10:
            while l <= 10:
                print(f'{c:3}  x{l:3} = {c * l:3}')
                l += 1
            l = 1
            c += 1
    elif escolha == ':':
        while c <= 10:
            while l <= 10:
                print(f'{c:2} : {l:2} = {c / l:2.2f}')
                l += 1
            l = 1
            c += 1
    elif escolha == 'E':
        print('\033[7mOperação encerrada!\033[m')
    else:
        print('\033[7mEscolha inválida!\033[m')