# Enunciado 21:
# Leia um nome completo e exiba quantas letras tem (sem espaços).

nome_completo = input('Digite o seu nome completo: ')

quantidade = len(nome_completo.replace(' ',''))

print(f'O nome {nome_completo} tem {quantidade} letras sem contar espaços.')