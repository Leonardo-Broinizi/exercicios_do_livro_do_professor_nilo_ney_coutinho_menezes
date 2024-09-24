#    Enunciado:

'''Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
1ª string: AAACTBF
2ª string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.'''

#    Minha resolução:

A = str(input('Digite a primeira string: ')).upper().strip()
B = str(input('Digite a segunda string: ')).upper().strip()
C = ''
for l in A:
    if l in B and l not in C:
        C += l
print(f'Os caracteres comuns às duas strings são: {C.lower()}')

# Ambas as resoluções ficaram parecidas.
#    Resolução do professor Nilo:

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

terceira = ""

# Para cada letra na primeira string
for letra in primeira:
    # Se a letra está na segunda string (comum a ambas)
    # Para evitar repetidas, não deve estar na terceira.
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == "":
    print("Caracteres comuns não encontrados.")
else:
    print(f"Caracteres em comum: {terceira}")

