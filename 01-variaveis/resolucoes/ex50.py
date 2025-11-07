# Enunciado 50:
# Leia o dia, mês (em número) e ano,
# e exiba a data no formato humanizado, com o nome do mês por extenso
# (exemplo: “15 de outubro de 2025”).

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês (1–12): '))
ano = int(input('Digite o ano: '))

meses = [
    'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
    'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
]

nome_mes = meses[mes - 1]

print(f'{dia} de {nome_mes} de {ano}')
