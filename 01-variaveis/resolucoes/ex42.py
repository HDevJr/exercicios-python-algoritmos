# Enunciado 42:
# Leia um valor em minutos e converta-o para horas, exibindo o resultado com duas casas decimais.

minutos = float(input('Digite o tempo em minutos: '))

horas = minutos / 60

print(f'{minutos:.0f} minutos equivalem a {horas:.2f} horas.')
