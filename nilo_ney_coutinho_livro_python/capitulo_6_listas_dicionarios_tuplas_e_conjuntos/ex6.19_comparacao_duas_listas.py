#    Minha resolução:

a = set([1, 12, 2, 21, 3, 22, 4])
b = set([1, 11, 23, 3, 43, 2, 5])
print(f'Lista a: {a}\nLista b: {b}')
print(f'Os valores comuns às duas listas são: {a | b}')
print(f'Os valores que existem apenas na lista A são: {a-b}')
print(f'Os valores que existem apenas na lista B são: {b-a}')
c = list(b - a)
c += list(a - b)
print(f'Uma valores que não se repetem nas duas listas são: {c}')
a = a-b
print(f'Os valores da lista A que não se repetem na lista B são: {a}')


#    Resolução do livro:

##############################################################################
'''Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
• os valores comuns às duas listas
• os valores que só existem na primeira
• os valores que existem apenas na segunda
• uma lista com os elementos não repetidos das duas listas.
• a primeira lista sem os elementos repetidos na segunda'''
##############################################################################
L1 = [1, 2, 6, 8]
L2 = [3, 6, 8, 9]

print(f"Lista 1: {L1}")
print(f"Lista 2: {L2}")

conjunto_1 = set(L1)
conjunto_2 = set(L2)

# Conjuntos suportam o operador & para realizar a interseção, ou seja,
# A & B resulta no conjunto de elementos presentes em A e B
print("Valores comuns às duas listas:", conjunto_1 & conjunto_2)
print("Valores que só existem na primeira:", conjunto_1 - conjunto_2)
print("Valores que só existem na segunda:", conjunto_2 - conjunto_1)

# Conjuntos suportam o operador ^ que realiza a subtração simétrica.
# A ^ B resulta nos elementos de A não presentes em B unidos
# com os elementos de B não presentes em A
# A ^ B = A - B | B - A
print("Elementos não repetidos nas duas listas:", conjunto_1 ^ conjunto_2)

# Repetido:
print("Primeira lista, sem os elementos repetidos na segunda:", conjunto_1 - conjunto_2)
