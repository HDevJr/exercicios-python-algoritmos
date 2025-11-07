# Enunciado 48:
# Crie variáveis para armazenar latitude e longitude como strings
# e também como números float.
# Exiba as duas versões na tela (texto e valor numérico).

latitude_str = "-16.6869"
longitude_str = "-49.2648"

latitude_float = float(latitude_str)
longitude_float = float(longitude_str)

print(f'''
Coordenadas (em string):
Latitude:  {latitude_str}
Longitude: {longitude_str}

Coordenadas (em float):
Latitude:  {latitude_float}
Longitude: {longitude_float}
''')
