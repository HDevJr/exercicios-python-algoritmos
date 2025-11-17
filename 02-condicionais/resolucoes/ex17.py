# Enunciado 17:
# Converter nota (0–100) em conceito A/B/C/D/E.

nota = int(input('Informe a sua nota (0 a 100): '))

if nota > 100 or nota < 0:
    print('Nota inválida')
elif nota >= 90:
    print('Nota A')
elif nota >= 80:
    print('Nota B')
elif nota >= 70:
    print('Nota C')
elif nota >= 60:
    print('Nota D')
else:
    print('Nota E')
