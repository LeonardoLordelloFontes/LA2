'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''

def erdos(artigos,n):
    erdos = {'Paul Erdos': 0}
    queue = ['Paul Erdos']
    while queue:
        v = queue.pop(0)
        for artigo in artigos:
            if v in artigos[artigo]:
                for autor in artigos[artigo]:
                    if autor not in erdos:
                        erdos[autor] = erdos[v] + 1
                        queue.append(autor)
    return [x for x,y in list(filter(lambda t: t[1] <= n, sorted(erdos.items(), key=lambda t:(t[1], t[0]))))]
