# Enunciado 12:
# Leia a distância percorrida em km e calcule o valor do pedágio:
# - Até 100 km: R$ 10,00
# - De 100 km até 200 km (exclusivo): R$ 20,00
# - Acima de 200 km: R$ 30,00
# Exiba o valor correspondente.

dist_km = float(input('Informe a distância em km: '))

if dist_km <= 100:
    print('O valor do pedário é R$: 10,00')
elif dist_km < 200:
    print('O valor do pedágio é R$: 20,00')
else:
    print('O valor do pedágio é R$: 30,00')