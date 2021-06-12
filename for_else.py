lista = ['Uadson', 'Emile', 'Castro', 'Feitosa']


for nome in lista:
    print(nome)
    # ao encontrar a palavra continue, vai para o próxima iteração
    continue
    # OUTPUT:
    # Uadson
    # Emile
    # Castro
    # Feitosa
print()

for nome in lista:
    # ao encontrar a palavra break, encerra a iteração
    print(nome)
    break

    # OUTPUT:
    # Uadson
print()

for nome in lista:    
    # se o valor da variável começa com a letra U
    if nome.startswith('U'):
        print(nome)
    # se não, imprime mensagem:
    else:
        print('Não existem mais nomes com a letra U')

    # OUTPUT:
    
    #Uadson
    #Não existem mais nomes com a letra U
    #Não existem mais nomes com a letra U
    #Não existem mais nomes com a letra U

print()
verificar_letra_no_nome = False

for nome in lista:
    if nome.upper().startswith('U'):
        verificar_letra_no_nome = True

if verificar_letra_no_nome:
    print('Existe nome com a letra U')
else:
    print('Não existe nome com a letra U')

# OUTPUT:
# Existe nome com a letra U

print()
for nome in lista:
    if nome.upper().startswith('U'):
        print('Existe nome com a letra U')
        break
else:
    print('Não existe nome com a letra U')

# OUTPUT:
# Existe nome com a letra U

print()
for nome in lista:
    if nome.upper().startswith('U'):
        continue
    print(nome)

    # OUTPUT:
    # Emile
    # Castro
    # Feitosa

print()
for nome in lista:
    if nome.upper().startswith('U'):
        print(nome)
        break

    # OUTPUT:
    # Uadson
    
