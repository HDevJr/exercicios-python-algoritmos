# Enunciado 11:
# Leia uma distância em km e converta para metros, centímetros e milímetros.

distancia_km = float(input('Digite a distância em quilômetros: '))
distancia_metros = distancia_km * 1000
distancia_centimetros = distancia_km * 100000
distancia_milimetros = distancia_km * 1000000

print(f'''
Distância em metros: {distancia_metros:.2f}
Distância em centímetros: {distancia_centimetros:.2f}
Distância em milímetros: {distancia_milimetros:.2f}
''')