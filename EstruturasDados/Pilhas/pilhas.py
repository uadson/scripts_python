""" Usando listas como pilhas

Em uma pilha o ÚLTIMO adicionado é o PRIMEIRO a sair - LIFO (Last In First Out).
Os métodos de lista são muito úteis pois - list.append(x) - adiciona um item 
na última posição da lista e - pop() - sem parâmetros remove o item da última
posição."""


pilha = [1, 2, 3]
print(pilha) # [1, 2, 3]

# adicionando itens
pilha.append(4)
pilha.append(5)

print(pilha) # [1, 2, 3, 4, 5]


# removendo itens
print(pilha.pop()) # 5

print(pilha) # [1, 2, 3, 4]

print(pilha.pop()) # 4

print(pilha) # [1, 2, 3]