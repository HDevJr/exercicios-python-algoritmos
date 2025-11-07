# Enunciado 39:
# Leia um número real e separe sua parte inteira e parte decimal em variáveis distintas.
# Em seguida, exiba as duas partes na tela.

numero = float(input('Digite um número real: '))

parte_inteira = int(numero)
parte_decimal = abs(numero - parte_inteira)

print(f'''
Número digitado: {numero}
Parte inteira:   {parte_inteira}
Parte decimal:   {parte_decimal:.4f}
''')
