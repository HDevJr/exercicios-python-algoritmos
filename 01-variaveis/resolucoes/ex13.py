# Enunciado 13:
# Leia três notas e calcule média aritmética e ponderada (pesos 2,3,5).

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))

media_aritmetica = (nota1 + nota2 + nota3) / 3
media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / (2 + 3 + 5)

print(f'''
A média Aritimética é: {media_aritmetica:.2f}
A média Ponderada é: {media_ponderada:.2f}
''')