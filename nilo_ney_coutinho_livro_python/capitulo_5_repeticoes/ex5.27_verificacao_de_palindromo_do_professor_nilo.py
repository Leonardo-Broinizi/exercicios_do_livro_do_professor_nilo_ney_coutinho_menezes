s = input("Digite o número a verificar, sem espaços:")
i = 0
f = len(s) - 1  # posição do último caracter da string
while f > i and s[i] == s[f]:
    f = f - 1
    i = i + 1
if s[i] == s[f]:
    print(f"{s} é palíndromo")
else:
    print(f"{s} não é palíndromo")


n = int(input("Digite o número a verificar:"))
q = 0
while 10**q < n:
    q = q + 1
i = q
f = 0
nf = ni = n  # Aqui nós copiamos n para ni e nf
pi = pf = 0  # e fazemos pi = pf (para casos especiais)
while i > f:
    pi = int(ni / (10 ** (i - 1)))  # Dígito mais à direita
    pf = nf % 10  # Dígito mais à esquerda
    if pi != pf:  # Se são diferentes, saímos
        break
    f = f + 1  # Passamos para o próximo dígito a esqueda
    i = i - 1  # Passamos para o dígito a direita seguinte
    ni = ni - (pi * (10**i))  # Ajustamos ni de forma a retirar o dígito anterior
    nf = int(nf / 10)  # Ajustamos nf para retirar o último dígito

if pi == pf:
    print(f"{n} é palíndromo")
else:
    print(f"{n} não é palíndromo")