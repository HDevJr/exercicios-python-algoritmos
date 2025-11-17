# Enunciado 07:
# Alerta se temperatura da sala > 25°C.

temperatura = float(input('Informe a temperatura em °C: '))

if temperatura > 25:
    print('Sala superaquecida')
else:
    print('Temperatura normal')