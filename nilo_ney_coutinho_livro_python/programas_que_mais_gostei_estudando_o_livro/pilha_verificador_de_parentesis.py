# Primeira tentativa, sem ler as dicas do professor no livro:
'''while True:
    erro = 'N'
    parêntesis = input('Digite seus grupos de parêntesis, sem espaços entre eles, para vermos se estão dispostos corretamente ou S para sair: ').strip().upper()
    if parêntesis == 'S':
        break
    x = p1 = p2 = 0
    while True:
        if parêntesis[x] != '(' and parêntesis[x] != ')':
            print('Caracteres inválidos foram digitados! Tente novamente.')
            erro = 'S'
            break
        if parêntesis[x] == '(':
            p1 += 1
            x += 1
        elif parêntesis[x] == ')':
            p2 += 1
            x += 1
        if p1 < p2:
            break
        elif x >= len(parêntesis):
            break
    if erro != 'S':
        if p1 == p2 and p1 > 0:
            print('Seu conjunto de parêntesis está disposto corretamente.')
        else:
            print('Seu conjunto de parêntesis não está disposto corretamente.')'''

# Exercício feito pelo professor:

expressão = input("Digite a sequência de parênteses a validar:")
x = 0
pilha = []
while x < len(expressão):
    if expressão[x] == "(":
        pilha.append("(")
    if expressão[x] == ")":
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(")")  # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print("OK")
else:
    print("Erro")
