# Enunciado 38:
# Leia o nome completo de uma pessoa e gere um username no formato nome.sobrenome,
# com todas as letras em minúsculas.
# (Considere o primeiro e o último nomes da entrada.)

nome_completo = input('Digite seu nome completo: ').strip().lower()

partes = nome_completo.split()

username = f'{partes[0]}.{partes[-1]}'

print(f'Username gerado: {username}')