# Enunciado 23:
# TROCA: leia dois inteiros e troque seus valores sem variável temporária.

num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))

num1, num2 = num2, num1

print(f'O primeiro número é {num1} e o segundo número é {num2}')