# Enunciado 19:
# Leia a hora atual (0 a 23) e exiba uma saudação de acordo com o período:
# - "Bom dia"       para horas de 0 a <12
# - "Boa tarde"     para horas de 12 a <18
# - "Boa noite"     para horas de 18 a 23
# Caso a hora não esteja no intervalo válido, exiba uma mensagem de erro.

hora_atual = int(input('Informe a hora atual no formato de 24hrs: '))

if hora_atual < 0 or hora_atual > 23:
    print('Hora inválida')
elif hora_atual < 12:
    print('Bom dia')
elif hora_atual < 18:
    print('Boa tarde')
else:
    print('Boa noite')
