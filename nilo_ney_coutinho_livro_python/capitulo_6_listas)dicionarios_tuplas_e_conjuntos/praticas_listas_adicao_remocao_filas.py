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