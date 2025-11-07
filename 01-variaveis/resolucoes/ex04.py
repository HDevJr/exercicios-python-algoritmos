# Enunciado 04:
# Leia o preço de um produto e aplique 10% de desconto, mostrando o novo preço.

preco_produto = float(input('Digite o preço do produto: R$ '))

desconto = preco_produto * 0.10
novo_preco = preco_produto - desconto

print(f'''
Preço original:     R$ {preco_produto:.2f}
Desconto (10%):     R$ {desconto:.2f}
------------------------------
Preço com desconto: R$ {novo_preco:.2f}
''')