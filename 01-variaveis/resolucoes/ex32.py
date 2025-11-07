# Enunciado 32:
# Leia a largura, altura, profundidade e calcule o volume de uma caixa.

largura = float(input('Informe a largura da caixa (m): '))
altura = float(input('Informe a altura da caixa (m): '))
profundidade = float(input('Informe a profundidade da caixa (m): '))

volume = largura * altura * profundidade

print(f'''
Dimensões da Caixa:
---------------------------
Largura:      {largura:.2f} m
Altura:       {altura:.2f} m
Profundidade: {profundidade:.2f} m
---------------------------
Volume Total: {volume:.2f} m³
''')
