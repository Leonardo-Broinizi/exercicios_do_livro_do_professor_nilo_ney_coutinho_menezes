a = str(input('Digite a primeira frase: ')).strip().replace(' ', '')
b = str(input('Digite a segunda frase: ')).strip().replace(' ', '')
c = ''
for letra in a.lower():
    if letra.lower() not in b.lower():
        c += letra
print(f'As letras que apareceram na primeira frase e não apareceram na segunda são: {c}')
