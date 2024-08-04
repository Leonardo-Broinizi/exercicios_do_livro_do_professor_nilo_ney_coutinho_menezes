lista = [1, 7, 2, 4] # Realmente fica bem mais prático realizar essas operações em listas com 'for'.
máximo = mínimo = lista[0]
for i in lista:
    if i < mínimo:
        mínimo = i
    elif i > máximo:
        máximo = i
print(mínimo, máximo)
