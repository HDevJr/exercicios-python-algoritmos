# Enunciado 30:
# Leia um número inteiro e converta para binário, octal e hexadecimal (strings).

numero = int(input('Digite um número inteiro: '))

binario = bin(numero)[2:]
octal = oct(numero)[2:]
hexadecimal = hex(numero)[2:].upper()

print(f'''
Número digitado: {numero}
-----------------------------
Binário:      {binario}
Octal:        {octal}
Hexadecimal:  {hexadecimal}
''')