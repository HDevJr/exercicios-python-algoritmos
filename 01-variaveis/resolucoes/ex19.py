# Enunciado 19:
# Cadastro simples: nome, email, telefone – imprima um “cartão” em 3 linhas.

nome = input('Informe seu nome: ')
email = input('Informe seu email: ')
telefone = input('Informe seu telefone: ')

print('\n--- Cartão de Contato ---')
print(f'''
Nome: {nome}
Email: {email}
Telefone: {telefone}
''')