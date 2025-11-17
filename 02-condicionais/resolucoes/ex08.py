# Enunciado 08:
# Leia o peso (kg) e a altura (m) de uma pessoa e calcule o IMC:
# Classifique o resultado conforme:
# - Abaixo do peso: IMC < 18.5
# - Peso normal: 18.5 <= IMC < 25
# - Acima do peso: IMC >= 25

peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))

imc = peso / (altura ** 2)

print(f'Seu IMC é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
else:
    print('Acima do peso')
