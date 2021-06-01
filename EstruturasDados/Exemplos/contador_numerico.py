""" Representação de uma PILHA de números onde o último número a 
entrar será o primeiro a sair - LIFO (Last In First Out)."""

NUM = []
print(NUM)

qtde_itens = 5

num_base = 1

for i in range(qtde_itens):
	if len(NUM) == 0:
		NUM.append(num_base)
		num_base += 1
		print(NUM)
	else:
		NUM.pop()
		NUM.append(num_base)
		num_base += 1
		print(NUM)

# []
# [1]
# [2]
# [3]
# [4]
# [5]