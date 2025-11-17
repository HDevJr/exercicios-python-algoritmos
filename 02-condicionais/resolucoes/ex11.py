# Enunciado 11:
# Leia três notas, calcule a média e informe a situação do aluno:
# - Aprovado: média ≥ 7
# - Recuperação: 5 ≤ média < 7
# - Reprovado: média < 5

nota1 = float(input('Informe a °1 nota: '))
nota2 = float(input('Informe a °2 nota: '))
nota3 = float(input('Informe a °3 nota: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f'''
          Média: {media:.2f}
          Aluno aprovado''')
elif 5 <= media < 7:
    print(f'''
          Média: {media:.2f}
          Recuperação''')
else:
    print(f'''
          Média: {media:.2f}
          Reprovado''')
