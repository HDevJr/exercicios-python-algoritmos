# Enunciado 05:
# Converta uma temperatura de Celsius para Fahrenheit e Kelvin.

celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f'''
Temperatura em Celsius: {celsius:.2f}°C
Temperatura em Fahrenheit: {fahrenheit:.2f}°F
Temperatura em Kelvin: {kelvin:.2f}K
''')