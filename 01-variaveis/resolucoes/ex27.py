# Enunciado 27:
# Leia o valor inicial de um investimento (capital) e a taxa de juros simples mensal (%).
# Calcule e exiba o valor total após 6 meses.

capital = float(input('Digite o valor inicial (capital): R$ '))
taxa = float(input('Digite a taxa de juros mensal (%): ')) / 100
tempo = 6

juros = capital * taxa * tempo
montante = capital + juros

print(f'''
Capital inicial: R$ {capital:.2f}
Taxa mensal: {taxa * 100:.2f}%
Tempo: {tempo} meses
-----------------------------
Juros acumulado: R$ {juros:.2f}
Valor total após {tempo} meses: R$ {montante:.2f}
''')
