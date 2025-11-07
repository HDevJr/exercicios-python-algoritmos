# Enunciado 40:
# Leia os dados de um produto (nome, categoria, preço e peso)
# e exiba uma ficha técnica formatada, usando uma f-string multilinha.

nome = input('Nome do produto: ')
categoria = input('Categoria: ')
preco = float(input('Preço (R$): '))
peso = float(input('Peso (kg): '))

print(f'''
Ficha Técnica do Produto
------------------------------
Nome:       {nome}
Categoria:  {categoria}
Preço:      R$ {preco:.2f}
Peso:       {peso:.2f} kg
------------------------------
''')
