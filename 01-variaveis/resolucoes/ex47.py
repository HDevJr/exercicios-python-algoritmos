# Enunciado 47:
# Crie variáveis para armazenar as notas de três disciplinas (por exemplo, Matemática, Português e Ciências).
# Em seguida, exiba um boletim formatado, mostrando o nome das disciplinas, as notas e a média final.

matematica = float(input('Nota de Matemática: '))
portugues = float(input('Nota de Português: '))
ciencias = float(input('Nota de Ciências: '))

media = (matematica + portugues + ciencias) / 3

print(f'''
Boletim Escolar
-----------------------------
Matemática: {matematica:.1f}
Português:  {portugues:.1f}
Ciências:   {ciencias:.1f}
-----------------------------
Média final: {media:.1f}
''')
