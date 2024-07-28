'''cores = {'amarelo':'\033[33m',
         'azul':'\033[34m',
         'bold':'\033[1m',
         'limpa':'\033[m'}
l = ['','','','']
c = 0
while c < len(l):
    l[c] = input(f'{cores['amarelo']}Digite o {c+1}º nome: ')
    c += 1
p = int(input(f'{cores['azul']}Qual nome deseja recordar? '))
print(f'{cores['bold']}{l[p-1]}')'''

'''último = 10
fila = list(range(1, último + 1))
while True:
    print(f'\nExistem {len(fila)} clientes na fila.')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')
    operação = input('Operação (F, A ou S): ').upper().strip()
    if operação == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido.')
        else:
            print('Todos os clientes foram atendidos.')
    elif operação == 'F':
        último += 1
        fila.append(último)
    elif operação == 'S':
        break
    else:
        print('Operção inválida! Digite apenas F, A ou S!')'''

'''lista = []
lista1 = input('Digite o comando: ')
lista.extend(lista1)
print(f'{lista}{len(lista)}')'''

#   A seguir deixarei o código do professor Nilo para o exercício 6.6 (duas filas) para análise,
# pois achei muito interessante a forma como ele usa da 'clonagem' das listas nas linhas 18 e 20 (aqui, 61 e 63)
# para alterar as filas, como ele explica nas linhas 15 e 16 (58 e 59).

'''último = 0
fila1 = []
fila2 = []
while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1 e {len(fila2)} na fila 2.")
    print("Fila 1 atual:", fila1)
    print("Fila 2 autal:", fila2)
    print("Digite F para adicionar um cliente ao fim da fila 1 (ou G para fila 2),")
    print("ou A para realizar o atendimento a fila 1 (ou B para fila 2")
    print("S para sair.")
    operação = input("Operação (F, G, A, B ou S):")
    x = 0
    sair = False
    while x < len(operação):
        # Aqui vamos usar fila como referência a fila 1
        # ou a fila 2, dependendo da operação.
        if operação[x] == "A" or operação[x] == "F":
            fila = fila1
        else:
            fila = fila2
        if operação[x] == "A" or operação[x] == "B":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[x] == "F" or operação[x] == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[x] == "S":
            sair = True
            break
        else:
            print(
                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
            )
        x = x + 1
    if sair:
        break'''

# Pilha de pratos (miha tentativa sem olhar a do professor):
'''
pilha = []
sair = 'N'
último = 0
while True:
    x = 0
    prato = input('Digite A para adicionar um prato e B para lavar e remover, ou S para sair: ').upper().strip()
    while True and len(prato) > x:
        if prato[x] == 'A':
            pilha.append(último)
            último += 1
            x += 1
            print(f'{último}° prato adicionado.')
        elif prato[x] == 'B':
            if len(pilha) >= 1:
                último = pilha.pop(último-1)#Aqui eu poderia ter simplesmente colocado -1 que já resolveria o problema, já que, ao análisar listas, -1 é o equivalente ao último número. Só me dei conta quando vi a resolução do professor.
                x += 1
                print(f'{último + 1}° prato lavado.')
            else:
                print('Todos os pratos foram lavados.')
                x += 1
        elif prato[x] == 'S':
            print(f'Restaram {len(pilha)} pratos na pilha.')
            sair = 'S'
            break
        else:
            print('Comando inválido!')
            x += 1
    if sair == 'S':
        break
    print(f'Restam {len(pilha)} pratos na pilha.')

# Exercício feito pelo professor:

prato = 5
pilha = list(range(1, prato + 1))
while True:
    print(f"\nExistem {len(pilha)} pratos na pilha")
    print(f"Pilha atual: {pilha}")
    print("Digite E para empilhar um novo prato,")
    print("ou D para desempilhar. S para sair.")
    operação = input("Operação (E, D ou S):")
    if operação == "D":
        if len(pilha) > 0:
            lavado = pilha.pop(-1)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia! Nada para lavar.")
    elif operação == "E":
        prato += 1  # Novo prato
        pilha.append(prato)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas E, D ou S!")

l = [1, 3, 5, 8, 12, 15]
p = int(input('Digite o número a ser pesquisado: '))
n = 0
for e in l:
    if e == p:
        print(f'O número {p} foi encontrado na posição {n}.')
        break
    n += 1
else:
    print(f'O número {p} não foi encontrado.')'''

# ENUMERATE: praticar mais o uso dessa função!
'''L = [5,9,13]
for x, e in enumerate(L):
    print(f'[{x}]{e}')'''

'''lista = [32, 43, 22, 9, 87]
menor = maior = 0
for i in range(len(lista)):
    if i == 0:
        menor = maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]
    if lista[i] > maior:
        maior = lista[i]
print(menor,maior)'''

'''for e in lista:
    print(e)'''

'''
# Minha tentativa de fazer o programa 6.12 deste capítulo sem olhar a resolução do professor:

lista = [9,8,7,12,0,13,21]
ímpares = []
pares = []
for c in range(len(lista)):
    if lista[c]%2 == 0 and lista[c] != 0:
        pares.append(lista[c])
    elif lista[c]%2 == 1 and lista[c] != 0:
        ímpares.append(lista[c])
print(f'Pares {pares} e ímpares {ímpares}.')

# Código do professor Nilo:     

V = [9, 8, 7, 12, 0, 13, 21]
P = []
I = []
for e in V:
    if e % 2 == 0:
        P.append(e)
    else:
        I.append(e)
print('Pares: ', P)
print('Ímpares: ', I)'''

# Minha tentativa de fazer o programa 6.13 (controle da utilização de salas de um cinema) deste capítulo sem olhar a resolução do professor:

'''vagas_por_sala = [9, 8, 7, 12, 0, 13, 21] # Só quando terminei e ví o código do professor percebí que copie  a lista errada, mas isso não interfere na lógica do meu código.
while True:
    assentos = 0
    sala = int(input('Digite o número da sala [1, 2, 3, 4, 5] ou 0 para sair: '))
    if sala == 0:
        break
    else:
        assentos = int(input('Digite a quantidade de assentos que deseja reservar: '))
    if vagas_por_sala[sala-1] < assentos:
        print(f'Número de vagas superior à quantidade disponível! Temos {vagas_por_sala[sala-1]} assentos disponíveis nessa sala.')
    else:
        vagas_por_sala[sala-1] -= assentos
        print(vagas_por_sala)'''

# Código do professor Nilo (eu costumo deixar meu código mais completo que o do professor, mas dessa vez foi o contrário rs):

lugares_vagos = [10, 2, 1, 3, 0]
while True:
    sala = int(input('Sala (0 sai): '))
    if sala == 0:
        print('Fim')
        break
    if sala > len(lugares_vagos) or sala < 1:
        print('Sala inválida')
    elif lugares_vagos[sala-1] == 0:
        print('Desculpe, sala lotada!')
    else:
        lugares = int(input(f'Quantos lugares você deseja ({lugares_vagos[sala - 1]} vagos): '))
        if lugares > lugares_vagos[sala-1]:
            print('Esse número de lugares não está disponível.')
        elif lugares < 0:
            print('Número inválido')
        else:
            lugares_vagos[sala-1] -= lugares
            print(f'{lugares} lugares vendidos')
    print('Utilização das salas')
    for x, l in enumerate(lugares_vagos):
        print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')
