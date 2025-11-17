# Enunciado 16:
# Crie um programa que leia:
# - a velocidade máxima permitida na via
# - a velocidade do motorista
#
# Classificação:
# - Sem multa: velocidade ≤ limite
# - Multa leve: velocidade até 10% acima do limite
# - Multa grave: mais de 10% acima do limite
#
# Exiba o valor da velocidade excedida e a classificação da multa.

vel_max = float(input('Informe a velocidade máxima permitida na via: '))
vel_mot = float(input('Informe a velocidade do veículo: '))

excesso = vel_mot - vel_max

if vel_mot <= vel_max:
    print('Sem multa')
elif vel_mot <= vel_max * 1.10:
    print(f'Multa leve. Excedeu {excesso:.2f} km/h')
else:
    print(f'Multa grave! Excedeu {excesso:.2f} km/h')
