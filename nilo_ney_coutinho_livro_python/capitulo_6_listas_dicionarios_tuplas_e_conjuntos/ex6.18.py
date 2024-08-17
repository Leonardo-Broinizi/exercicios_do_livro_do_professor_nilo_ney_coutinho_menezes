frase = str(input('Digite uma frase: ')).strip()
dicionário = {}
for letra in frase:
    if letra in dicionário:
        dicionário[letra] = dicionário[letra] + 1
    else:
        dicionário[letra] = 1
print(dicionário)