"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""

def maxsoma(lista):
    d = {0: lista[0]}
    for i in range(1, len(lista)):
        d[i] = lista[i]
        if d[i-1] > 0:
            d[i] += d[i-1]
    return max(d.values())
