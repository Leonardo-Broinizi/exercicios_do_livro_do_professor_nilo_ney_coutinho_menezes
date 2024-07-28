l = [15, 7, 27, 39]
p = int(input('Digite o número a procurar: '))
c = 0
while c < len(l):
    if l[c] == p:
        break
    c += 1
if c < len(l):
    print(f'O número {p} foi achado na posição {c}.')
else:
    print(f'O número {p} não existe na lista.')