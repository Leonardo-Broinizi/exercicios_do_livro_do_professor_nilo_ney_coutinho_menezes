#   Ex. 6.14: O que acontece quando a lista já está ordenada?
# Rastreie o Programa 6.20, mas com a lista L = [1, 2, 3, 4, 5].

#   Resposta: O programa fará apenas um laço do primeiro while, pois, após concluir todos os laços do segundo while,
# sem atender nenhuma vez a condição if dentro dele (que só é atendida caso haja algum número fora da ordem crescente),
# a variável 'trocou' que começou esse primeiro laço com False não receberá True (que só receberia dentro do if já referido),
# e isso atenderá a condição do final desse primeiro while, que dará um break na repetição.

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


#   Ex. 6.15: O que acontece quando dois números são iguais?
# Rastreie o Programa 6.20, mas com a lista L = [3, 3, 1, 5, 4].

#   Resposta: No primeiro laço do segundo while, a condição if não será atendida, pois há o mesmo número nas duas posições da lista comparadas,
# e a condição exige que o primeiro número seja maior que o segundo.
#   No segundo laço do segundo while, a condição if será atendida e o programa trocará o 3 da posição 1 com o 1 da posição 2.
# E a variável 'trocou' receberá True, o que garantirá pelo menos mais um laço do primeiro while.
#   No quarto laço desse segundo while, ele trocará o 5 da posição 4 pelo 4 da posição 5.
#   Quando terminarem os laços dessa primeira rodada do segundo while, o primeiro while fará sua segunda rodada e chamará novamente o segundo while.
#   Nessa segunda 'rodada' de laços do segundo while, o primeiro laço será atendido, pois agora o número da primeira posição (3) é maior que o da segunda (1), e serão invertidos.
# Isso garantirá a futura terceira rodada do primeiro while. Isso é importante aqui, porque, apesar da lista já estar ordenada,
# esse programa não tem como saber sem uma verificação, e pra isso servirá a proxima rodada.

# Ex. 6.16: Modifique o programa 6.20 para ordenar a lista em ordem decrescente. L = [1, 2, 3, 4, 5] deve ser ordenada como L = [5, 4, 3, 2, 1].

#   Obs.: Imagino que a resolução desse exercício ocorra apenas ao trocar um sinal de mais por menos,
# mas quero fixar bem esse código na cabeça então irei refazê-lo sem consultar o código do professor:

#   Minha resolução:

'''l = [1, 2, 3, 4, 5]
tl = len(l)-1
while True:
    trocou = False
    x = 0
    while x < tl:
        if l[x] < l[x+1]:
            trocou = True
            temporário = l[x+1]
            l[x+1] = l[x]
            l[x] = temporário
        x += 1
    if not trocou:
        break
    tl -= 1
for i in l:
    print(i,end=' ')'''

#   Obs. 2: Nesse ponto do livro, o professor menciona o método sort, que ordena uma lista,
# e a função sorted, que retorna os valores ordenados da lista, porém sem alterá-la de fato.
# Ex.:

lista = [5,1,4,2,7,9,8,3,6]
print(f'A lista original: {lista}')
print(f'Os elementos da lista ordenados pela função sorted: {sorted(lista)}')
print(f'Nossa lista ainda inalterada: {lista}')
lista.sort()
print(f'Nossa lista ordenada, agora de fato alterada, pelo método sort: {lista}')
lista.sort(reverse=True)
print(f'Nossa lista em ordem decrescente (novamente alterada de fato pelo método sorte com o valor reverse=True): {lista}')


