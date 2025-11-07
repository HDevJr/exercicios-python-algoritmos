# Enunciado 12:
# Leia um valor em reais e converta para dólares e euros (considere taxas fixas).

valor_reais = float(input('Digite o valor em reais: '))

taxa_dolar = 5.25
taxa_euro = 5.90

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f'Valor em dólares: {valor_dolar:.2f}')
print(f'Valor em euros: {valor_euro:.2f}')