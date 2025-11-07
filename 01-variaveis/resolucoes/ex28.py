# Enunciado 28:
# Leia massa (kg) e altura (m) e calcule IMC.

massa = float(input('Digite o seu peso em quilos: '))
altura = float(input('Digite a sua altura em metros: '))

imc = massa / (altura ** 2)

print(f'O seu IMC é {imc:.2f}')