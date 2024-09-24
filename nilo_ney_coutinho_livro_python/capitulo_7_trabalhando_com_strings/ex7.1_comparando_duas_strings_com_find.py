#    Enunciado:
'''Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
1ª string: AABBEFAATT
2ª string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT'''

#    Minha resolução:

S_A = 'AABBEFAATT'
S_B = 'BE'
if S_B in S_A:
    print(f'{S_B} encontrado na posição {S_A.find(S_B)} de {S_A}')

#    Resolução do professor Nilo:

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")

posição = primeira.find(segunda)

if posição == -1:
    print(f"'{segunda}' não encontrada em '{primeira}'")
else:
    print(f"{segunda} encontrada na posição {posição} de {primeira}")

