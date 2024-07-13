n = float(input('Digite um número para saber a raiz quadrada dele: '))
r = n ** (1/2)
print(f'A raiz quadrada de {n} é {r:.4f}.')

'''Agora a solução sugerida pelo livro do professor Nilo Ney Coutinho:  '''

n = float(input('Digite um número para saber sua raiz quadrada: '))
b = 2
while abs(n - (b * b)) > 0.00001:
    p = (b+(n/b))/2
    b = p
print(f'A raiz quadrada de {n} é aproximadamente {p:8.4f}.')