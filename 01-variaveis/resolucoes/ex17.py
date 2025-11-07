# Enunciado 17:
# Leia um tempo em segundos e converta para hh:mm:ss.

tempo_segundos = int(input('Digite o tempo em segundos: '))

tempo_horas = tempo_segundos // 3600
tempo_minutos = tempo_segundos // 60 % 60
tempo_segundos_restantes = tempo_segundos % 60

print(f'Tempo convertido: {tempo_horas:02d}:{tempo_minutos:02d}:{tempo_segundos_restantes:02d}')