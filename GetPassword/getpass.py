import random
from string import digits
from string import punctuation
from string import ascii_letters

special_symbols = '!@#$%&*/|.;:'

caracteres = ascii_letters + digits + special_symbols

secure_random = random.SystemRandom()

length = int(input('Quantidade de Caracteres: '))
password = ''.join(secure_random.choice(caracteres) for _ in range(length))

print('-' * (length + 1))
print(password)
print('-' * (length + 1))