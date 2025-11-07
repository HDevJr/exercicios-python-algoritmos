# Enunciado 29:
# Leia os dados de um produto: nome, SKU, preço e quantidade em estoque. Em seguida, exiba um resumo formatado do produto, mostrando também o valor total em estoque.

nome = input('Nome do produto: ')
sku = input('SKU do produto: ')
preco = float(input('Preço do produto (R$): '))
estoque = int(input('Quantidade em estoque: '))

valor_total_estoque = preco * estoque

print(f'''
Resumo do Produto
-------------------------
Nome: {nome}
SKU: {sku}
Preço: R$ {preco:.2f}
Estoque: {estoque} un.
Valor total em estoque: R$ {valor_total_estoque:.2f}
''')
