notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
c = 0
while c < len(notas):
    notas[c] = float(input(f'Digite a {c+1}ª nota: '))
    soma += notas[c]
    c += 1
media = soma / len(notas)
print(f'A média do aluno é: {media:.>10.2f}.')

