#    Enunciado:

'''Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.
String: TTAAC
Resultado:
T: 2x
A: 2x
C: 1x'''

#    Minha resolução:

A = str(input('Digite a frase: ')).strip().replace(' ', '').upper()
controle = ''
for l in A:
    c = 0
    la = l
    if l not in controle:
        for ls in A:
            if ls == la:
                c += 1
        print(f'A letra {la} aparece {c} vezes' if c > 1 else f'A letra {la} aparece 1 vez.')
    controle += l

#    Eu imaginava que o código do professor estaria mais simples e lógico do que o meu,
# já que não consegui encontrar uma resolução muito simples. Gostei do código do professor.
#    Resolução do professor Nilo:

sequencia = input("Digite a string: ")

contador = {}

for letra in sequencia:
    contador[letra] = contador.get(letra, 0) + 1

for chave, valor in contador.items():
    print(f"{chave}: {valor}x")

