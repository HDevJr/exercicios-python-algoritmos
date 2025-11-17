# Enunciado 05:
# Leia o número de vendas de maçãs e bananas e informe:
# - Qual fruta vendeu mais
# - Ou se houve empate

venda_banana = int(input('Informe a quantidade de bananas vendidas: '))
venda_maca = int(input('Informe a quantidade de maçãs vendidas: '))

if venda_banana > venda_maca:
    print('A banana foi a fruta que mais vendeu')
elif venda_banana < venda_maca:
    print('A maçã foi a fruta que mais vendeu')
else:
    print('Empate')
