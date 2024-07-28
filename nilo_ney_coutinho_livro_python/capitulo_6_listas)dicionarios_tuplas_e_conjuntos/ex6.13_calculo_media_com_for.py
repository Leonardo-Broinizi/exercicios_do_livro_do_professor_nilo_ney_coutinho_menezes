T = [-10, -8, 0, 1, 2, 5, -2, -4] # Realmente fica bem mais prático realizar essas operações em listas com 'for'.
máximo = mínimo = T[0]
média = c = 0
for i in T:
    if i < mínimo:
        mínimo = i
    elif i > máximo:
        máximo = i
    média += i
    c += 1
média /= c
print(mínimo, máximo, média)
