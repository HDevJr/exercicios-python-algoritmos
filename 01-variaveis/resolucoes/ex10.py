# Enunciado 10:
# Leia base e altura de um retângulo e mostre área e perímetro.

base_retangulo = float(input('Digite a base do retângulo: '))
altura_retangulo = float(input('Digite a altura do retângulo: '))

area_retangulo = base_retangulo * altura_retangulo
perimetro_retangulo = 2 * (base_retangulo + altura_retangulo)

print(f'A área do retângulo é: {area_retangulo:.2f}')
print(f'O perímetro do retângulo é: {perimetro_retangulo:.2f}')