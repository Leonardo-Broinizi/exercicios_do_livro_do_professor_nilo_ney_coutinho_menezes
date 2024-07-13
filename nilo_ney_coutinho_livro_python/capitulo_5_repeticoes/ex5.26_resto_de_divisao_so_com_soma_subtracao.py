n1 = int(input('Vamos calcular o resto da divisão entre dois números.\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
resto = n1
while resto > n2:
    resto = resto - n2
print(f'O resto da divisão de {n1} por {n2} é igual a {resto}.')
