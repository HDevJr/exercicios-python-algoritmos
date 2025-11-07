# Enunciado 44:
# Leia o nome de um arquivo no formato nome.ext e separe o nome e a extensão em variáveis distintas.

arquivo = input('Digite o nome do arquivo (ex: relatorio.pdf): ').strip()

nome, extensao = arquivo.split('.')

print(f'''
Nome do arquivo: {nome}
Extensão:        {extensao}
''')
