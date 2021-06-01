lista = [] # ou list()

# Métodos

""" append(x) - Adiciona um item ao FIM  da lista """

lista.append(1)
lista.append(1)
lista.append(2)
print(lista) # [1, 1, 2]


""" extend(iterable) - Prolonga a lista, adicionando no fim todos os elementos do 
argumento iterable passado como parâmetro."""

lista.extend('python')
print(lista) # [1, 1, 2, 'p', 'y', 't', 'h', 'o', 'n']


""" insert(i, x) - Insere um item em uma dada posição. O primeiro argumento
é o índice do elemento ANTES do qual será feita a inserção."""

lista.insert(3, 3)
lista.insert(10, 4)
print(lista) # [1, 1, 2, 3, 'p', 'y', 't', 'h', 'o', 'n', 4]
			 #	0  1  2 [3]  4    5    6    7    8    9  10


""" remove(x) - Remove o PRIMEIRO item encontrado na lista cujo valor é 
igual ao parâmetro passado. Se o valor não existir, uma exception ValueError
é retornada."""

lista.remove(1)
print(lista) # [1, 2, 3, 'p', 'y', 't', 'h', 'o', 'n']
#lista.remove(7)
#print(lista) # ValueError: list.remove(x): x not in list


""" pop(x) - Remove um item em uma dada POSIÇÃO na lista e o retorna.
Se nenhum índice é especificado - pop() - o ÚLTIMO item da lista é removido."""

lista.pop(2)
print(lista) # [1, 2, 'p', 'y', 't', 'h', 'o', 'n', 4]
lista.pop()
print(lista) # [1, 2, 'p', 'y', 't', 'h', 'o', 'n']


""" clear() - Remove todos os itens de uma lista."""

lista.clear()
print(lista) # []


""" index(x) - Devolve o índice de um item na lista com base no parâmetro
informado."""

lista = ['P', 'y', 't', 'h', 'o', 'n']
print(lista.index('P')) # 0
print(lista.index('t')) # 2


""" count(x) - Devolve o número de vezes em que um valor x aparece na lista."""

print(lista.count('h')) # 1


""" sort() - Ordena os itens na lista """

lista.sort()
print(lista) # ['P', 'h', 'n', 'o', 't', 'y']


""" reverse() - Inverte a ordem dos elementos da lista. """

lista.reverse()
print(lista) # ['y', 't', 'o', 'n', 'h', 'P']


""" copy() - Devolve uma cópia da lista """
lista2 = lista.copy()
print(lista) # ['y', 't', 'o', 'n', 'h', 'P']
print(lista2) # ['y', 't', 'o', 'n', 'h', 'P']

lista2.pop()
print(lista2) # ['y', 't', 'o', 'n', 'h']
