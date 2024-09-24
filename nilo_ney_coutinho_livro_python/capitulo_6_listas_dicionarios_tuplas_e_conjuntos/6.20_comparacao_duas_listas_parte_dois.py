'''Escreva um programa que compare duas listas.
Considere a primeira lista como a versão inicial e a segunda como a versão após alterações.
Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
• os elementos que não mudaram
• os novos elementos
• os elementos que foram removidos'''

l_a = [1, 3, 5, 7, 9, 10]
l_b = [1, 2, 3, 4, 6, 10]
c_a = set(l_a)
c_b = set(l_b)
c_c = set()
print(f'A lista inicial é: {l_a}\nA lista alterada é: {l_b}')
# c_c = c_a - c_b             # Essas duas linhas anuladas são uma alternativa de resolução do primeiro ítem da questão.
# print(f'c_c: {c_a - c_c}')
print('Os elementos que não mudaram são: ', end='')
for elementos in c_a:
    if elementos in c_b:
        c_c.add(elementos)
print(c_c)
print(f'Os novos elementos são: {c_b - c_a}')
print(f'Os elementos que foram removidos são: {c_a - c_b}')

print('\n\n\n')


#    Resolução do professor Nilo:

ANTES = [1, 2, 5, 6, 9]
DEPOIS = [1, 2, 8, 10]

conjunto_antes = set(ANTES)
conjunto_depois = set(DEPOIS)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Antes:", ANTES)
print("Depois:", DEPOIS)
print("Elementos que não mudaram: ", conjunto_antes & conjunto_depois) # anotação minha: O & (and) mostra os elementos comuns aos dois conjuntos.
print("Elementos novos", conjunto_depois - conjunto_antes)
print("Elementos que foram removidos", conjunto_antes - conjunto_depois)



print(c_a & c_b)
