# Enunciado 34:
# Leia uma placa de veículo no formato brasileiro (7 caracteres, ex.: ABC1D23)
# e exiba separadamente os 3 primeiros caracteres (parte inicial)
# e os 4 últimos caracteres (parte final da placa).

placa = input('Digite a placa do veículo (ex: ABC1D23): ').strip().upper()

primeira_parte = placa[:3]
segunda_parte = placa[-4:]

print(f'''
Placa completa: {placa}
-----------------------------
Primeira parte (3 primeiros): {primeira_parte}
Última parte (4 últimos):     {segunda_parte}
''')
