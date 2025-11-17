# Enunciado 14:
# Leia o valor dos três lados de um triângulo.
# Verifique se os lados formam um triângulo válido.
# Classifique como:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes
# Exiba a classificação.

lado_a = float(input('Informe o lado A: '))
lado_b = float(input('Informe o lado B: '))
lado_c = float(input('Informe o lado C: '))

triangulo_valido = (
    lado_a < lado_b + lado_c and
    lado_b < lado_a + lado_c and
    lado_c < lado_a + lado_b
)

if not triangulo_valido:
    print('Os valores informados NÃO formam um triângulo.')
else:
    if lado_a == lado_b == lado_c:
        print('Equilátero')
    elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
        print('Isósceles')
    else:
        print('Escaleno')
