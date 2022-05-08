"""

Um vendedor ambulante tem que decidir que produtos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""

import math

def vendedor(capacidade,produtos):
    if capacidade == 0 or produtos == []:
        return 0, []
    p = list(filter(lambda t: t[2] <= capacidade, sorted(produtos, reverse=True, key=lambda t: t[1]/t[2])))
    l = [p[0][0]] * math.floor(capacidade/p[0][2])
    soma = p[0][1] * math.floor(capacidade/p[0][2])
    r = capacidade % p[0][2]
    aux = list(filter(lambda t: t[2] < r,p[1:]))
    while r != 0 and aux != []:
        next_product = max(aux, key=lambda t: t[1]/t[2] * math.floor(r/t[2]))
        l += [next_product[0]] * math.floor(r/next_product[2])
        soma += next_product[1] * math.floor(r/next_product[2])
        r = r % next_product[2]
        aux = list(filter(lambda t: t[2] < r, aux))
    return soma, sorted(l)
