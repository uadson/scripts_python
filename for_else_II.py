from random import randint

# list comprehension: um for itera 20 vezes e cria uma lista com 20 números aleatórios entre 1 e 100
lista_de_numeros = [randint(1,100) for _ in range(20)]

# o usuário informa um número
numero = int(input('Informe um número: '))

# o laço for itera sobre a lista e verifica:
for num in lista_de_numeros:
    # se houver algum número na lista que seja igual ao número informado
    if num == numero:
        # imprime na tela o número e sua posição na lista
        print(f'Existe o número {numero} na posição {lista_de_numeros.index(numero)}\n')
        # imprime a lista
        print(lista_de_numeros)
        # encerra a iteração
        break
# se não houver o número, imprime a mensagem.
else:
    print('Não existe o número')

