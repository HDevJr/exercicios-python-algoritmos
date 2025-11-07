# Enunciado 45:
# Leia um endereço no formato 'Rua, Número - Bairro, Cidade'
# e separe cada parte (rua, número, bairro e cidade) em variáveis distintas.

endereco = input("Digite o endereço (formato: Rua, Número - Bairro, Cidade): ").strip()

rua, resto = endereco.split(',', 1)
numero, resto = resto.split('-', 1)
bairro, cidade = resto.split(',', 1)

rua = rua.strip()
numero = numero.strip()
bairro = bairro.strip()
cidade = cidade.strip()

print(f'''
Rua:    {rua}
Número: {numero}
Bairro: {bairro}
Cidade: {cidade}
''')
