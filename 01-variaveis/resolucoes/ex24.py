# Enunciado 24:
# Leia uma data dd/mm/aaaa e separe em dia, mes, ano.

data = input('Digite uma data no formato dia/mês/ano: ').strip()

dia, mes, ano = data.split('/')

print(f'''
Dia: {dia}
Mês: {mes}
Ano: {ano}
''')
