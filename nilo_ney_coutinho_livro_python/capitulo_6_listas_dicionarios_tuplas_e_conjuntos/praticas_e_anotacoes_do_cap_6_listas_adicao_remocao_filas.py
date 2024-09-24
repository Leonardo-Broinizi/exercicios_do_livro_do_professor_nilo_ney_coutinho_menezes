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

'''lugares_vagos = [10, 2, 1, 3, 0]
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
        print(f'Sala {x + 1} - {l} lugar(es) vazio(s)')'''

#   Minha tentativa de fazer o programa 6.14 sem ver o código, só o enunciado.

'''compras = []
ítem = ''
cont = 0
while True:
    ítem = str(input('Digite o ítem desejado: ')).strip().upper()
    if ítem == 'FIM':
        break
    compras.append(ítem)
    cont += 1
print(f'Você comprou {cont} ítens, que são: {compras}')

#   Código do livro do programa 6.14:b
compras = []
while True:
    produto = input("Produto:")
    if produto ==  "fim":
        break
    compras.append(produto)
    for p in compras:
        print(p)

l = ['maças','uvas','kiwis']
for itens in l:
    print(itens,end=': ')
    for letras in itens:
        print(letras,end=' - ')
    print()
#   Programa 6.18, impressão das compras: 

produto1 = ['maça',10,0.30]
produto2 = ['pera',5,0.75]
produto3 = ['kiwi',4,0.98]
compras = [produto1,produto2,produto3]
for l in compras:
    print(f'Produto: {l[0]}')
    print(f'Quantidade: {l[1]}')
    print(f'Preço R${l[2]:.2f}\n')'''

#   Minha tentativa de criar o programa 6.19 sem ver o código do livro, apenas com o enunciado:

'''ListaGeral = []
while True:
    Lista = []
    continuar = ' '
    produto = str(input('Digite o nome do produto: ')).strip()
    Lista.append(produto)
    quantidade = int(input('Digite a quantidade: '))
    Lista.append(quantidade)
    preço = float(input('Digite o preço: '))
    Lista.append(preço)
    ListaGeral.append(Lista)
    while continuar not in 'SN':
        continuar = str(input('Quer cadastrar mais itens? [S/N]: ')).strip().upper()[0]
    print()
    if continuar == 'N':
        break
for i in ListaGeral:
    print(f'Produto: {i[0]}\nQuantidade: {i[1]}\nPreço R${i[2]:.2f}\n')
#   Análise após terminar meu código e ver o do professor Nilo no livro: eu não fiz exatamente o que ele estava pedindo, 
# mas cheguei perto. Agora, o código do professor é claramente mais enxuto, mesmo desconsiderando meus preciosismos. 
# Ainda preciso me empenhar em entender as possibilidades de manipulação dos elementos (nesse caso, listas)
# para encontrar soluções mais simples para meus desafios. A saga continua!

#   Programa 6.19 do livro:

compras = []
while True:
    produto = input("Produto: ")
    if produto == "fim":
        break
    quantidade = int(input('Quantidade: '))
    preço = float(input('Preço: '))
    compras.append([produto,quantidade,preço])
soma = 0.0
for e in compras:
    print(f"{e[0]:20s} x {e[1]:5d} {e[2]:5.2f} {e[1] * e[2]:6.2f}")
    soma += e[1] * e[2]
print(f"Total: {soma:7.2f}")'''

#   Minha tentativa antes de ver o código do livro de fazer um ordenador de números em listas:
'''lista = [3,1,81,93,32,23,1,2,39]
for contador1 in range(len(lista)):
    for contador2, números in enumerate(lista):
        if números > lista[contador1]:
            controle = lista[contador1]
            lista[contador1] = números
            lista[contador2] = controle
print(lista)
#  Comentario após ver o programa 6.20 com o método de bolhas: Apesar de meu  código resolver o problema, 
# ele faz isso com mais "força bruta"(com mais laços) que o do método de bolhas, que já é pesado (exige muito processamento).'''

#   (código do livro) Programa 6.20, ORDENAÇÃO PELO MÉTODO DE BOLHAS:


'''L = [7, 4, 3, 12, 8]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1
for e in L:
    print(e)'''

#   Dicionários:

'''tabela = {'Alface':0.45,
          'Batata':1.20,
          'Tomate':2.30,
          'Feijão':1.50}
while True:
    chave = str(input('Digite o ítem que deseja consultar ou FIM para sair: ')).strip()
    if chave.upper() == 'FIM':
        break
    elif chave in tabela:
        print(f'Produto: {chave} R${tabela[chave]:.2f}.')
    else:
        print('O produto digitado não foi encontrado.\nVerifique se digitou corretamente e tente novamente.')'''

#   Fiz o seguinte código para tentar criar um programa de estoque e vendas como o mencionado na descrição do programa 6.22,
# mas sem ver o código dele. Gostei bastante do resultado.

'''estoque = {'CAMISA':[101,159.99],
           'BERMUDA':[74,199.00],
           'CALÇA':[203,319.99],
           'BLUSA':[89,399.99],
           'MEIA':[381,29.50],
           'TIARA':[193,15.89]}
total = 0
while True:
    escolha = str(input('Qual item deseja comprar [digite FIM para sair]: ')).upper().strip()
    if escolha == 'FIM':
        break
    elif escolha not in estoque:
        print('Comando inválido! Tente novamente.')
    elif estoque[escolha][0] == 0:
        print('Produto fora de estoque! Por favor, tente novamente.')
    else:
        while True:
            quantidade = int(input('Digite a quantidade desejada: '))
            if estoque[escolha][0] < quantidade:
                print(f'Infelizmente só temos {estoque[escolha][0]} em estoque.\nPor favor, escolha outra quantidade.')
            else:
                estoque[escolha][0] = estoque[escolha][0] - quantidade
                total += estoque[escolha][1] * quantidade
                print('Compra efetuada com sucesso!')
                break
print(f'O valor total de suas compras foi: {total:.2f}.')'''

# Programa 6.22 - Exemplo de dicionário com estoque e operações de venda:

'''estoque = {'tomate':[1000,2.30],
           'alface':[500,0.45],
           'batata':[2001,1.20],
           'feijão':[100,1.50]}
venda = [['tomate',5], ['batata',10], ['alface',5]]
total = 0
print('Vendas:\n')
for operação in venda:
    produto, quantidade = operação
    preço = estoque[produto][1]
    custo = preço * quantidade
    print(f'{produto:12s}:{quantidade:3d} x {preço:6.2f} = {custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: {total:21.2f}\n')
print('Estoque:\n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: { dados[1]:6.2f}\n')

print()'''


#   Programa 6.23 - Exemplo de dicionário sem valor padrão:

'''d = {}
for letra in 'abracadabra':
    if letra in d:
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1
print(d)'''

#   Programa 6.23 - Simplificação do programa 6.23 usando o método get:

'''d = {}
for letra in 'abracadabra':
    d[letra] = d.get(letra, 0) + 1 # O método 'get' tenta obter a chave procurada. Caso não a encontre, retorna o segundo parâmetro, no caso 0. Se o segundo parâmetro não for especificado, get retornará None. 
print(d)'''



'''d = {'A':5, 'B': 8, 'C':12}
d['D'] = d.get('A',55)
print(d)'''

'''a = [1, 2, 3, 4, 5, 6]
b = tuple
b = tuple(a)
a[0] = 9

print(f'A: {a}, type(a): {type(a)}, B: {b}, type(b): {type(b)}')'''

'''lista_a = [1, 3, 5, 7, 9, 11, 12, 13, 14]
lista_b = [2, 4, 6, 8, 10, 11, 12, 13, 14]
print(f'lista_a: {lista_a}\nlista_b: {lista_b}')
print(f'Os valores que aparecem em ambas as listas são: {set(lista_a)|set(lista_b)}')
print(f'Os valores que não se repetem nas listas são: {set(lista_a) ^ set(lista_b)}')
print(f'Os valores que aparecem só na lista a são: {set(lista_a) - set(lista_b)}')
print(f'Os valores que aparecem só na lista a são: {set(lista_b) - set(lista_a)}')'''

