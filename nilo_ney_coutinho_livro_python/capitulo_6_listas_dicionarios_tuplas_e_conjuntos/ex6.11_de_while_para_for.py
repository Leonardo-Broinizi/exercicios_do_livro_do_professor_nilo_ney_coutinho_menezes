# Explicação, como pedida pelo exercício, de porque nem todos os 'while' podem ser transformados em 'for':
# Porque quando não sabemos quantas vezes iremos precisar repetir o laço, não conseguimos fazer o comando que encerrará uma estrutura de repetição.

l = []
while True:
    n = int(input('Digite um número (0 sai): '))
    if n == 0:
        break
    l.append(n)
for x in l:
    print(x)

# Resolução do professor Nilo:

L = []
while True:
    n = int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
for e in L:
    print(e) # Basicamente idêntico ao meu

# Respostas do professor:
# O primeiro while não pôde ser convertido em for porque
# o número de repetições é desconhecido no início.
