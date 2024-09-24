#    Enunciado:

'''Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
1ª string: AATTCGAA
2ª string: TG
3ª string: AC
Resultado: AAAACCAA'''

#    Minha resolução (imagino que arrumei um caminho mais complicado do que o do professor):

a = str(input('Digite a primeira frase: ')).strip()
b = str(input('Digite as letras que você deseja retirar: ')).strip()
while True:
    c = str(input(f'Digite em ordem as {len(b)} letras que você deseja inserir no lugar: ')).strip()
    if len(c) == len(b):
        break
    else:
        print(f'ERRO! Digite o número correto de letras {len(b)}.')
d = ''
print('O resultado é: ', end='')
for letra in a:
    troca = True
    for n, sub in enumerate(b):
        if letra == b[n]:
            d += c[n]
            troca = False
    if troca:
        d += letra
print(d)

#    Comparando com o do professor, até que não achei meu código muito mais complexo que o dele, mas eu deveria ter usado mais os conceitos ensinados no capítulo, como o método find.
#    Resolução do professor:

primeira = input("Digite a primeira string: ")
segunda = input("Digite a segunda string: ")
terceira = input("Digite a terceira string: ")

if len(segunda) == len(terceira):
    resultado = ""
    for letra in primeira:
        posição = segunda.find(letra)
        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == "":
        print("Todos os caracteres foram removidos.")
    else:
        print(
            f"Os caracteres {segunda} foram substituídos por "
            f"{terceira} em {primeira}, gerando: {resultado}"
        )
else:
    print("ERRO: A segunda e a terceira string devem ter o mesmo tamanho.")
