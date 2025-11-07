# Enunciado 03:
# Leia dois números e calcule soma, subtração, multiplicação, divisão e resto.

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2 
divisao = numero1 / numero2 if numero2 != 0 else 'Divisão por zero não é permitida'
resto = numero1 % numero2 if numero2 != 0 else 'Resto por zero não é permitido'

print(f'''
Resultados:
---------------------------
Soma:            {soma:.2f}
Subtração:       {subtracao:.2f}
Multiplicação:   {multiplicacao:.2f}
Divisão:         {divisao if isinstance(divisao, str) else f"{divisao:.2f}"}
Resto:           {resto if isinstance(resto, str) else f"{resto:.2f}"}
''')
