# Enunciado 41:
# Leia o preço de compra de um produto e a taxa de imposto (%) aplicada sobre ele.
# Calcule e exiba o preço final, incluindo o valor do imposto.

preco_compra = float(input('Digite o preço de compra (R$): '))
taxa_imposto = float(input('Digite a taxa de imposto (%): '))

preco_final = preco_compra + (preco_compra * taxa_imposto / 100)

print(f'''
Preço de compra: R$ {preco_compra:.2f}
Taxa de imposto: {taxa_imposto:.2f}%
-----------------------------
Preço final:     R$ {preco_final:.2f}
''')
