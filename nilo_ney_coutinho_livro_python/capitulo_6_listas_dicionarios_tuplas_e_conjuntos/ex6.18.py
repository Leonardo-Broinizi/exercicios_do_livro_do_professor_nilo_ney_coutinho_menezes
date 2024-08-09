frase = str(input('Digite uma frase: '))
dicionário = {}
for letras in frase:
    if letras in dicionário:
        dicionário[letras] = dicionário[letras] + 1
    else:
        dicionário[letras] = 1
print(dicionário)


