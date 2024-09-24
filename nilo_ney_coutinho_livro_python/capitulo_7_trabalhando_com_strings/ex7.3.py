#    Enunciado:

'''Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.
1ª string: CTA
2ª string: ABC
3ª string: BT
A ordem dos caracteres da terceira string não é importante.'''

#    Minha resolução:

A = str(input('Digite a primeira string: ')).replace(' ', '')
B = str(input('Digite a segunda string: ')).replace(' ', '')
C = ''
for l in A:
    if l not in B and l not in C:
        C += l
for l in B:
    if l not in A and l not in C:
        C += l
print(f'Os caracteres que não se repetem nas strings são: {C}')

#    Resolução do professor Nilo:

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

# Para cada letra na primeira string
for letra in primeira:
    # Verifica se a letra não aparece dentro da segunda string
    # e também se já não está listada na terceira
    if letra not in segunda and letra not in terceira:
        terceira += letra

# Para cada letra na segunda string
for letra in segunda:
    # Além de não estar na primeira string,
    # verifica se já não está na terceira (evitar repetições)
    if letra not in primeira and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres incomuns não encontrados.")
else:
    print(f"Caracteres incomuns: {terceira}")
