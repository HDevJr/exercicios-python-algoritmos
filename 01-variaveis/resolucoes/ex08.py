# Enunciado 08:
# Leia um número de dias e converta para semanas e dias (ex.: 10 → 1 semana e 3 dias).

numero_de_dias = int(input('Digite o número de dias: '))
semanas = numero_de_dias // 7
dias = numero_de_dias % 7

print(f'{numero_de_dias} dias equivalem a {semanas} semana(s) e {dias} dia(s).')