numint = int(input('Digite um número para descobrir se é ou não um palíndromo: '))
num = str(numint)
n = len(num) // 2
c = 1
p = 1
while c < n:
    if num[c-1] != num[-c]:
        p = 2
    c += 1
if p == 1:
    print(f'O número {numint} é um palíndromo.')
else:
    print(f'O número {numint} não é um palíndromo.')
