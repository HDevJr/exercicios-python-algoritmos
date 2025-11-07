# Enunciado 20:
# Leia um inteiro e decomponha milhar, centena, dezena e unidade.

numero_int = int(input('Digite um número inteiro: '))

milhar = numero_int // 1000
centena = numero_int // 100 % 10
dezena = numero_int // 10 % 10
unidade = numero_int % 10

print(f'''
Milhar: {milhar}
Centena: {centena}
Dezena: {dezena}
Unidade: {unidade}
''')