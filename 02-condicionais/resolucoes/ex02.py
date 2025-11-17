# Enunciado 02:
# Classificar idade: criança (0–12), adolescente (13–18), adulto (>18), inválida (<0).

idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('Idade inválida')
elif idade <= 12:
    print('Criança')
elif idade <= 18:
    print('Adolescente')
else:
    print('Adulto')