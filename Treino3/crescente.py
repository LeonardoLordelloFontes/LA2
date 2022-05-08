"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""

def crescente(lista):
    if lista == []:
        return 0
    lens = [1] * len(lista)
    for i in range(len(lista)):
        menores = []
        for j in range(i-1, -1, -1):
            if lista[j] <= lista[i]:
                menores.append(j)
        if menores != []:
            lens[i] += lens[max(menores, key=lambda j: lens[j])] 
    return max(lens)
