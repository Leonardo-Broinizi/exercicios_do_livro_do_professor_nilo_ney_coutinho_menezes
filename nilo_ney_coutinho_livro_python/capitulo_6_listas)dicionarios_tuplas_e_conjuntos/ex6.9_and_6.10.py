# Minha resolução (na minha tentativa já contemplei o enunciado do exercício 6.10 támbem):

l = [15, 7, 27, 39]
p = int(input('Digite o 1° número a procurar: '))
v = int(input('Digite o 2° número a procurar: '))
c = 0
pp = pv = -1
while c < len(l):
    if l[c] == p:
        pp = c
    elif l[c] == v:
        pv = c
    c += 1
if pp > -1 or pv > -1:
    if pp > -1 and pv > -1:
        if pp < pv:
            print(f'O primeiro número achado foi {p} na posição {pp}, e o segundo foi {v} na posiçõa {pv}.')
        else:
            print(f'O primeiro número achado foi {v} na posição {pv}, e o segundo foi {p} na posiçõa {pp}.')
    elif pp > -1:
        print(f'Apenas o número {p} foi encontrado na lista, na posição {pp}.')
    else:
        print(f'Apenas o número {v} foi encontrado na lista, na posição {pv}.')
else:
    print(f'Nenhum dos números {p} ou {v} foram encontrados na lista.')



# Resolução do professor:

L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar (p): "))
v = int(input("Digite o outro valor a procurar (v): "))
x = 0
achouP = False
achouV = False
primeiro = 0
while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1
if achouP:
    print(f"p: {p} encontrado")
else:
    print(f"p: {p} não encontrado")
if achouV:
    print(f"v: {v} encontrado")
else:
    print(f"v: {v} não encontrado")
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")