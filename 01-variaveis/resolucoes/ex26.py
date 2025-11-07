# Enunciado 26:
# Leia lados de um triângulo e calcule semiperímetro (Heron, sem raiz).

lado1 = float(input('Informe o °1 lado: '))
lado2 = float(input('Informe o °2 lado: '))
lado3 = float(input('Informe o °3 lado: '))

semi_p = (lado1 + lado2 + lado3) / 2

heron_sem_raiz = semi_p * (semi_p - lado1) * (semi_p - lado2) * (semi_p - lado3)

print(f'''
Semiperímetro: {semi_p}
Heron(sem raiz): {heron_sem_raiz:.2f}
''')